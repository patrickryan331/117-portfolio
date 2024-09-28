from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail



def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        #send message
        print("Sending message")

        form = ContactForm(request.POST)

        if  form.is_valid():
            print("Sending")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message = f"Name:{name}\nEmail:{email}\nMessage:{message}"

            send_mail(
                "Email from " + name,
                email_message,
                email,
                ['patrick.ryan0331@gmail.com']
            )

        else:
            print("Invalid form")

    else:
        #display form
        form = ContactForm()

    form = ContactForm()
    return render(request, 'pages/contact.html',  {'form': form})