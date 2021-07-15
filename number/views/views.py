from django.shortcuts import render

# Create your views here.

def convert_num(request):
    if 'number'in request.GET:
        decimal_number = int(request.GET['number'])

        if decimal_number != '':
            if 'to_convert' in request.GET:

                dict_type = {
                    'binario' : Binario(),
                    'hexadecimal' : Hexadecimal(),
                }

                # Cria um objeto, dependente do tipo de conversão
                type_convert = dict_type[request.GET['to_convert']]
                convert_number = type_convert._convert(decimal_number)                

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

    return render(request, 'number/convert_num.html', context)


class Binario():
    def _convert(self, dec_number):
        num_bin = list()
        while dec_number > 1:            
            num_bin.insert(0, dec_number % 2)
            dec_number = dec_number // 2
        num_bin.insert(0, dec_number)
        
        return num_bin
    
class Hexadecimal():
    def _convert(self, dec_num):
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
