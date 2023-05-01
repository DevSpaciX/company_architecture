from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from company_app.filters import EmployeeFilter
from company_app.forms import SignUpForm, LoginForm
from company_app.models import Employee

from django.contrib.auth import login, authenticate, get_user_model

from django.core.paginator import Paginator

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View


class EmployeeCRUDMixin:
    model = Employee
    fields = ["name", "position", "hire_date", "email", "parent"]
    success_url = reverse_lazy("employee-list")


class EmployeeCreateView(LoginRequiredMixin, EmployeeCRUDMixin, CreateView):
    template_name = "employee_update.html"


class EmployeeUpdateView(LoginRequiredMixin, EmployeeCRUDMixin, UpdateView):
    template_name = "employee_update.html"


class EmployeeTree(ListView):
    template_name = "employee_tree.html"
    queryset = Employee.objects.all()
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get("page")
        employees = paginator.get_page(page)
        context["employees"] = employees
        return context


class EmployeeListView(ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "employee_list.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = EmployeeFilter(self.request.GET)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get("page")
        employees = paginator.get_page(page)
        context["employees"] = employees
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = EmployeeFilter(self.request.GET, queryset=queryset)
        return filter.qs.distinct()


@login_required
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return JsonResponse({"status": "ok"})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return redirect(reverse("employee-tree"))
        return render(request, "sign_up.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect(reverse("employee-tree"))
            form.add_error(None, "Invalid username or password")
        return render(request, "login.html", {"form": form})
