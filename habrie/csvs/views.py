from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def upload_file_view(request):
    return HttpResponse("Drop the file here")