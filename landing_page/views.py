from django.shortcuts import render
from django.http import HttpResponse

# Initial landing page view.
# def index(request):
#     return render(request, 'landing_page/index.html')

def index(request):
    return HttpResponse('Hello')
#Add other views here