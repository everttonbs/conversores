from django.shortcuts import render

# Create your views here.

def conversor_num(request):
    if 'number'in request.GET:
        decimal_number = request.GET['number']

        if decimal_number != '':
            if 'to_convert' in request.GET:
                if request.GET['to_convert'] == 'binario':
                    convert_number = _get_binario(int(decimal_number))
                elif request.GET['to_convert'] == 'hexadecimal':
                    convert_number = _get_hexadecimal(int(decimal_number))
                else:
                    context = None

                context = {
                    'decimal_number' : decimal_number,
                    'convert_number' : convert_number,
                    'type'           : request.GET['to_convert'],
                }

            else:
                context = None
        else:
            context = None
    else:
        context = None

    return render(request, 'number/conversor_num.html', context)

def _get_binario(dec_num):
    num_bin = list()
    while dec_num > 1:            
        num_bin.insert(0, dec_num % 2)
        dec_num = dec_num // 2
    num_bin.insert(0, dec_num)
        
    return num_bin

def _get_hexadecimal(dec_num):
    hex_number = list()
    dict_hex = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    while dec_num > 15:
        hex_number.insert(0, dict_hex[dec_num%16])
        dec_num = dec_num // 16
    hex_number.insert(0, dict_hex[dec_num])
    
    return hex_number

