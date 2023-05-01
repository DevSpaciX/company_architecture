"""Company_tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from company_app.views import EmployeeTree, EmployeeListView, EmployeeUpdateView, delete_employee, EmployeeCreateView, \
    LoginView, SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', EmployeeTree.as_view(), name='employee-tree'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee_create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('delete_employee/<int:pk>/', delete_employee, name='employee-delete'),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/sign_up/", SignUpView.as_view(), name="sign-up"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
