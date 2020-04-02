from django.shortcuts import render

# Create your views here.
def portifolio(request):
    context = {}
    return render(request, 'portifolio/about.html', context)
