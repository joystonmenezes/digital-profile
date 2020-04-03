from django.urls import path
from .views import HomePageView, AboutPageView, DeptPageView, ContactPageView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
	path('contact/',ContactPageView.as_view(), name='contact'),
	path('about/',AboutPageView.as_view(), name='about'),
	path('dept/',DeptPageView.as_view(), name='dept'),
	
]