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
    a = request.GET['attack']
    d = request.GET['defense']
    stage_one = TypeChart.objects.get(name=a)
    stage_two =getattr(stage_one,d)
    class Info:
        def __init__(self,at,de,ef):
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
    obj = Info(a,d,stage_two)
    context = {'obj':obj}
    return render(request, 'result.html',context)