from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse
#from django.http import HttpResponse

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
    LOW=Webpage.objects.order_by('name')   
     #------------retrive--with--lookups-----------
    LOW=Webpage.objects.filter(name__startswith='N')
    LOW=Webpage.objects.filter(name__startswith='D')
    LOW=Webpage.objects.filter(name__contains='h')
    LOW=Webpage.objects.filter(name__contains='r')
    LOW=Webpage.objects.filter(name__in=('Nare','Lohit'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{6}')
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='Rohit'))
    LOW=Webpage.objects.filter(Q(topic_name='Football') & Q(name='Nare'))
    LOW=Webpage.objects.filter(Q(topic_name='Kabbadi') & Q(name='Dinesh'))
    LOW=Webpage.objects.filter(Q(topic_name='Vollyball') & Q(name='Lohit'))
    LOW=Webpage.objects.filter(Q(topic_name='Kabbadi'))
    LOW=Webpage.objects.all()
    Webpage.objects.filter(name='Rohit').update(name='Shasank')
    Webpage.objects.filter(url='https://Rohit.com').update(url='https://Shasank.com')
    

    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)
def display_AcessRecord(request):
    LOA=AcessRecord.objects.all()
    #----------Field--lookups--------------------
    LOA=AcessRecord.objects.filter(date__gt='2000-01-10')
    LOA=AcessRecord.objects.filter(date__gt='2000-02-21')
    LOA=AcessRecord.objects.filter(date__gte='2000-02-21')
    LOA=AcessRecord.objects.filter(date__lt='2002-02-21')
    LOA=AcessRecord.objects.filter(date__month='02')
    LOA=AcessRecord.objects.filter(date__year='2002')
    LOA=AcessRecord.objects.filter(date__day='21')
    LOA=AcessRecord.objects.filter(date__month='02')
    LOA=AcessRecord.objects.all()
    
    d={'AcessRecord':LOA}
    return render(request,'display_AcessRecord.html',context=d)
def display_update(request):
    #OT1=Topic.objects.get_or_create(topic_name='Football')[0]
    #OT1.save()
   # OT2=Webpage.objects.get_or_create(topic_name=OT1,name='Rama',url='https://Shasank.com')[0]
   # OT2.save()
    

    #AcessRecord.objects.update_or_create(author='azeem',defaults={'author':'suri','date':'2021-01-21'})
    AcessRecord.objects.filter(author='suri').delete()
    d={'AcessRecord':AcessRecord.objects.all()}
    return render(request,'display_AcessRecord.html',d)