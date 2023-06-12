from django.test import TestCase, Client

from common.models import AboutUs

client = Client()


class TestAboutUs(TestCase):
    def setUp(self) -> None:
        self.aboutus = AboutUs.objects.create(
            title='New title1',
            description='New descriptions 1',
        )
        self.new_about_data = {
            "title": "New title2",
            "descriptions": "New descriptions 2",
        }

    def test_aboutus_list(self):
        url = reversed('aboutus_list_create')

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"][0]["title"], self.aboutus.title)
