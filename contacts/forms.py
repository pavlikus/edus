from django import forms
from django.conf import settings

from .tasks import send_email
from .models import Contact


class ContactForm(forms.ModelForm):
    
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():              
            if (hasattr(visible.field.widget, 'input_type') and
                    visible.field.widget.input_type == 'checkbox'):
                visible.field.widget.attrs['class'] = 'form-checkbox-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def is_valid(self):
        data = super().is_valid()
        for i in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[i].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return data

    def send_emails(self):

        first_name = self.cleaned_data['first_name']
        recipient = self.cleaned_data['email']
        message = self.cleaned_data['message']

        send_email.delay('New message from website',
                         f"{message}",
                         settings.DEFAULT_FROM_EMAIL,
                         recipients=settings.MANAGERS)

        send_email.delay('Thanks for your message',
                         f"Dear {first_name}, Thank you",
                         settings.DEFAULT_FROM_EMAIL,
                         recipients=[recipient])


        
    class Meta:

        model = Contact
        exclude = 'date_created', 
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Joe/Jane'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'email': forms.TextInput(attrs={'placeholder': 'joe@example.com', 'type': 'email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message or Comment'}), 
        }
