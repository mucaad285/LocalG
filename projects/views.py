from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from .models import Project,ProjectGallery,Comment
from django.db import connection
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html',{'projects':projects})

def about(request):
    return render(request, 'projects/about.html',{})

def contact(request):
    return render(request, 'projects/contact.html',{})

def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects':projects})

def single_project(request,pk):
    pr= ProjectGallery.objects.filter(project=pk)
    projka = Project.objects.filter(id=pk)
    comments = Comment.objects.filter(project=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            prt = get_object_or_404(Project,id=pk)
            comment_txt = request.POST.get('comment_txt')
            name = request.POST.get('name')
            email = request.POST.get('email')
            comm = Comment.objects.create(project = prt ,comment_txt = comment_txt,name=name,email=email)
            comm.save()
            return redirect(projects) 
    else:
        form = CommentForm()
    context = {'projka':projka , 'pr':pr , 'comments':comments,'form': form}
    return render(request, 'projects/single-project.html',context)

def message_from_mayor(request):
    return render(request, 'projects/message_from_mayor.html',{})


