import os
from django.test import TestCase
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.settings import BASE_DIR
from WanderWayBackend.views.route.lib import (
    get_route_obj, get_route_file, get_poi_img, get_route_img, _encode_polyline,
    _encode_markers, _generate_google_maps_url, _generate_route_img, _save_img, _parse_gpx
)

class RouteLibTests(TestCase):

    def setUp(self):
        # Set up test data
        self.route = Route.objects.create(filePath='test.gpx')
        self.poi = POI.objects.create(name='Test POI', description="POI created in order to conduct unit tests.", longitude=40.757937, latitude=-73.985563)

    def test_get_route_obj(self):
        route, status = get_route_obj(self.route.id)
        self.assertIsNotNone(route)
        self.assertEqual(status, "Ok")

    def test_get_route_file(self):
        route_file, file_name, status = get_route_file(self.route)
        self.assertIsNotNone(route_file)
        self.assertEqual(file_name, 'test.gpx')
        self.assertEqual(status, "Ok")

    def test_get_poi_img(self):
        img_file, filename, status = get_poi_img(self.poi.id)
        self.assertIsNotNone(img_file)
        self.assertEqual(filename, f'{self.poi.id}.jpg')
        self.assertEqual(status, "Ok")

    def test_get_route_img(self):
        img_file, filename, status = get_route_img(self.route.id, 'roadmap')
        self.assertIsNotNone(img_file)
        self.assertEqual(filename, f'{self.route.id}_roadmap.jpg')
        self.assertEqual(status, "Ok")

    def test_encode_polyline(self):
        points = [(1.0, 2.0), (3.0, 4.0)]
        encoded = _encode_polyline(points)
        self.assertIsInstance(encoded, str)

    def test_encode_markers(self):
        pois = [(1.0, 2.0, 'label1'), (3.0, 4.0, 'label2')]
        encoded = _encode_markers(pois)
        self.assertIsInstance(encoded, str)

    def test_generate_google_maps_url(self):
        url = _generate_google_maps_url('encoded_polyline', 'encoded_markers', 'roadmap')
        self.assertIn('https://maps.googleapis.com/maps/api/staticmap', url)

    def test_generate_route_img(self):
        result = _generate_route_img(self.route, 'roadmap')
        self.assertTrue(result)

    def test_parse_gpx(self):
        with open(os.path.join(BASE_DIR, 'gpx', 'test.gpx'), 'rb') as file:
            points, pois = _parse_gpx(file)
            self.assertIsInstance(points, list)
            self.assertIsInstance(pois, list)