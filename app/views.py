from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_Topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='cricket')
    LOT=Topic.objects.exclude(topic_name='cricket')
    d={'topics':LOT}
    return render(request,'display_Topic.html',context=d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by('topic_name')
    LOW=Webpage.objects.order_by('-topic_name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('topic_name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.exclude(topic_name='Football')
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)
def display_AcessRecord(request):
    LOA=AcessRecord.objects.all()
    LOA=AcessRecord.objects.filter(date__gt='2000-01-10')
    LOA=AcessRecord.objects.filter(date__gt='2000-02-21')
    LOA=AcessRecord.objects.filter(date__gte='2000-02-21')
    LOA=AcessRecord.objects.filter(date__lt='2002-02-21')
    #LOA=AcessRecord.objects.filter(date__lte='2000-02-21')
    d={'AcessRecord':LOA}
    return render(request,'display_AcessRecord.html',context=d)
