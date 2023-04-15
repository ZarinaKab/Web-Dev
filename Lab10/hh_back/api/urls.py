from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #fbv
    #path('companies', views.Companies),
    #path('companies/<int:id_>', views.CompanyById),
    #path('companies/<int:id_>/vacancies', views.CompanyVacancies),
    # path('vacancies', views.Vacancies),
    # path('vacancies/<int:id_>', views.VacancyById),
    #path('vacancies/top_ten', views.VacanciesTop),

    #cbv
    path('companies', views.CompaniesView.as_view()),
    path('companies/<int:id>', views.CompanyView.as_view()),
    path('companies/<int:id>/vacancies', views.CompanyVacanciesView.as_view()),
    path('vacancies', views.VacanciesView.as_view()),
    path('vacancies/<int:id>', views.VacancyView.as_view()),
    path('vacancies/top_ten', views.VacanciesTop.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/token-refresh/', TokenRefreshView.as_view()),
]