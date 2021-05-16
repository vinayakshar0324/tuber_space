from django.shortcuts import get_object_or_404, render
from .models import Youtuber
# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers

    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_details(request, id):
    tubers = get_object_or_404(Youtuber, pk=id)
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers_details.html', data)


def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()
    camera_search = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__inexact=city)

    if 'camera_type' in request.GET:
        city = request.GET['camera_type']
        if city:
            tubers = tubers.filter(camera_type__inexact=city)

    if 'category' in request.GET:
        city = request.GET['category']
        if city:
            tubers = tubers.filter(category__inexact=city)

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'category_search': category_search,
        'camera_search': camera_search
    }
    return render(request, 'youtubers/search.html', data)
