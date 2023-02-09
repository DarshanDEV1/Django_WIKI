from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
import pyttsx3

engine = pyttsx3.init()

# Create your views here.
def method_name(request):
	query = request.POST.get('text_input')
	query_range = request.POST.get('number_input')
	res = str(query)
	context = {'result' : wikipedia.summary(res, query_range)}
	return render(request, "index.html", context)

def say():
	pass