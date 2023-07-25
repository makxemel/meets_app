import django_filters
from .models import User
from django import forms


class UsersFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        label='First Name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = django_filters.CharFilter(
        label='Last Name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    gender = django_filters.ChoiceFilter(choices=User.genders)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']
