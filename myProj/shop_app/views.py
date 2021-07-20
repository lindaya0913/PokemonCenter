# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .models import RegisteredUser
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

def app_homepage(request):
    try:
        if username:
            userdetails = {'username': username}
            return render(request, 'loggedin.html', userdetails)
    except NameError:
        return render(request, 'homepage.html')

def about_us(request):
    try:
        if username:
            return render(request, 'aboutus.html')
    except NameError:
        return render(request, 'aboutus.html')

def services(request):
    try:
        if username:
            return render(request, 'services.html')
    except NameError:
        return render(request, 'services.html')

def contact_us(request):
    try:
        if username:
            return render(request, 'contactus.html')
    except NameError:
        return render(request, 'contactus.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else: 
        #GET
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, 'register.html', user_info)

def signin(request):
    global username
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']

        try:
            user = RegisteredUser.objects.get(name = username)
            if username == user.name and password == user.password:
                return redirect('loggedin')
            else:
                messages.info(request, 'Incorrect password!')
                return redirect('signin')
        except ObjectDoesNotExist:
            messages.info(request, 'The user does not exist!')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def loggedin(request):
    userdetails = {'username': username}
    return render(request, 'loggedin.html', userdetails)

def logout(request):
    global username
    del username
    return render(request, 'logout.html')

class UserListView(ListView):
    model = RegisteredUser
    template_name = 'user_data.html'
    context_object_name = 'alldata'

class UserDetailView(DetailView):
    model = RegisteredUser

class UserCreateView(CreateView):
    model = RegisteredUser
    form_class = RegisterForm

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = RegisteredUser
    form_class = RegisterForm

    # only admin can update
    def test_func(self):
        if self.request.user.is_active:
            return True
        else:
            return False

class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = RegisteredUser
    success_url = '/userlist'

    # only admin can update
    def test_func(self):
        if self.request.user.is_active:
            print(self.request.user)
            return True
        else:
            return False