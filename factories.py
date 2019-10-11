# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.test import TestCase

import factory
from faker import Faker
from models import *

# Create your tests here.


class RequestHeaderFactory(factory.Factory):
    # FACTORY_FOR=RequestHeader
    class Meta:
        model = models.RequestHeader
    CFRequestId=fake.pyint(min_value=0, max_value=100, step=1)
    RequestDate=faker.date_this_decade()
    CFApiUserId=fake.pyint(min_value=0, max_value=100, step=1)
    CFApiPassword=fake.pyint(min_value=0, max_value=100, step=1)
    IsTestLead=True


class BusinseeFactory(factory.Factory):
    #FACTORY_FOR=Businsee
    class Meta:
        model = models.Businsee
    #RequestHeader=factory.SubFactory(RequestHeaderFactory)
    
    Name=fake.company()
    
    TaxID=fake.pyint(min_value=0, max_value=100, step=1)
    Phone=fake.phone_number()
    NAICS=fake.pyint(min_value=0, max_value=100, step=1)
    HasBeenProfitable=True
    HasBankruptedInLast7Years=True
    InceptionDate=faker.date_this_decade()


class OwnersFactory(factory.Factory):
    #FACTORY_FOR=Owners
    class Meta:
        model = models.Owners
    Business=factory.SubFactory(BusinseeFactory)
    
    Name=fake.first_name()
    FirstName=fake.first_name_male()
    LastName=fake.last_name()
    Email=fake.email()
    HomeAddress=fake.address()
    DateOfBirth=fake.date(pattern="%Y-%m-%d", end_datetime=None)
    HomePhone=fake.phone_number()
    SSN=fake.invalid_ssn()
    PercentageOfOwnership=models.FloatField()



class AddressFactory(factory.Factory):
    # FACTORY_FOR=Address
    class Meta:
        model = models.Address
    Business=factory.SubFactory(BusinseeFactory)
    Owners=factory.SubFactory(BusinseeFactory)
    
    Address1=fake.address()
    Address2=''
    City=fake.city()
    State=fake.military_state()
    Zip=fake.zipcode()


class CFApplicationDataFactory(factory.Factory):
    #FACTORY_FOR=CFApplicationData
    class Meta:
        model = models.CFApplicationData
    RequestHeader=factory.SubFactory(RequestHeaderFactory)
    
    RequestedLoanAmount=fake.pyint(min_value=0, max_value=100000, step=1)
    StatedCreditHistory=fake.pyint(min_value=0, max_value=10, step=1)
    LegalEntityType=fake.pyint(min_value=0, max_value=10, step=1)
    FilterID=fake.pyint(min_value=0, max_value=100000, step=1)




class SelfReportedCashFlowFactory(factory.Factory):
    
    #FACTORY_FOR=SelfReportedCashFlow
    class Meta:
        model = models.SelfReportedCashFlow
    Business=factory.SubFactory(BusinseeFactory)
    AnnualRevenue=fake.pyint(min_value=0, max_value=100000, step=1)
    MonthlyAverageBankBalance=fake.pyint(min_value=0, max_value=100000, step=1)
    MonthlyAverageCreditCardVolume=fake.pyint(min_value=0, max_value=100000, step=1)


