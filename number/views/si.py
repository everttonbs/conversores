from django.shortcuts import render

def unit_lenght(request):
    if 'number' in request.GET:    
        try:
            number = float(request.GET['number'])

            dic_length = {
                'm'  : 1,
                'dm' : 10,
                'cm' : 100,
                'mm' : 1000,
            }
            in_si = dic_length[request.GET['in_si_length']]
            out_si = dic_length[request.GET['out_si_length']]
            convert_length = number / in_si * out_si

            context = {
                'number' : number,
                'si' : request.GET['out_si_length'],
                'convert_number' : convert_length
            }

        except ValueError:
            context=None
    else:
        context = None
   
    return render(request, 'si/length/convert_length.html', context)
    
    