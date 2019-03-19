from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserloginForm, UserRegistrationForm

# Create your views here.


def index(request):
    """
    return the index.html file
    """   
    return render(request, 'index.html')


@login_required
def auth_index(request):
    """
    Generate the views for the authorized customer if logged in.
    """
    user = User.objects.get(email=request.user.email)
    return render(request, 'index.html', {"profile": user})


@login_required
def logout(request):
    """
    Log the user out, if the user is already logged in.
    """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))


def login(request):
    """
    Return a login page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        """
        security which prevents access to the login page via url bar
        """     

    if request.method == "POST":
        login_form = UserloginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your login is sucessfull!")
                return redirect(reverse('index'))
                """
                security which prevents access to the login page via url bar
                """
            else:
                login_form.add_error(None,
                                    "Your username or password is \
                                    incorrect")

    else:
        login_form = UserloginForm()

    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """
    Render the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index')) 
        """
        redirect a registerd user away from registration to the index
        """

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            """
            add the user data to the User model in the database
            """
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
               auth.login(user=user, request=request)
               messages.success(request, "You have registerd successfully")
               return redirect(reverse('index'))
               """
               redirect the newly registerd user away from registration to 
               the index
               """
                  
        else:
            messages.error(request, registration_form.errors)            
            """
            messages.warning(request, "Plesse check that your passwords
            match and username/email is unique!")
            """        

    registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
