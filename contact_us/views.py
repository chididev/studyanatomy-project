from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'settings.EMAIL_HOST_USER',
                          ['chidihenry2018@outlook.com'],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    form = ContactForm()
    return render(request, "contact_us/contact.html", {'form': form})
