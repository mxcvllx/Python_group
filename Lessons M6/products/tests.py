from django.test import TestCase, Client
from django.urls import reverse

from common.models.category_models import Category, Brand
from products.models import Product

client = Client()


class TestProduct(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(title="New cat1")
        brand = Brand.objects.create(title="New brand")
        self.product = Product.objects.create(
            title="New product1",
            price=1000,
            category=self.category,
            brand=brand,
        )
        self.new_product_data = {
            "title": "new product2",
            "price": 2000,
            "category": self.category.id,
            "brand": brand.id
        }

    def test_product_list(self):
        url = reverse("products_list_create")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["title"], self.product.title)

    def test_product_create(self):
        url = reverse("products_list_create")

        response = client.post(url, data=self.new_product_data)

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["title"], self.new_product_data["title"])

    def test_product_detail(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product.title, "New product1")

    def test_product_update(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})
        data = {
            "title": "string",
            "price": 3000,
            "category": self.category.id
        }
        response = client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])

    def test_product_delete(self):
        url = reverse("product_detail", kwargs={"slug": self.product.slug})

        response = client.delete(url)

        self.assertEqual(response.status_code, 204)
