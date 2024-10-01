from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        
        
class MenuViewTest(TestCase):

    def setUp(self):
        # Add test instances of the Menu model
        self.item1 = Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        self.item2 = Menu.objects.create(title="Burger", price=120.00, inventory=50)
        self.item3 = Menu.objects.create(title="Pizza", price=150.00, inventory=30)
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/menu/')  # Replace with your actual endpoint

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)