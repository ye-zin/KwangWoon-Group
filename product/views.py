from django.shortcuts import render
from .models import MainContent

def index(requset):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(requset, 'product/content_list.html', context)