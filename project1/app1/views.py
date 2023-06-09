from django.shortcuts import render, redirect
from app1.models import Data
from app1.forms import Dataform

# Create your views here.
def emp(request):
    if request.method=="POST":
        form=Dataform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show/')
            except Exception as e:
                print(e)
                pass
    else:
        form=Dataform()
    return render(request,'index.html',{'form':form})


def show(request):
    data= Data.objects.all()
    return render(request,'show.html',{'data':data})

def delete(request,id):
    data= Data.objects.get(id=id)
    data.delete()
    return redirect('/show')



def edit(request,id):
    data=Data.objects.get(id=id)
    return render (request,'edit.html',{'data':data})


def update(request, id):
    data= Data.objects.get(id=id)
    form= Dataform(request.POST, instance=data)
    try:
        form.save()
        return redirect('/show')
    except Exception as e:
        print(e)
        pass
    return render(request,'edit.html',{'data':data})

