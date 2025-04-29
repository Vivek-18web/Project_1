from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import vacancy, berojgar, application, hrgroup


# Create your views here.
def main(request):
    return render(request,'maindashbord.html')

def home(request):
     if request.session.get('email') is not None:
         data = vacancy.objects.all()
         return render(request,'index.html',{'data':data})
     else:
         return redirect('/')

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def registercheck(request):
    if request.method == "POST":
        n=request.POST['name']
        e=request.POST['email']
        s=request.POST['skill']
        p=request.POST['password']

        r=berojgar(name=n,email=e,skill=s,password=p)
        r.save()

        return render(request,'login.html')

def logincheck(request):
    if request.method =="POST":
        email=request.POST['email']
        password=request.POST['password']

        check=berojgar.objects.all().filter(email=email,password=password)
        if check:
            request.session['email']=email
            return redirect('/home')
        else:
            return redirect('/')



def out(request):
    del request.session["email"]
    return redirect('/')


def profile(request):
    i = request.GET['email']
    data = berojgar.objects.all().filter(email=i)
    return render(request,'profile.html',{'data':data})


def update(request):
    if request.method =="POST":
        i=request.POST['id']
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['skill']
        p = request.POST['password']

        r = berojgar(id=i,name=n, email=e, skill=s, password=p)
        r.save()

        return redirect("/home")







def apply(request):
    i = request.GET['company']
    data = vacancy.objects.all().filter(company=i)
    return render(request, 'apply.html', {'data': data})


def success(request):
    if request.method =="POST":
        c=request.POST['company']
        n=request.POST['name']
        e= request.POST['email']
        p=request.POST['phone']
        q= request.POST['qualification']
        photo=request.FILES['photo']

        send=application(company=c,name=n,email=e,phone=p,qualification=q,photo=photo)
        send.save()

        return redirect('/home')

def job(request):
    return render(request,'addjob.html')

def addjob(request):
    if request.method =="POST":
        r=request.POST['role']
        c= request.POST['company']
        l= request.POST['location']
        learn = request.POST['learn']
        v = request.POST['vac']

        send=vacancy(role=r,company=c,location=l,learn=learn,vac=v)
        send.save()

        return redirect('/hrdash')


def hrlogin(request):
    return render(request,'hrlogin.html')

def hrregister(request):
    return render(request,'hrregister.html')

def hrregistercheck(request):
    if request.method =="POST":
        hn = request.POST['name']
        he = request.POST['email']
        hc = request.POST['company']
        hp = request.POST['password']


        send = hrgroup(name=hn, email=he,company=hc,password=hp)
        send.save()

        return redirect("/hrlogin")


def hrlogincheck(request):
    if request.method =="POST":
        company=request.POST['company']
        password=request.POST['password']

        check = hrgroup.objects.all().filter(company=company, password=password)
        if check:
            request.session['company']=company
            return redirect('/hrdash')
        else:
            return redirect('/')




def hrdash(request):
    if request.session.get('company') is not None:
        return render(request,'hrdashbord.html')
    else:
        return redirect('/hrlogin')


def hrprofile(request):
    i=request.GET['company']
    data=hrgroup.objects.all().filter(company=i)
    return render(request,'hrprofile.html',{'data':data})

def hrupdate(request):
    if request.method =="POST":
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['company']
        p = request.POST['password']

        hrgroup.objects.filter(company=s).update(name=n, email=e, company=s, password=p)
        return render(request,'hrdashbord.html')




def hrlogout(request):
    del request.session['company']
    return redirect('/home')

def list(request):
    i=request.GET['company']
    data=vacancy.objects.all().filter(company=i)
    return render(request,'list.html',{'data':data})



def applylist(request):
    i = request.GET['company']
    data = application.objects.all().filter(company=i)
    return render(request, 'hrdash.html', {'data': data})

def delete(request):
    i = request.GET['id']
    vacancy.objects.all().filter(id=i).delete()
    return redirect("/job")

def user_applied(request):
    i = request.GET['email']
    data = application.objects.all().filter(email=i)
    return render(request, 'user_applied.html', {'data': data})


def reject(request):
    i=request.GET['id']
    data = application.objects.all().filter(id=i)
    return render(request, 'reject.html', {'data': data})


def reject_process(request):
    if request.method == "POST":
        i=request.POST['id']
        c=request.POST['company']
        n = request.POST['name']
        e = request.POST['email']
        q = request.POST['qualification']
        r = request.POST['apply']

        send = application.objects.filter(id=i).update(id=i,company=c,name=n, email=e, qualification=q, apply=r)


        return redirect('/hrdash')




