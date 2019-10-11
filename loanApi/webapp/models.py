# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

from django.db.models import Count

## implement clasd here



class RequestHeader(models.Model):
    CFRequestId=models.TextField()
    RequestDate=models.DateTimeField()
    CFApiUserId=models.TextField()
    CFApiPassword=models.TextField()
    IsTestLead=models.BooleanField()
    #status=models.TextField()
 
    def __str__(self):
            return self.CFRequestId



class Business (models.Model ):
    RequestHeader=models.ForeignKey(RequestHeader, models.CASCADE,related_name="RequestHeader")
    
    Name=models.TextField()
    TaxID=models.TextField()
    Phone=models.TextField()
    NAICS=models.TextField()
    HasBeenProfitable=models.BooleanField()
    HasBankruptedInLast7Years=models.BooleanField()
    InceptionDate=models.DateTimeField()
    
    def __str__(self):
        return self.Name

class Owners (models.Model):
    Business=models.ForeignKey(Business, related_name="Owners")
    Name=models.TextField()
    FirstName=models.TextField()
    LastName=models.TextField()
    Email=models.EmailField()
    HomeAddress=models.TextField()
    DateOfBirth=models.TextField()
    HomePhone=models.TextField()
    SSN=models.TextField()
    PercentageOfOwnership=models.FloatField()
    def __str__(self):
        return self.Name

class Address(models.Model):
    Business=models.ForeignKey(Business,related_name="Address")
    Owners=models.ForeignKey(Owners, related_name="Address")
    Address1=models.TextField()
    Address2=models.TextField()
    City=models.TextField()
    State=models.TextField()
    Zip=models.TextField()

class CFApplicationData(models.Model):
    RequestHeader=models.ForeignKey(RequestHeader, models.CASCADE,related_name="CFApplicationData")
   # Business=models.ForeignKey(Business,related_name="CFApplicationData2")
    RequestedLoanAmount=models.FloatField()
    StatedCreditHistory=models.TextField()
    LegalEntityType=models.TextField()
    FilterID=models.TextField()



class SelfReportedCashFlow(models.Model):
    Business=models.ForeignKey(Business,related_name="SelfReportedCashFlow")
    AnnualRevenue=models.FloatField()
    MonthlyAverageBankBalance=models.FloatField()
    MonthlyAverageCreditCardVolume=models.FloatField()


class AppStatus(models.Model):
     RequestHeader=models.ForeignKey(RequestHeader, related_name="AppStatus")
     status=models.TextField()
     updateDate=models.DateTimeField()
