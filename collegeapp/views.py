from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Branches
from .forms import RegistrationForm
from .models import FeedBack
from .models import FeedBackPage

@login_required(login_url='loginpage')
def homePage(request):
    return render(request,'home.html')


@login_required(login_url='loginpage')
def contactPage(request):
    return render(request,'contact.html')


@login_required(login_url='loginpage')
def servicePage(request):
    branches=Branches.objects.all()
    return render(request,'service.html',{'branches':branches})


@login_required(login_url='loginpage')
def feedbackPage(request):
    if request.method == "GET":
        comments=FeedBackPage.objects.all().order_by('-id')
        return render(request,'feedback.html',{'comments':comments})

    else:
        FeedBackPage(
            comment=request.POST['comment'],
            username=request.POST['user'],
            date=request.POST['date']
        ).save()
        comments=FeedBackPage.objects.all().order_by('-id')
        return render(request,'feedback.html',{'comments':comments})
        


@login_required(login_url='loginpage')
def imagesPage(request):
    return render(request,'images.html')



def loginPage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(homePage)
        else:
            return HttpResponse("invalid details,please enter valid username and password.")
    else:
        return render(request,'loginpage.html')


def logoutpage(request):
    logout(request)
    return redirect(loginPage)



def registerpage(request):
    if request.method=="GET":
        form = RegistrationForm()
        return render(request,'registerpage.html',{'form':form})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginPage)
        else:
            return HttpResponse("Please fill the all fields!")

