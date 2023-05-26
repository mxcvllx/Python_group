from django.test import TestCase, Client

from common.models import ContactUs

client = Client()


class TestContactUs(TestCase):
    def setUp(self) -> None:
        self.contact = ContactUs.objects.create(
            country='Uzbekistan',
            city='Tashkent',
            street='Shayhantahur',
            location='my location',
            email='admin@gmail.com',
            phone='+998123456789',
        )

        self.new_contact_data = {
            "country": "Uzbekistan",
            "city": 'Tashkent',
            "street": "Shayhantahur",
            "location": "my location",
            "email": "admin@gmail.com",
            "phone": "+998123456789",
        }

    def test_contact_list(self):
        url = reversed("product_list_create")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"][0]["country"], self.contact.title)
