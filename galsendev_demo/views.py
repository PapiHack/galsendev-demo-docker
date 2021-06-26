from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    # return HttpResponse("""
    # <h1>Hello World !</h1>
    # <h4>#galsendev #docker</h4>
    # """)
    return render(request, 'index.html')