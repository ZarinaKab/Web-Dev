
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from .models import Product, Category

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())

def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    # return JsonResponse(products_json, safe=False)
    return render(request, 'products_list.html', {'products':products})

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        raise Http404("Product does not exist")
    return render(request, 'product_detail.html', {'product':product})
    # return JsonResponse(product.to_json())

def categories_list(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    categories_json = [category.to_json() for category in categories]
    # return JsonResponse(categories_json, safe=False)
    return render(request, 'categories_list.html', context)


def category_products(request, id):
    # try:
    #     category = Category.objects.get(id=id)
    # except Category.DoesNotExist as exception:
    #     return Http404("Category does not exist")
    #     # return JsonResponse({'exception': str(exception)}, status=400)
    # # return JsonResponse(category.to_json())
    # return render(request, 'category_details.html', {'category':category})
    try:
        # categories = Category.objects.get(id=id)
        # products = Product.objects.filter(category=categories.name)
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category = category.name)
        context = {
            'category': category,
            'products': products,
        }
    except Category.DoesNotExist as e:
        return Http404("Category is empty")
    return render(request, 'category_products.html', context)



def category_detail(request, id):
    try:
        categories = Category.objects.get(id=id)
        products = Product.objects.filter(category=categories.name)
    except Category.DoesNotExist as e:
        return Http404("Category is empty")
    return render(request, 'category_details.html', {'products':products, 'categories': categories})
    # return JsonResponse([i.to_json() for i in products], safe=False)