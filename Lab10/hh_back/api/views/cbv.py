import json
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, views

from api.serializers import VacancySerializer, CompanySerializer
from api.models import Vacancy, Company
from rest_framework.response import Response


class VacanciesView(GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VacancyView(GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    def get(self, request, id):
        req_com = Vacancy.objects.get(id=id)
        return Response(VacancySerializer(req_com).data)

    def put(self, request, id):
        req_com = Vacancy.objects.get(id=id)
        data = json.loads(request.body)
        req_com.name = data.get('name', req_com.name)
        req_com.description = data.get('description', req_com.description)
        req_com.salary = data.get('salary', req_com.salary)
        req_com.company_id = data.get('company_id', req_com.company_id)
        req_com.save()
        return Response(VacancySerializer(req_com).data)

    def delete(self, request, id):
        req_com = Company.objects.get(id=id)
        temp = req_com
        req_com.delete()
        return Response(CompanySerializer(temp).data)


class VacanciesTop(ListView, views.APIView):

    def get(self, request):
        queryset = Vacancy.objects.all()
        queryset1 = queryset.order_by("-salary")
        return Response(VacancySerializer(queryset1, many=True).data)



class CompaniesView(views.APIView):

    def get(self, request):
        return Response(CompanySerializer(Company.objects.all(), many=True).data)

    def post(self, request):
        data = json.loads(request.body)
        com = Company.objects.create(name=data.get('name', ''),
                                     description=data.get('description', ''),
                                     city=data.get('city', ''),
                                     address=data.get('address', ''))
        return Response(CompanySerializer(com).data)


class CompanyView(views.APIView):
    def get(self, request, id):
        req_com = Company.objects.get(id=id)
        return Response(CompanySerializer(req_com).data)

    def put(self, request, id):
        req_com = Company.objects.get(id=id)
        data = json.loads(request.body)
        req_com.name = data.get('name', req_com.name)
        req_com.description = data.get('description', req_com.description)
        req_com.city = data.get('city', req_com.city)
        req_com.address = data.get('address', req_com.address)
        req_com.save()
        return Response(CompanySerializer(req_com).data)

    def delete(self, request, id):
        req_com = Company.objects.get(id=id)
        temp = req_com
        req_com.delete()
        return Response(CompanySerializer(temp).data)

class CompanyVacanciesView(views.APIView):

    def get(self, request, id):
        return JsonResponse(list(Vacancy.objects.filter(company_id=id).values()), safe=False)
