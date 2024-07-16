from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields """
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Hello!',
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_no_name_is_invalid(self):
        """Tests that form is invalid without name"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'message',
        })
        self.assertFalse(form.is_valid(), msg="No name was provided, but Form is valid")
    
    def test_no_email_is_invalid(self):
        """Tests that form is invalid without email"""
        form = CollaborateForm({
            'name': 'test',
            'email': '',
            'message': 'message',
        })
        self.assertFalse(form.is_valid(), msg="No mail was provided but Form is valid")
    
    def test_no_message_is_invalid(self):
        """Tests that form is invalid without message"""
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': '',
        })
        self.assertFalse(form.is_valid(), msg="No message was provided but Form is valid")