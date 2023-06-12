from audioop import reverse

from django.test import TestCase, Client

from users.models import User

client = Client()


class TestUser(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='New username 1',
            email='admin@gmail.com',
            phone='+123456789012',
            job='Developer',
            adress='Tashkent',
            birth_date='12/12/22',
            age='16',
            type='teacher'
        )

    def test_list_user(self):
        url = reverse('test-user-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
