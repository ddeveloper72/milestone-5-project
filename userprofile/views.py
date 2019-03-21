from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserProfileForm
from accounts.forms import UserNameForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'POST':
        userbio_form = UserProfileForm(request.POST,
                                       instance=request.user.profile)
        username_form = UserNameForm(request.POST,
                                     instance=request.user)
     
        if userbio_form.is_valid() and username_form.is_valid():
            userbio_form.save()
            username_form.save()
            messages.success(request, _('Your profile was updated successfully!'))
            return redirect(reverse('index'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user = request.user
        userbio_form = UserProfileForm(instance=request.user.profile)
        username_form = UserNameForm(instance=request.user)

    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user,
                                            'userbio_form': userbio_form,
                                            'username_form': username_form})
