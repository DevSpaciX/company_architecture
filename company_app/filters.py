import django_filters
from django.forms import TextInput
from django_filters import rest_framework as filters, CharFilter

from company_app.models import Employee


class EmployeeFilter(filters.FilterSet):
    name_filter = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "mt-12 block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 "
                "rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 "
                "dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                "dark:focus:border-blue-500",
                "placeholder": "Search by name",
            }
        ),
    )

    email_filter = filters.CharFilter(
        field_name="email",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "mt-8 block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 "
                "rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 "
                "dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                "dark:focus:border-blue-500",
                "placeholder": "Email by email",
            }
        ),
    )
    position_filter = filters.CharFilter(
        field_name="position",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "mt-8 block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 "
                "rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 "
                "dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 "
                "dark:focus:border-blue-500",
                "placeholder": "Position by position",
            }
        ),
    )

    class Meta:
        model = Employee
        fields = "__all__"
