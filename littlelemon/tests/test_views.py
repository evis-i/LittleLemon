from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title = 'Carbonara', price = 10.9, inventory = 10)
        self.item2 = Menu.objects.create(title = "Tortellini", price = 14.5, inventory = 12)
        self.item3 = Menu.objects.create(title = "Baked Potatoes", price = 10.5, inventory = 14)
    
    def test_getall(self):
        self.assertEqual(Menu.objects.count(), 3)