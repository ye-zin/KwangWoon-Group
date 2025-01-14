from django.shortcuts import render
from .models import MainCotent

def index(request):
    content_list = MainCotent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(request, 'product/content_list.html', context)