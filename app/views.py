from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

# Create your views here.

def contactPage(request):

	form = ContactForm

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get("name")
			email = form.cleaned_data.get("email")
			subject = form.cleaned_data.get("subject")
			message = form.cleaned_data.get("message")


			full_message = f"""
			Received message below from {name}, with email address {email}, {subject}
			________________________


			{message}
			"""
			send_mail(
				subject="Received contact form submission",
				message=full_message,
				from_email=settings.DEFAULT_FROM_EMAIL,
				recipient_list=[settings.NOTIFY_EMAIL],
				)
			return redirect('success')

	context = {'form':form}
	return render(request, 'app/contact.html', context)

def successPage(request):

	return render(request, 'app/success.html')