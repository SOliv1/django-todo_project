from django.test import TestCase
from .models import Item


class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        item = Item(name="Create a Test")
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertFalse(item.done)
    
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create a Test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)
    
    def test_item_as_a_string(self):
        item = Item(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
