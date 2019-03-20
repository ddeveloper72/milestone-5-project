from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user,
                                            'form': form})
