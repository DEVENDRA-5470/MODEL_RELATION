from MySQLdb import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':

        if 'login' in request.POST:
            username = request.POST['username']
            print(username)
            password2 = request.POST['password2']
            print(password2)
            user = authenticate(request, username=username, password=password2)
            print(user,"====================================")
            if user is not None:
                print(user)
                login(request, user)
                return redirect('change_profile')
            else:
                return render(request,'sign_up.html', {'error':'Invalid username or password'})
    

        if 'signup' in request.POST:
        # Get the user information from the form
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
        # Check that both passwords match
            if password1 != password2:
                return render(request, 'sign_up.html', {'error':"Passwords do not match."})
            else:
                try:
                    User.objects.create_user(username=username,password=password1)
                # login
                    user = authenticate(username=username, password=password1)
                    login(request,user)
                    return redirect('change_profile')
                except IntegrityError as e:
                    return render(request, 'sign_up.html',{'error':'Username already exists.'})
                
    return render(request, 'sign_up.html')

def profile(request):
    data=Profile.objects.filter(user=request.user)
    print(data,"--------------------------------")
    context = {'data':data}
    return render(request, 'profile.html', context)


def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect("/profile/")
        else:
            messages.error(request, 'There was an error updating your profile. Please check the form.')

    form = ProfileForm()
    context = {'form': form}
    return render(request, 'change_profile.html', context)

def user_logout(request):
    logout(request)
    return redirect("/")
    


