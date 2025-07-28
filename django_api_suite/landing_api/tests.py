from django.test import TestCase
from django.urls import reverse

class LandingAPITests(TestCase):
    def test_landing_api_index(self):
        response = self.client.get(reverse('landing_api:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Landing API")  # Assuming the view returns this text in the response