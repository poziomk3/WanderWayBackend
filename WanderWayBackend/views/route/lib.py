import os
import gpxpy
import requests
from decouple import config
from polyline import polyline

from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.settings import BASE_DIR


def get_route_obj(route_id: int):
    try:
        return Route.objects.get(id=route_id), "Ok"
    except Route.DoesNotExist:
        return None, "Route not found"


def get_poi_obj(poi_id: int):
    try:
        return POI.objects.get(id=poi_id), "Ok"
    except POI.DoesNotExist:
        return None, "POI not found"


def get_route_file(route: Route):
    file_name = route.filePath
    file_path = os.path.join(BASE_DIR, 'gpx', file_name)
    try:
        route_file = open(file_path, 'rb')
        return route_file, file_name, "Ok"
    except FileNotFoundError:
        return None, None, "Route file not found on server"


def get_poi_img(poi_id: int):
    poi, op_status = get_poi_obj(poi_id)
    if not poi: return None, None, op_status
    filename = f"{poi.id}.jpg"
    img_path = os.path.join(BASE_DIR, 'images', 'poi', filename)

    if not os.path.exists(img_path):
        if not _generate_poi_img(poi):
            return None, None, "Failed to generate image"

    try:
        img_file = open(img_path, 'rb')
        return img_file, filename, "Ok"
    except FileNotFoundError:
        return None, None, "Image file not found on server"


def get_route_img(route_id: int, img_type: str):
    route, op_status = get_route_obj(route_id)
    if not route: return None, None, op_status
    filename = f"{route.id}_{img_type}.jpg"
    img_path = os.path.join(BASE_DIR, 'images', 'route', filename)

    if not os.path.exists(img_path):
        if not _generate_route_img(route, img_type):
            return None, None, "Failed to generate image"

    try:
        img_file = open(img_path, 'rb')
        return img_file, filename, "Ok"
    except FileNotFoundError:
        return None, None, "Image file not found on server"


def _encode_polyline(points: list) -> str:
    return polyline.encode(points)


def _encode_markers(pois: list) -> str:
    marker_strs = [
        f"&markers=label:{poi[2]}|{poi[0]},{poi[1]}"
        for poi in pois
    ]
    return "".join(marker_strs)


def _generate_google_maps_url(encoded_polyline: str, encoded_markers: str, img_type: str, size="1280x720") -> str:
    return f"https://maps.googleapis.com/maps/api/staticmap?size={size}{encoded_markers}&style=feature:poi|visibility:off&path=color:red|weight:10|enc:{encoded_polyline}&key={config('GOOGLE_MAPS_API_KEY')}&maptype={img_type}"


def _generate_poi_img(poi: POI) -> bool:
    search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={poi.latitude},{poi.longitude}&radius=200&key={config('GOOGLE_MAPS_API_KEY')}"
    response = requests.get(search_url)
    if response.status_code != 200:
        return False

    data = response.json()
    if not data['results']:
        return False

    print(data)

    photo_ref = None

    for place in data['results']:
        if 'photos' in place.keys():
            photo_ref = place['photos'][0]['photo_reference']
            break

    if not photo_ref:
        return False

    img_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={config('GOOGLE_MAPS_API_KEY')}"

    return _save_img(img_url, os.path.join(BASE_DIR, 'images', 'poi', f'{poi.id}.jpg'))


def _generate_route_img(route: Route, img_type: str) -> bool:
    route_file, filename, op_status = get_route_file(route)
    if not route_file: return False
    points, pois = _parse_gpx(route_file)
    url = _generate_google_maps_url(_encode_polyline(points), _encode_markers(pois), img_type)
    return _save_img(url, os.path.join(BASE_DIR, 'images', 'route', f'{route.id}_{img_type}.jpg'))


def _save_img(url: str, save_path: str) -> bool:
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        return False
    print("Image fetched... saving image to", save_path)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    return True


def _parse_gpx(file):
    gpx = gpxpy.parse(file)
    points = [(point.latitude, point.longitude)
              for route in gpx.routes
              for point in route.points]
    pois = [(waypoint.latitude, waypoint.longitude, waypoint.name)
            for waypoint in gpx.waypoints]
    return points, pois
