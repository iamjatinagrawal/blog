from .models import ContactFormModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['full_name', 'email',
                  'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-lg-2'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-10'
        self.helper.add_input(Submit('submit', 'Save'))
