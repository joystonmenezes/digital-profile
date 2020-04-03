from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html'
class ContactPageView(TemplateView):
	template_name = 'contact.html'
class DeptPageView(TemplateView):
	template_name = 'dept.html'
class AboutPageView(TemplateView):
	template_name = 'about.html'

# Create your views here.
