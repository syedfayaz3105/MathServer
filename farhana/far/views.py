from django.shortcuts import render
def cylinderarea(request):
    context={}
    context['area'] = "0"
    context['b'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        b = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('radius=',b)
        print('height=',h)
        area  = 2 * 3.14 * int(b) * int(h) + 2 * 3.14 *int(b) * int(b)
        context['area'] = area
        context['r'] = b
        context['h'] = h
        print('area=',area)
    return render(request,'far/maths.html',context)

