from django.shortcuts import render

#importing http response
from django.http import HttpResponse


#function for accepting a request
def index(request):
    #return a HTTP response, and this response contains Html code
    return HttpResponse("<h>This is the books Homepage</h>")

