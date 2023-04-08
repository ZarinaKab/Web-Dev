import json, re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Company, Vacancy

# Create your views here.


#works
@csrf_exempt
def companies(request):
    if request.method == 'GET':
        comp = Company.objects.all()
        return JsonResponse([i.to_json() for i in comp], safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        comp_name = data.get('name', '')
        comp_description = data.get('description', '')
        comp_city = data.get('city', '')
        comp_address = data.get('address', '')
        company = Company.objects.create(name = comp_name, description=comp_description, city=comp_city, address=comp_address)
        return JsonResponse(company.to_json())


#works
@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vac = Vacancy.objects.all()
        data = []
        for v in vac:
            data.append({
                'name': v.name,
                'description': v.description,
                'salary': v.salary,
                'company_id': v.company_id
            })
        return JsonResponse(json.dumps(data, ensure_ascii=False), safe=False)


    elif request.method == 'POST':
        data = json.loads(request.body)
        vac_name = data.get('name', '')
        vac_description = data.get('description', '')
        vac_salary = data.get('salary', '')
        vac_company = data.get('company', '')
        vacancy = Vacancy.objects.create(name=vac_name, description=vac_description, salary=vac_salary, company_id=vac_company)

        # создаем словарь для представления только что созданной вакансии в JSON-формате
        vacancy_data = {
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company_id': vacancy.company_id
        }
        # возвращаем JSON-объект
        return JsonResponse(json.dumps(vacancy_data), safe=False)


# works
@csrf_exempt
def companyById(request, id):
    try:
        comp = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(comp.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        # name
        new_company_name = data.get('name', comp.name)
        comp.name = new_company_name

        # description
        disc = data.get('description', comp.description)
        comp.description = disc

        # city
        city = data.get('city', comp.city)
        comp.city = city

        # address
        address = data.get('address', comp.address)
        comp.address = address

        comp.save()
        return JsonResponse(comp.to_json())


    elif request.method == 'DELETE':
        comp.delete()
        return JsonResponse({'deleted': True})



#works without put
@csrf_exempt
def VacancyById(request, id):
    try:
        vac = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        data = {
            'name': vac.name,
            'description': vac.description,
            'salary': vac.salary,
            'company_name': vac.company.name,
            'company_id': vac.company_id
        }
        return JsonResponse(data, safe=False)


    # elif request.method == 'PUT':
    #     data = json.loads(request.body)
    #     new_name = ''
    #     disc = ''
    #     salary = ''
    #     company_id = ''
    #
    #     # name
    #     new_name = data.get('name', vac.name)
    #     if new_name != '':
    #         vac.name = new_name
    #
    #     # description
    #     disc = data.get('description', vac.description)
    #     if disc != '':
    #         vac.description = disc
    #
    #     # salary
    #     salary = data.get('salary', vac.salary)
    #     if salary != '':
    #         vac.salary = salary
    #
    #     # company
    #     company_id = data.get('company_id', vac.company_id)
    #
    #     if company_id != '':
    #         try:
    #             company = Company.objects.get(id=company_id)
    #         except Company.DoesNotExist as e:
    #             return JsonResponse({'error': str(e)}, status=400)
    #         vac.company = company
    #
    #     vac.save()
    #
    #     data = {
    #         'name': vac.name,
    #         'description': vac.description,
    #         'salary': vac.salary,
    #         'company_id': vac.company.id,
    #     }
    #     return JsonResponse(data)



    elif request.method == 'DELETE':
        vac.delete()
        return JsonResponse({'deleted': True})

#works
@csrf_exempt
def CompanyVacancies(request, id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, status=400)

        vacancies = company.vacancy_set.all()
        data = []
        for vacancy in vacancies:
            data.append({
                'company_name': company.name,
                'name': vacancy.name,
                'description': vacancy.description,
                'salary': vacancy.salary,
                'company_id': company.id
            })
        return JsonResponse(data, safe=False)



#works
@csrf_exempt
def TopTen(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')
        data = []
        for vacancy in vacancies:
            data.append({
                'name': vacancy.name,
                'company': vacancy.company.name,
                'description': vacancy.description,
                'salary': vacancy.salary,
            })
        return JsonResponse(data, safe=False)
        # return JsonResponse([i.to_json() for i in vac], safe=False)
