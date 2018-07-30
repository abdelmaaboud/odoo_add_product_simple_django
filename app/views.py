# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from app.form import ProductForm
from app.myapi import OdooAPI

url,db,username,password="http://0.0.0.0:8069","test","admin","admin"
api=OdooAPI(url,db,username,password)


def index(request):
    data=api.search_read('ir.module.module',[['state','=','installed']],['name'])
    context={'data':data}
    return render(request,'index.html',context)



def products(request):
    data=api.search_read('product.template',[],['name','barcode'])
    context={'data':data}
    return render(request,'products.html',context)



def add(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        api.create('product.template',{'name': form.cleaned_data['name'],'barcode':form.cleaned_data['barcode']})
        return redirect('/products')
    context={'form':form}
    return render(request,'add.html',context)
