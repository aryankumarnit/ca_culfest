from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import ProfileForm, UserForm, DocumentForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .models import Profile, Document
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
import re
# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required
@transaction.atomic
def base(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':

        document = Document()
        document.user = request.user
        form = DocumentForm(data=request.POST, files=request.FILES, instance=document)

        if form.is_valid():
            form.save()
            data = {
                'result': 'success',
                'message': 'Image uploaded successfully!!',
            }
            return JsonResponse(data)

        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():

            try:
                grad = int(profile_form.cleaned_data['year_of_grad'])
                if grad < 2018:
                    data = {
                        'result': 'error',
                        'message': 'Invalid details..Please correct the error below!!<br/>Enter correct/valid yead of graduation!!',
                    }
                    return JsonResponse(data)
            except Exception:
                data = {
                    'result': 'error',
                    'message': 'Invalid details..Please correct the error below!!<br/>Enter correct/valid year of graduation!!',
                }
                return JsonResponse(data)

            phone = profile_form.cleaned_data['phone']
            rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
            if not rule.search(phone):
                data = {
                    'result': 'error',
                    'message': 'Invalid details..Please correct the error below!!<br/>Enter a valid phone number!!',
                }
                return JsonResponse(data)

            user_form.save()
            profile_form.save()
            # print(profile_form.cleaned_data['address'])
            # messages.success(request, _('Your profile was successfully updated!'))
            data = {
                'result': 'success',
                'message': 'Your profile is updated successfully !!',
            }
        else:
            # messages.error(request, _('Please correct the error below.'))
            data = {
                'result': 'error',
                'message': 'Invalid details..Please correct the error below!!<br/>All fields are required !!<br/> Enter valid emails if not valid!!',
            }
        return JsonResponse(data)
    else:
        if request.user.profile.address == "":
            return redirect("http://localhost:8000/register")
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        form = DocumentForm()
    return render(request, 'base.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'form': form,
    })


@login_required
@transaction.atomic
def update_profile(request):

    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile(user=request.user)
        print("yes")

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            flag = False
            if user_form.is_valid() and profile_form.is_valid():

                try:
                    grad = int(profile_form.cleaned_data['year_of_grad'])
                    if grad < 2018:
                        messages.error(request, _('Please correct the error below!! Enter correct/valid yead of graduation!!'))
                        flag = True
                except Exception:
                    messages.error(request, _('Please correct the error below!! Enter correct/valid yead of graduation!!'))
                    flag = True

                phone = profile_form.cleaned_data['phone']
                rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
                if not rule.search(phone):
                    messages.error(request, _('Please correct the error below!! Enter a valid phone number!!'))
                    flag = True

            if flag:
                return render(request, 'register.html', {
                    'user_form': user_form,
                    'profile_form': profile_form
                })

            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect("home:base")
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        if request.user.profile.address != "":
            return redirect("home:base")
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render(request, 'index.html')
