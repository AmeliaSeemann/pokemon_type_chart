from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return redirect('/search')
def search(request):
    return render(request, 'search.html',{})
def result(request):
    context={}
    return render(request, 'result.html',context)