from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.contrib.auth import get_user_model
from .models import (
    Role,
)
User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! '
                                      f'Please contact the admin to assign you a ROLE'
                             )
            return redirect('register')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('CHMS-home')
        else:
            messages.error(request, f'Username or Password is Incorrect!')
    return render(request, 'users/login.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f' {username} Your account has been Updated !')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)


def LogOut(request):
    logout(request)
    return redirect('login')


# Role
class RoleListView(PermissionRequiredMixin, ListView, LoginRequiredMixin):
    model = Role
    template_name = 'users/Role/index.html'
    context_object_name = 'role'
    ordering = ['-createDate']
    extra_context = {'Role': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class RoleCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Role
    form_class = forms.RoleForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    template_name = 'users/Role/create.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class RoleUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Role
    form_class = forms.RoleForm
    extra_context = {'Role': 'Update'}

    def form_valid(self, form):
        return super().form_valid(form)
    template_name = 'users/Role/create.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class RoleDetailView(PermissionRequiredMixin, LoginRequiredMixin,DetailView):
    model = Role
    template_name = 'users/Role/details.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class RoleDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Role
    success_url = '/Role'
    template_name = 'users/Role/delete.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


# Users
class UsersListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/AllUsers/index.html'
    context_object_name = 'allUsers'
    extra_context = {'allUsers': 'active'}

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class UsersUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.AllUsersForm
    extra_context = {'allUsers': 'Update'}

    def form_valid(self, form):
        return super().form_valid(form)
    template_name = 'users/AllUsers/create.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class UsersDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/AllUsers/details.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


class UsersDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/AllUsers'
    template_name = 'users/AllUsers/delete.html'

    def has_permission(self):
        return (
                self.request.user.is_superuser
                or self.request.user.is_superadmin
        )


