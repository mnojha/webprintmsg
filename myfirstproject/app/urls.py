from django.urls import path
from app.views import pagefirst,pagesecond,pagethird

urlpatterns = [
	path('pagefirst/',pagefirst, name = "Hello Everyone!"),
	path('pagesecond/',pagesecond, name = "Good Morning..!"),
	path('pagethird/',pagethird, name = "Good Evening..!"),
]