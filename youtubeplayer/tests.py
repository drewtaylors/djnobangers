from django.test import TestCase
from .models import Item, List

# Create your tests here.
class HomePageTest(TestCase):
        
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.url = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.url = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.url, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.url, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/youtubeplayer/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(url='itemey 1', list=correct_list)
        Item.objects.create(url='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(url='other list item 1', list=other_list)
        Item.objects.create(url='other list item 2', list=other_list)
    
        response = self.client.get(f'/youtubeplayer/{correct_list.id}/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/youtubeplayer/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/youtubeplayer/new', data={'item_url': 'A new list item'})       
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.url, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/youtubeplayer/new', data={'item_url': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/youtubeplayer/{new_list.id}/')

class NewItemTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        self.client.post(
            f'/youtubeplayer/{correct_list.id}/add_item', 
            data={'item_url': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.url, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/youtubeplayer/{correct_list.id}/add_item', 
            data={'item_url': 'A new item for an existing list'}
        )

        self.assertRedirects(response, f'/youtubeplayer/{correct_list.id}/')
        