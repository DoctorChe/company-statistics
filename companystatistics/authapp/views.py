from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView

from statapp.models import Department
from .forms import UserLoginForm, UserEditForm, UserProfileEditForm
# from .forms import DepartmentEnrollForm


def user_login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            # next = request.POST['next'] if 'next' in request.POST.keys() else ''
            if user:
                login(request, user)
                if 'next' in request.POST.keys():
                    # if 'next' in request.POST.keys() and request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('department_list'))
                    # return HttpResponseRedirect(reverse('authapp:user_department_list'))
    else:
        login_form = UserLoginForm()

    context = {
        'page_title': 'login',
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def user_logout(request):
    logout(request)
    context = {
        'page_title': 'logged out',
    }
    return render(request, 'authapp/logged_out.html', context)


@login_required
@transaction.atomic
def user_edit(request):
    title = 'edit'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(
            instance=request.user.userprofile
        )

    content = {
        'page_title': title,
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', content)


@login_required
def user_profile(request):
    title = 'profile'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(
            instance=request.user.userprofile
        )

    content = {
        'page_title': title,
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/profile.html', content)


# class UserEnrollDepartmentView(LoginRequiredMixin, FormView):
#     department = None
#     form_class = DepartmentEnrollForm
#
#     def form_valid(self, form):
#         self.department = form.cleaned_data['department']
#         self.department.users.add(self.request.user)
#         return super(UserEnrollDepartmentView,
#                      self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('authapp:user_department_detail',
#                             args=[self.department.id])
#
#
# class UserDepartmentListView(LoginRequiredMixin, ListView):
#     model = Department
#     template_name = 'authapp/department/list.html'
#
#     def get_queryset(self):
#         qs = super(UserDepartmentListView, self).get_queryset()
#         return qs.filter(users__in=[self.request.user])
#
#
# class UserDepartmentDetailView(DetailView):
#     model = Department
#     template_name = 'authapp/department/detail.html'
#
#     def get_queryset(self):
#         qs = super(UserDepartmentDetailView, self).get_queryset()
#         return qs.filter(users__in=[self.request.user])
#
#     def get_context_data(self, **kwargs):
#         context = super(UserDepartmentDetailView,
#                         self).get_context_data(**kwargs)
#         # get department object
#         department = self.get_object()
#         if 'card_id' in self.kwargs:
#             # get current card
#             context['card'] = department.cards.get(
#                 id=self.kwargs['card_id'])
#         else:
#             # get first card
#             context['card'] = department.cards.all()[0]
#         return context
