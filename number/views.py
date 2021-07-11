from django.shortcuts import render

# Create your views here.

def conversor_num(request):
    if 'number'in request.GET:
        decimal_number = request.GET['number']
    else:
        context = None

    return render(request, 'number/conversor_num.html')

def binario(request):

    return render(request, 'number/binario.html')

def hexadecimal(request):

    return render(request, 'number/hexadecimal.html')
