from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def ListFunc(request):
    gdata = Guest.objects.all()
    #gdata = Guest.objects.all().order_by('title') # asc
    #gdata = Guest.objects.all().order_by('-title') # desc
    #gdata = Guest.objects.all().order_by('-id')[0:3] # 0~2 까지
    
    return render(request, 'list.html', {'gdata':gdata})

def InserFunc(request):
    return render(request, 'insert.html')

def InserOkFunc(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST['content'])
        Guest(
            title = request.POST.get('title'),
            content = request.POST['content'],
            regdata = datetime.now()
            ).save() # insert문
        
    return HttpResponseRedirect('/guest') # 추가후 목록보기