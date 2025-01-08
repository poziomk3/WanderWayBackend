from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.models.route_model import Route


class RouteViewsTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.poi = POI.objects.create(name='Test POI', description="POI created in order to conduct unit tests.", longitude=0.0, latitude=0.0)
        self.route = Route.objects.create(filePath='test.gpx')

    def test_get_all_pois(self):
        url = reverse('get_pois')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('pois', response.data)

    def test_get_poi(self):
        url = reverse('get_poi', args=[self.poi.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.poi.id)

    def test_gen_routes(self):
        url = reverse('gen_routes')
        data = {'pois': [self.poi.id], 'preferences': {"key": "value"}}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('routeIds', response.data)

    def test_get_route(self):
        url = reverse('get_route', args=[self.route.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_route_img(self):
        url = reverse('get_route_img', args=[self.route.id])
        response = self.client.get(url, {'imgtype': 'roadmap'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)