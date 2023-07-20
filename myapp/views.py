from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def info(request):
	return render(request,'1.html')
def web(request):
	return render(request,'2.html')
def about(request):
	return render(request,'3.html')
# Create your views here.
