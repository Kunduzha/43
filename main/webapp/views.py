from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(request,'index.html')

def second_view(request):
    return render(request,'second.html')

def third_view(request):
    num = 1
    return render(request,'third.html')
