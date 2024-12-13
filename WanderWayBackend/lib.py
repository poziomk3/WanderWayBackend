import gpxpy
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.views.route.lib import get_route_obj, get_route_file


def get_route_pois(route):
    gpx_file, gpx_file_name, status = get_route_file(route)

    if not gpx_file:
        return None, status

    gpx = gpxpy.parse(gpx_file)

    pois = [POI.objects.get(id=waypoint.extensions[0].text)
            for waypoint in gpx.waypoints]

    return pois, "Ok"
