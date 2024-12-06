import os
from webbrowser import Error

import gpxpy
import requests
from polyline import polyline

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
        return None, None, "File not found on server"


def parse_gpx(file):
    gpx = gpxpy.parse(file)
    points = [(point.latitude, point.longitude)
              for route in gpx.routes
              for point in route.points]
    return points

def get_route_img(route):
    print("get_route_img called")
    filename = route.imgURI
    print("imgURI: ", filename)
    try:
        img_path = os.path.join(BASE_DIR, 'images', 'route', filename)
        print(img_path)
        img_file = open(img_path, 'rb')
        return img_file, filename, "Ok"
    except FileNotFoundError:
        return None, None, "File not found on server"
    except TypeError:
        return None, None, "File not found on server"

def _encode_polyline(points):
    return polyline.encode(points)

def _generate_google_maps_url(encoded_polyline, api_key, size="1280x720"):
    return f"https://maps.googleapis.com/maps/api/staticmap?size={size}&path=enc:{encoded_polyline}&key={api_key}"

def generate_route_img(route_file, route):
    api_key = "YOUR_API_KEY"
    points = parse_gpx(route_file)
    encoded_polyline = _encode_polyline(points)
    url = _generate_google_maps_url(encoded_polyline, api_key)
    route.imgURI = f'{route.id}.jpg'
    return _save_route_img(url, route.id)

def _save_route_img(url, route_id):
    save_path = os.path.join(BASE_DIR, 'images', 'route', f'{route_id}.jpg')
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    else:
        return False