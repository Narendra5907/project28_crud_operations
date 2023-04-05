from django.shortcuts import render
from app.models import *

# Create your views here.
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',context=d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)
def display_AcessRecord(request):
    LOA=AcessRecord.objects.all()
    d={'AcessRecord':LOA}
    return render(request,'display_AcessRecord.html',context=d)
