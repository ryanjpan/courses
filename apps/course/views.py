from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
    "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def addcourse(request):
    if request.method != 'POST':
        return redirect('/')
    Course.objects.create(name=request.POST['name'], description=request.POST['desc'])
    return redirect('/')

def confirm(request, id):
    request.session['idtodelete'] = id
    row = Course.objects.filter(id=id)[0]
    context = {
    'name': row.name,
    'description': row.description
    }
    return render(request, 'course/confirm.html', context)

def delete(request):
    if request.method != 'POST':
        return redirect('/')
    if request.POST['confirm'] == 'yes':
        Course.objects.filter(id=request.session['idtodelete']).delete()
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')
