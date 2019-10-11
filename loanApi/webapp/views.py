# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
from django.db.models import Count



class RequestHeader(viewsets.ModelViewSet):
     queryset=RequestHeader.objects.all()
     serializer_class=RequestHeaderSerializer

class BusinessView(viewsets.ModelViewSet):
    queryset=Business.objects.all()
    serializer_class=BusinessSerializer

class DuplicateView(APIView):
  def get(self,Request):
    Taxid=Business.objects.all().values('TaxID').annotate(total=Count('TaxID')).filter(total__gt=1)
    query=Business.objects.filter(TaxID__in=[item['TaxID'] for item in Taxid])
    serializer=BusinessSerializer(query, many=True)
    return Response(serializer.data)



class AddressView(viewsets.ModelViewSet):
     queryset=Address.objects.all()
     serializer_class=AddressSerializer

class SelfReportedCashFlowView(viewsets.ModelViewSet):
     queryset=SelfReportedCashFlow.objects.all()
     serializer_class=SelfReportedCashFlowSerializer

class OwnersFlowView(viewsets.ModelViewSet):
     queryset=Owners.objects.all()
     serializer_class=OwnersSerializer

class CFApplicationFlowView(viewsets.ModelViewSet):
     queryset=CFApplicationData.objects.all()
     serializer_class=CFApplicationDataSerializer

class AppStatusView(viewsets.ModelViewSet):
     queryset=AppStatus.objects.all()
     serializer_class=AppStatusSerializer
     def post(self,request):
         pass
     # def get(self,Request):
    #     re=AppStatus.objects.all()
    #  serializer=RequestHeaderSerializer(re, many=True)#
    #  return Response(serializer.data)
    # def post(self,Request):
#pass
    # def post(self,Request):
#   print Request.POST.get('Status')

