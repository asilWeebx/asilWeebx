from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Best, Top, Quality, Course_Regis, Contact, Text_to_Youtube
from django.contrib import messages


def index(request):
    best = Best.objects.all()
    top = Top.objects.all()
    qualite = Quality.objects.all()
    course = Course.objects.all()
    yt = Text_to_Youtube.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        emaila = request.POST.get('emaila')
        message = request.POST.get('message')
        contact = Contact(
            name=name,
            email = emaila,
            message = message
        )
        contact.save()
        messages.success(request, 'Sizning Arizangiz Qabul Qilindi')
        return redirect('index')

    ctx = {
        'best':best,
        'top':top,
        'qualite':qualite,
        'yt':yt,
        'course':course
    }
    return render(request,'index.html',ctx)
