from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from. models import mymodel
from .forms import myform
from django.contrib.auth import authenticate ,logout, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

app_name ='myapp'

def home(request):
    all_model = mymodel.objects.all()
    return render(request, 'myapp/home.html',{'all_model': all_model})

def detail(request,id):
    sanu = mymodel.objects.get(id=id)
    return render(request, 'myapp/detail.html',{'sanu':sanu})

def add_new(request):
    if request.method == 'POST':
        form = myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = myform()
    return render(request, 'myapp/add_new.html', {'form':form})



def update(request, id):
    treasure = get_object_or_404(mymodel, pk=id)

    if request.method == "POST":
        form = myform(request.POST, request.FILES, instance=treasure)
        if form.is_valid():
            form.save()

            return redirect( 'myapp:detail', id=treasure.pk)

    else:
        form = myform(instance=treasure)

        return render(request,'myapp/update.html', {'form': form})




def delete(request,id):
    obj = get_object_or_404(mymodel, id=id)
    if request.method == "POST":

        obj.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html')


def login_req(request):

    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
        return render(request,'registration/login.html',{'form':form})



def sign_up1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def logout1(request):
    logout(request)
    return redirect('/')