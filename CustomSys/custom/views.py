from django.shortcuts import render,render_to_response
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from custom.models import Custom,Lot
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
@login_required(login_url='//')

def index(request):
    contacts=[]
    custom=Custom.objects.all()

    for i in custom:
        res=dict()
        res['name']=i.name
        res['account']=i.account
        res['init_money']=i.init_money
        res['create_time']=i.create_time
        res['type']=i.get_type_display()
        if i.upper is not None:
            res['upper']=i.upper.name
        lot_all=0.0
        for index in i.lot_set.all():
            lot_all=lot_all+index.lot
        res['lot']=lot_all
        contacts.append(res)
    page = request.GET.get('page')
    paginator = Paginator(contacts, 25)
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    return render_to_response('custom/list.html',{"contacts":contacts})

def update(request):

    return HttpResponseRedirect("/custom")