from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import addContact, editContact, deleteContact

class TestUrls(SimpleTestCase):

    def test_add_contact_resolved(self):
        url = reverse('add-contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, addContact )

    # def test_edit_contact_resolved(self):
    #     url = reverse('edit-contact')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, editContact )

    # def test_delete_contact_resolved(self):
    #     url = reverse('delete-contact')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, deleteContact )