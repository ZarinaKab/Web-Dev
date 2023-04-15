from django.contrib import admin

from .models import Company, Vacancy

# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'salary', 'company')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')


# admin.site.register(Company)
# admin.site.register(Vacancy)