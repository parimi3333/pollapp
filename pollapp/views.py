from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def deom(request):
        user = request.user.username
        messages.info(request,user)
        return render(request,'demo.html')


@login_required(login_url='signin')
def createform(request):
        return render(request,'create.html')


@login_required(login_url='signin')
def createdata(request):
        q = request.POST['q']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        user = request.user.username
        qu = len(poll_question.objects.filter(user=user))
        if qu>5:
            return HttpResponse('max limit 5 only')
        else:
            u = poll_question.objects.create(question=q,option1=o1,option2=o2,option3=o3,option4=o4)
            u.save()
            return HttpResponse('created')


@login_required(login_url='signin')
def resultspage(request):
        data = poll_question.objects.all()
        return render(request,'results.html',{'d':data})


@login_required(login_url='signin')
def results(request):
        uid = request.POST['uid']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        q = request.POST['q']
        q1 = len(poll_answer.objects.filter(Q(id_answer=uid)&Q(answer=o1)))
        q2 =len(poll_answer.objects.filter(Q(id_answer=uid) & Q(answer=o2)))
        q3 = len(poll_answer.objects.filter(Q(id_answer=uid) & Q(answer=o3)))
        q4 = len(poll_answer.objects.filter(Q(id_answer=uid) & Q(answer=o4)))
        data = {'question':q,o1:q1,o2:q2,o3:q3,o4:q4}
        return render(request,'res.html',{'d':data,})



@login_required(login_url='signin')
def poll_vote(request):
        poll_id = request.POST['uid']
        a = request.POST['a']
        q = request.POST['q']
        user = request.user.username
        qu = poll_answer.objects.filter(Q(user=user)&Q(id_answer=poll_id))
        if qu.exists():
            qu.delete()
            data = poll_question.objects.all()
            return render(request, 'polls.html', {'d': data})

        else:
            s = poll_answer.objects.create(id_answer=poll_id,question=q,answer=a,user=user)
            s.save()
            data = poll_question.objects.all()
            return render(request, 'polls.html', {'d': data})


@login_required(login_url='signin')
def polls_now(request):
        data = poll_question.objects.all()
        return render(request,'polls.html',{'d':data})
def singupdata(request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already taken')
            return render(request,'signup.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already used')
            return render(request, 'signup.html')
        else:
            c = User.objects.create_user(username=username, password=password, email=email)
            c.save()
            user_model = User.objects.get(username=username)
            new_profile = usermodel.objects.create(username=user_model, id_user=user_model.id)
            new_profile.save()

            return render(request,'demo.html')
def signupform(request):
        return render(request,'signup.html')
def signinform(request):
        return render(request,'signin.html')
def signindata(request):
        username = request.POST['username']
        password = request.POST['password']
        e = authenticate(username=username,password=password)
        if e is not None:
            u = request.user.username
            messages.info(request,u)
            login(request,e)
            return render(request,'demo.html')
        else:
            messages.info(request,'pease give valid credintials')
            return render(request,'signin.html')


@login_required(login_url='signin')
def logoutdata(request):
        logout(request)
        return render(request,'signin.html')


