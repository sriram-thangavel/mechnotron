from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def counter(count,limit):
    if count > limit:
        return True
    return False

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully.')
            return ContactForm()
        else:
            messages.error(request, 'Error submitting.')
            messages.error(request, form.errors)
    else:
        form = ContactForm()
    return form
