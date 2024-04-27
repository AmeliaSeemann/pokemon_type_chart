from django.shortcuts import render,redirect,HttpResponse
from .models import TypeChart,Colors
# Create your views here.
def index(request):
    return redirect('/search')
def search(request):
    if request.get_full_path()=='/search/':
        return render(request, 'search.html',{})
    else:
        at = request.GET['attack']
        de = request.GET['defense']
        try:
            pokemon = TypeChart.objects.get(name=at)
            pokemon2 = TypeChart.objects.get(name=de)
        except Exception:
            return redirect('/')
        else:
            return redirect('/result/?attack={}&defense={}'.format(at,de))



def result(request):
    if request.method == 'POST':
        return redirect('/search/')
    else:
        try:
            a = request.GET['attack']
            d = request.GET['defense']
        except KeyError:
            return redirect('/search/')
        else:
            stage_one = TypeChart.objects.get(name=a)
            stage_two =getattr(stage_one,d)
            class Info:
                def __init__(self,at,de,ef,c1,c2):
                    self.c1 = c1
                    self.c2 = c2
                    self.at=at
                    self.de=de
                    if ef=="2":
                        self.ef="It's super effective!"
                    elif ef=="0.5":
                        self.ef="It's not very effective..."
                    elif ef=="0":
                        self.ef="It has no effect..."
                    else:
                        self.ef="Nothing special here..."
            code1 = Colors.objects.get(type=a).code
            code2 = Colors.objects.get(type=d).code
            obj = Info(a,d,stage_two,code1,code2)
            context = {'obj':obj}
            return render(request, 'result.html',context)