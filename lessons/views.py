from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from .models import Lessons
from datetime import date


#from .models import Projects
# Create your views here.


def index(request):
    lessons = Lessons.objects.all()
    published = Lessons.objects.filter(is_published=1)
    previous = Lessons.objects.filter(is_ended=1).order_by("-lesson_date")
    planned = Lessons.objects.filter(is_ended=0).order_by("lesson_date")
    context = {
            "lessons" : lessons,
            "published": published[0],
            "previous": previous,
            "planned" : planned
        }

    return render(request,"index.html",context=context)


def lesson(request,id):
    lesson = get_object_or_404(Lessons,id = id)
    context = {
            "lesson" : lesson,       
        }
    return render(request,"lesson.html",context=context)
