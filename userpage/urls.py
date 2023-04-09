from django.urls import path

from . import views

urlpatterns = [
	# ex: /userpage/
	path('', views.index, name='index'),

	path('calc', views.calculate, name='calculate'),
]