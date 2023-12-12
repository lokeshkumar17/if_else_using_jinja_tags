from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'a':100,'b':20,'c':150}
    return render(request,'jinja.html',d)
