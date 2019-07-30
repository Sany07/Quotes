from django.shortcuts import render
from .models import Quotes

def Home(request):
    data=Quotes.objects.all()
    context = {

        'data_list':data
    }
    return render(request,"index.html",context)
