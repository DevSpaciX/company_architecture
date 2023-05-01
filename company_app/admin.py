from django.contrib import admin

from company_app.models import Employee, User

# Register your models here.
admin.site.register(Employee)
admin.site.register(User)