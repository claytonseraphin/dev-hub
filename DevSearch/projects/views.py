from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm, ReviewForm
from .utils import SearchProjects, paginateProjects
from django.contrib import messages


def projects(request):
    projects, search_query = SearchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projObj = Project.objects.get(id=pk)
    tag = projObj.tags.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = projObj
            review.owner = request.user.profile
            review.save()

            projObj.getVoteCount
            messages.success(request, 'Your review was succesfully submitted!')
            return redirect('project', pk=projObj.id)
    context = {'project': projObj, 'tags': tag, 'form': form}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def CreateProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def UpdateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def DeleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)
# Create your views here.
