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
        return result(request,at,de)
def result(request,a,d):
    stage_one = TypeChart.objects.get(name=a)
    stage_two =getattr(stage_one,d)
    return HttpResponse(a+d+stage_two)
    #return render(request, 'result.html',{})