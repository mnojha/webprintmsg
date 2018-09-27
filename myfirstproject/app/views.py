from django.shortcuts import render , HttpResponse

# Create your views here.
def pagefirst(request):
	return HttpResponse("Hello Everyone..!")

def pagesecond(request):
	return HttpResponse("Good Morning..!")

def pagethird(request):
	return HttpResponse("Good Evening..!")