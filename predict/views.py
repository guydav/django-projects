from django.shortcuts import render

from models import ProjectProposal
# Create your views here.


def index(request):
    return render(request, 'index.html')


def proposals(request):
    projects = ProjectProposal.objects.all()
    return render(request, 'proposals.html', {'projects': projects,})
