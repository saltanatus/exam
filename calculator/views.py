from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Category, Resource


def category_view(request):
    category = Category.objects.all()
    return render(request, 'main.html', {'category': category})

def resource_view(request):
    resource = Resource.objects.all()
    return render(request, 'resource.html', {'resource': resource})

def delete_view(request, id):
    delete_resource = Resource.objects.get(id=id)
    delete_resource.delete()
    return HttpResponse('Запись удалена.')


def create_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'resource_create.html', {'category': category})

    if request.method == 'POST':
        label = request.POST.get('label')
        last_number = request.POST.get('last_number')
        initial_cost = request.POST.get('initial_cost')
        residual_cost = request.POST.get('residual_cost')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        new_resource = Resource(
            label=label, 
            last_number=last_number,  
            initial_cost=initial_cost, 
            category=category,
            residual_cost=residual_cost
        )
        new_resource.save()

        return redirect(reverse('resource'))


def update_view(request,id):
    single_resource = Resource.objects.get(id=id)
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'resource_create.html', {'category': category})

    if request.method == 'POST':
        label = request.POST.get('label')
        last_number = request.POST.get('last_number')
        initial_cost = request.POST.get('initial_cost')
        residual_cost = request.POST.get('residual_cost')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        single_resource.label = label
        single_resource.last_number = last_number
        single_resource.initial_cost = initial_cost
        single_resource.residual_cost = residual_cost
        single_resource.category = category
        single_resource.save()

        return redirect(reverse('resource'))


