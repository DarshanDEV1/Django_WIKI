from django.urls import path
from . import views

urlpatterns = [
	path('wiki_dt/', views.method_name, name='wiki_dt'),
]