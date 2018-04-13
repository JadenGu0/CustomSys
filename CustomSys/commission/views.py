# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from custom.models import Custom, Lot
from commission.models import Commission
import csv

# Create your views here.
IB_COMMISSION = 6
MIB_COMMISSION = 9
PIB_COMMISSION = 11
FIRSR_COMMISSION = 3
SECOND_COMMISSION = 2


def new(request):
    return render_to_response('commission/new.html')


def calculate(request):
    if request.method == 'POST':
        time = request.POST['time']
        year = time.split('-')[0]
        month = time.split('-')[1]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="commission.csv"'
        writer = csv.writer(response)
        writer.writerow(['name', 'type', 'year', 'month', 'commnission'])
        custom = Custom.objects.filter(type=1)
        ib = Custom.objects.filter(type=2)
        mib = Custom.objects.filter(type=3)
        pib = Custom.objects.filter(type=4)
        for item in ib:
            mount = get_commission_ib(item, year, month, IB_COMMISSION)
            writer.writerow([item.name, item.get_type_display(), year, month, mount])
        for item in mib:
            mount = get_commission_mib(item, year, month)
            writer.writerow([item.name, item.get_type_display(), year, month, mount])
        for item in pib:
            mount = get_commission_pib(item, year, month)
            writer.writerow([item.name, item.get_type_display(), year, month, mount])
        return response


def get_commission_custom(custom, year, month, commission):
    mount = 0.0
    lot = 0.0
    for count in custom.lot_set.filter(start_time__month=int(month)).filter(start_time__year=int(year)):
        lot = lot + count.lot
    mount = lot * commission
    return mount


def get_commission_ib(ib, year, month, commission):
    mount = 0.0
    lot = 0.0
    all_child = Custom.objects.filter(upper=ib)
    for i in all_child:
        for count in i.lot_set.filter(start_time__month=int(month)).filter(start_time__year=int(year)):
            lot = lot + count.lot
    mount = lot * commission

    return mount


def get_commission_second(upper, year, month, commission):
    mount = 0.0
    child = Custom.objects.filter(upper=upper)
    for item in child:
        mount = mount + get_commission_ib(item, year, month, FIRSR_COMMISSION)
    return mount


def get_commission_third(upper, year, month):
    mount = 0.0
    # 这个mib的下属是ib
    child_ib = Custom.objects.filter(upper=upper).filter(type=2)
    # 这个mib的下属是客户
    child_c = Custom.objects.filter(upper=upper).filter(type=1)
    # 这个mib的所有下属
    child_all = Custom.objects.filter(upper=upper)
    for item in child_all:
        mount = mount + get_commission_ib(item, year, month, FIRSR_COMMISSION)
    for item in child_ib:
        mount = mount + get_commission_ib(item, year, mount, SECOND_COMMISSION)

    return mount


def get_commission_mib(mib, year, month):
    mount = 0.0
    childs = Custom.objects.filter(upper=mib)
    for child in childs:
        # xiashu shi kehu
        if child.type == 1:
            mount = mount + get_commission_custom(child, year, month, IB_COMMISSION)
            # xiashu shi ib
        if child.type == 2:
            mount = mount + get_commission_custom(child, year, month, MIB_COMMISSION)
            mount = mount + get_commission_ib(child, year, month, FIRSR_COMMISSION)
    return mount


def get_commission_pib(pib, year, month):
    mount = 0.0
    childs = Custom.objects.filter(upper=pib)
    for child in childs:
        if child.type == 1:
            print "in custom before"
            print get_commission_custom(child, year, month, IB_COMMISSION)
            # pib的下属是客户，6美金
            mount = mount + get_commission_custom(child, year, month, IB_COMMISSION)
        elif child.type == 2:
            # pib的下属是ib，9美金
            print "in ib before"
            print mount
            mount = mount + get_commission_custom(child, year, month, MIB_COMMISSION)
            # pib下属的ib下属的客户，3美金
            mount = mount + get_commission_ib(child, year, month, FIRSR_COMMISSION)
            print "in ib after"
            print mount
        elif child.type == 3:
            #print "in mib before"
            #print mount
            # pib的下属是mib，11美金
            mount = mount + get_commission_custom(child, year, month, PIB_COMMISSION)
            # pib下属的mib的所有下属
            for ib in Custom.objects.filter(upper=child).filter(type=2):
                mount = mount + get_commission_ib(ib, year, month, SECOND_COMMISSION)
           # print "in mib after"
            #print mount
    return mount
