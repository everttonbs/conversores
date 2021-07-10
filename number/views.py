from django.shortcuts import render

# Create your views here.

def conversor_num(request):
    return render(request, 'number/conversor_num.html')

def binario(request):

    return render(request, 'number/binario.html')

def hexadecimal(request):

    return render(request, 'number/hexadecimal.html')
