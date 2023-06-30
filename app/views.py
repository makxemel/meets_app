from django.views.generic import CreateView
from .forms import RegisterClientForm


class RegisterClient(CreateView):
    form_class = RegisterClientForm
    template_name = 'register.html'
    # success_url = '/'