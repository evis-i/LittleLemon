from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuTest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, Decimal(80))
        self.assertEqual(item.inventory, 100)
