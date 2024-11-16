from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("This is the Landing Page!!")
