from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Prography
from django.core.files.storage import FileSystemStorage


# Create your views here.

def home(request):
    prographys = Prography.objects
    prographys_list=Prography.objects.all().order_by('-id')
    paginator = Paginator(prographys_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'prographys':prographys,'posts':posts}) 

def detail(request, prographys_id):
    prographys_detail = get_object_or_404(Prography, pk=prographys_id)
    return render(request, 'detail.html', {'prographys': prographys_detail})

def new(request): #new.html실행
    return render(request,'new.html') 

def create(request): #데이터베이스에 넣어줌
    prographys = Prography()
    prographys.title = request.GET['title']
    prographys.body = request.GET['body']
    prographys.pub_date = timezone.datetime.now()
    prographys.save()
    return redirect('/' + str(prographys.id))

def edit(request, prographys_id):

    prographys = Prography.objects.get(id=prographys_id)

    if request.method == 'GET':
        return render(request, 'edit.html', {'prographys':prographys})
    
    else:  
        
        prographys.title = request.POST['title']
        prographys.body = request.POST['body']
        prographys.pub_date = timezone.datetime.now()   
        prographys.save()
        return redirect('/' + str(prographys.id))


def delete(request, prographys_id):
    prographys = Prography.objects.get(id=prographys_id)
    prographys.delete()

    return redirect('/')

