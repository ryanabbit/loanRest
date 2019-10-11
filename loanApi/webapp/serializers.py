from rest_framework import serializers

from .models import *


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = "__all__"

class OwnersSerializer(serializers.ModelSerializer):
    Address = AddressSerializer(many=True, read_only=True)
    class Meta:
        model = Owners
        fields = "__all__"




class SelfReportedCashFlowSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = SelfReportedCashFlow
        fields = "__all__"


class CFApplicationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFApplicationData
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):
     Address = AddressSerializer(many=True, read_only=True)
     Owners=  OwnersSerializer(many=True, read_only=True)
#CFApplicationData=CFApplicationDataSerializer(many=True, read_only=True)
     SelfReportedCashFlow=SelfReportedCashFlowSerializer(many=True, read_only=True)
     class Meta:
        model = Business
        fields = "__all__"

class AppStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStatus
        fields = "__all__"

class RequestHeaderSerializer(serializers.ModelSerializer):
    Business=BusinessSerializer(many=False, read_only=True)
    CFApplicationData=CFApplicationDataSerializer(many=True, read_only=True)
    AppStatus=AppStatusSerializer(many=True, read_only=True)
    class Meta:
        model = RequestHeader
        fields = "__all__"


class DuplicateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Business
        fields = "__all__"
