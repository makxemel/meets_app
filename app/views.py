from django.views.generic import CreateView, ListView
from .forms import RegisterClientForm, LoginUserForm
from .models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .services import like_and_check_match
from django.http import HttpResponseRedirect
from .filters import UsersFilter
from django_filters.views import FilterView


class RegisterClient(CreateView):
    form_class = RegisterClientForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('main_menu')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    # success_url = '/'

    def get_success_url(self):
        return reverse_lazy('main_menu')


def logout_user(request):
    logout(request)
    return redirect('login')


def client_view(request):
    user = User.objects.order_by('?').first()

    return render(request, 'client_detail.html', {'card': user})


def like(request, pk):
    like_and_check_match(request.user.id, pk)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# class UsersList(ListView):
#     model = User
#     template_name = 'user_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)


class UserListView(FilterView):
    model = User
    template_name = 'user_list.html'
    filterset_class = UsersFilter



