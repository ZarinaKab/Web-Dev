from django.urls import path

from . import views

urlpatterns = [
    path('companies', views.companies),
    path('companies/<int:id>/', views.companyById),
    path('companies/<int:id>/vacancies/', views.CompanyVacancies),
    path('vacancies/', views.vacancies),
    path('vacancies/<int:id>/', views.VacancyById),
    path('vacancies/top_ten/', views.TopTen)
]