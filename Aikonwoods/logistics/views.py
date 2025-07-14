from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'logistics/home.html')

def about(request):
    return render(request, 'logistics/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company = form.cleaned_data['company']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            subject = f"New Contact Form Submission from {first_name} {last_name}"
            body = f"""
            Name: {first_name} {last_name}
            Company: {company if company else 'N/A'}
            Phone: {phone}
            Email: {email}

            Message:
            {message}
            """

            send_mail(
                subject,
                body,
                'jay.akwa511@gmail.com',
                ['jay.akwa511@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'logistics/contact.html', {'success': True})
    else:
        form = ContactForm()

    return render(request, 'logistics/contact.html', {'form': form})