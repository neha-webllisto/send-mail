from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from sendmail import settings

# Create your views here.

def mail(request):
	subject = 'Greetings'
	msg = 'Hello Neha'
	to = 'neha.webllisto@gmail.com'
	res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

	if res == 1:
		msg = 'Mail sent successfully'

	else:
		msg = 'Mail could not send'

	return HttpResponse(msg)