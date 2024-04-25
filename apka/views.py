from django.shortcuts import render,redirect,HttpResponse
from .models import TypeChart
# Create your views here.
def index(request):
    return redirect('/search')
def search(request):
    if request.get_full_path()=='/search/':
        return render(request, 'search.html',{})
    else:
        at = request.GET['attack']
        de = request.GET['defense']
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
            color_names = {
            "normal": '#A8A77A',
            "fire": '#EE8130',
            "water": '#6390F0',
            "electric": '#F7D02C',
            "grass": '#7AC74C',
            "ice": '#96D9D6',
            "fighting": '#C22E28',
            "poison": '#A33EA1',
            "ground": '#E2BF65',
            "flying": '#A98FF3',
            "psychic": '#F95587',
            "bug": '#A6B91A',
            'rock': '#B6A136',
            'ghost': '#735797',
            'dragon': '#6F35FC',
            'dark': '#705746',
            'steel': '#B7B7CE',
            'fairy': '#D685AD'
        }
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
            obj = Info(a,d,stage_two,color_names[a],color_names[d])
            context = {'obj':obj}
            return render(request, 'result.html',context)