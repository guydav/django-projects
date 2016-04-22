from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from models import ProjectProposal


def index(request):
    return render(request, 'index.html')


def proposals(request):
    projects = ProjectProposal.objects.all()
    return render(request, 'proposals.html', {'projects': projects,})


def support(request, user_id, proposal_id):
    user = User.objects.get(pk=user_id)
    proposal = ProjectProposal.objects.get(pk=proposal_id)

    supporting = proposal.change_user_support(user)

    return JsonResponse({'supporting': supporting, 'multiplier': proposal.multiplier})


def user_is_supporting(request, user_id, proposal_id):
    user = User.objects.get(pk=user_id)
    proposal = ProjectProposal.objects.get(pk=proposal_id)

    return JsonResponse({'supporting': proposal in user.projects_supported.all(), })


def user_can_support(request, user_id, proposal_id):
    user = User.objects.get(pk=user_id)
    proposal = ProjectProposal.objects.get(pk=proposal_id)

    return JsonResponse({'can_support': user.profile.can_support_project(proposal), })


def get_remaining_budget(request, user_id):
    user = User.objects.get(pk=user_id)
    return JsonResponse({'budget': user.profile.str_remaining_budget()})



def help(request):
    pass


def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        signup_form = UserCreationForm(auto_id='id-signup-%s-input')
        login_form = AuthenticationForm(auto_id='id-login-%s-input')

    return render(request, 'signup_login.html', {'signup_form': signup_form, 'login_form': login_form})