from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def agents(request):
    return render(request, 'agents.html')

def properties(request):
    return render(request, 'properties.html')

def propertysingle(request):
    return render(request, 'property-single.html')

def servicedetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starterpage(request):
    return render(request, 'starter-page.html')
def blog(request):
    return render(request, 'blog.html')
def singleblog(request):
    return render(request, 'single-blog.html')
def blogdetails(request):
    return render(request, 'blog-details.html')


