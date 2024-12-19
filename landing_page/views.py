from django.shortcuts import render
from django.http import HttpResponse

# Initial landing page view.
# def index(request):
#     return render(request, 'landing_page/index.html')

def index(request):
    
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
           
        </body>
    </html>
    '''
    return HttpResponse(html)
#Add other views here