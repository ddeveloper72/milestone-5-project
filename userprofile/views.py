from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserProfileForm
from accounts.forms import UserNameForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
# Create your views here.

@login_required
def user_profile(request):
    """Private profile edit page - requires login"""
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


def public_profile(request, username):
    """Public profile view - GDPR compliant, shows only non-sensitive data"""
    user = get_object_or_404(User, username=username)
    profile = user.profile
    
    return render(request, 'public_profile.html', {
        'profile_user': user,
        'profile': profile,
    })
