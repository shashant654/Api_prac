from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# *************************8AFTER CREATIGN ITEMLISTCREATE FUNCITON  FIRST OF MAKEMIGRATIONS KR LENGE***********

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})