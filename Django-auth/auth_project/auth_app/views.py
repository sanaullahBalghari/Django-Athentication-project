
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# Registration view
def register_view(request):
    if request.method == 'POST':  # POST request for form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in automatically
            return redirect('login')  # Redirect the user to the login page after registration
    else:
        initial_data = {'username': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)  # Show an empty form for GET requests

    return render(request, 'auth/register.html', {'form': form})  # Render the form in both cases

# Login view
def login_view(request):
    if request.method == 'POST':  # POST request for login
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log in the user
            return redirect('/dashboard/')  # Redirect to the dashboard after successful login
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)  # Show an empty form for GET requests

    return render(request, 'auth/login.html', {'form': form})  # Render the form in both cases





@login_required(login_url="/login/")
def dashboard_view(request):
    return render(request,'dashboard.html')
def logout_view(request):
    logout(request)
    return redirect('login')