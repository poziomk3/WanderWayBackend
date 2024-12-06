import os
import gpxpy
import requests
from decouple import config
from polyline import polyline

from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.settings import BASE_DIR


def get_route_obj(route_id):
    try:
        return Route.objects.get(id=route_id), "Ok"
    except Route.DoesNotExist:
        return None, "Route not found"


def get_route_file(route):
    file_name = route.filePath
    file_path = os.path.join(BASE_DIR, 'gpx', file_name)
    try:
        route_file = open(file_path, 'rb')
        return route_file, file_name, "Ok"
    except FileNotFoundError:
        return None, None, "Route file not found on server"


def get_poi_img(poi_id):
    try:
        poi = POI.objects.get(id=poi_id)
        filename = poi.imgURI
        img_path = os.path.join(BASE_DIR, 'images', 'poi', filename)
        try:
            img_file = open(img_path, 'rb')
            return img_file, filename, "Ok"
        except FileNotFoundError:
            return None, None, "Image file not found on server"
    except POI.DoesNotExist:
        return None, None, "POI not found"


def get_route_img(route_id, img_type):
    route, op_status = get_route_obj(route_id)
    if not route: return None, op_status
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


def _encode_polyline(points):
    return polyline.encode(points)


def _encode_markers(pois):
    marker_strs = [
        f"&markers=label:{poi[2]}|{poi[0]},{poi[1]}"
        for poi in pois
    ]
    return "".join(marker_strs)


def _generate_google_maps_url(encoded_polyline, encoded_markers, img_type, size="1280x720"):
    return f"https://maps.googleapis.com/maps/api/staticmap?size={size}{encoded_markers}&style=feature:poi|visibility:off&path=color:red|weight:10|enc:{encoded_polyline}&key={config('GOOGLE_MAPS_API_KEY')}&maptype={img_type}"


def _generate_route_img(route, img_type):
    route_file, filename, op_status = get_route_file(route)
    if not route_file: return False
    points, pois = _parse_gpx(route_file)
    url = _generate_google_maps_url(_encode_polyline(points), _encode_markers(pois), img_type)
    return _save_route_img(url, route.id, img_type)


def _save_route_img(url, route_id, img_type):
    save_path = os.path.join(BASE_DIR, 'images', 'route', f'{route_id}_{img_type}.jpg')
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    else:
        return False


def _parse_gpx(file):
    gpx = gpxpy.parse(file)
    points = [(point.latitude, point.longitude)
              for route in gpx.routes
              for point in route.points]
    pois = [(waypoint.latitude, waypoint.longitude, waypoint.name)
            for waypoint in gpx.waypoints]
    return points, pois
