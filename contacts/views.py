from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Contact


class ContactView(FormView):

    form_class = ContactForm
    template_name = 'contacts/form.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):

        form.save()
        try:
            form.send_emails()
            success_message = "We just sent you a confirmation email"
            messages.success(self.request, success_message)
        except Exception as e:
            # messages.warning(self.request, e)
            messages.warning(self.request, "Some errors. Email not sent to you")
        return super().form_valid(form)
