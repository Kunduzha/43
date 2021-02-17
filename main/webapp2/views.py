from django.shortcuts import render

# Create your views here.
def webapp2_view(request):
    return render(request, 'demo.html', )