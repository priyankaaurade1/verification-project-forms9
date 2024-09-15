from rest_framework import serializers
from depository.models import Depository,RequestDetails,InvestorIdentityDetails,InvestorAddressDetails,InvestorBankDetails,InvestorAdditionalKycDetails,InvestorNomineeDetails,InvestorAccountType,InvestorGaurdianDetails,InvestorDeclaration,InvestorStandingInstructions,InvestorSmsAlert,InvestorOtherDetails,User

## Serializer for request

# start's here 🫡

# -- Identity Details Serializer

class IdentityDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorIdentityDetails
        fields='__all__'

# -- Address Details Serializer

class AddressDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorAddressDetails
        fields='__all__'

# -- Bank Details Serializer

class BankDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorBankDetails
        fields='__all__'

# -- Additional Kyc Details Serializer

class AdditionalKycDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorAdditionalKycDetails
        fields='__all__'

# -- Nominee Details Serializer

class NomineeDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorNomineeDetails
        fields='__all__'

# -- Account Type Serializer

class AccountTypeSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorAccountType
        fields='__all__'

# -- Gaurdian Details Serializer

class GaurdianDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorGaurdianDetails
        fields='__all__'    

# -- DeclarationSerializer

class DeclarationSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorDeclaration
        fields='__all__'  

# .. Standing Instructions Searializer 

class StandingInstructionsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorStandingInstructions
        fields='__all__' 
         
# Investor SmsAlert
class InvestorSmsAlertSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorSmsAlert
        fields='__all__'  

# Investor Other Details
class InvestorOtherDetailsSearializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorOtherDetails
        fields='__all__'  

# RequestDetails -- Main 👇
class RequestDetailsSearializer(serializers.ModelSerializer):
    identityDetailsSearializer = serializers.SerializerMethodField()
    addressDetailsSearializer = serializers.SerializerMethodField()
    bankDetailsSearializer = serializers.SerializerMethodField()
    additionalKycDetailsSearializer = serializers.SerializerMethodField()
    nomineeDetailsSearializer = serializers.SerializerMethodField()
    accountTypeSearializer = serializers.SerializerMethodField() 
    gaurdianDetailsSearializer = serializers.SerializerMethodField() 
    standingInstructionsSearializer = serializers.SerializerMethodField() 
    investorSmsAlertSearializer = serializers.SerializerMethodField() 
    investorOtherDetailsSearializer = serializers.SerializerMethodField() 

    def get_identityDetailsSearializer(self, obj):
        identity_details = InvestorIdentityDetails.objects.filter(request_no=obj).first()
        serializer = IdentityDetailsSearializer(instance=identity_details)
        return serializer.data
    
    def get_addressDetailsSearializer(self, obj):
        address_details = InvestorAddressDetails.objects.filter(request_no=obj).first()
        serializer = AddressDetailsSearializer(instance=address_details)
        return serializer.data
    
    def get_bankDetailsSearializer(self, obj):
        bank_details = InvestorBankDetails.objects.filter(request_no=obj).first()
        serializer = BankDetailsSearializer(instance=bank_details)
        return serializer.data
    
    def get_additionalKycDetailsSearializer(self, obj):
        additionalKyc = InvestorAdditionalKycDetails.objects.filter(request_no=obj).first()
        serializer = AdditionalKycDetailsSearializer(instance=additionalKyc)
        return serializer.data
    
    def get_nomineeDetailsSearializer(self, obj):
        Nominee_details = InvestorNomineeDetails.objects.filter(request_no=obj).first()
        serializer = NomineeDetailsSearializer(instance=Nominee_details)
        return serializer.data
    
    def get_accountTypeSearializer(self, obj):
        accountType_details = InvestorAccountType.objects.filter(request_no=obj).first()
        serializer = AccountTypeSearializer(instance=accountType_details)
        return serializer.data

    def get_gaurdianDetailsSearializer(self, obj):
        gaurdian_details = InvestorGaurdianDetails.objects.filter(request_no=obj).first()
        serializer = GaurdianDetailsSearializer(instance=gaurdian_details)
        return serializer.data

    def get_standingInstructionsSearializer(self, obj):
        standingInstructions_details = InvestorStandingInstructions.objects.filter(request_no=obj).first()
        serializer = StandingInstructionsSearializer(instance=standingInstructions_details)
        return serializer.data
    
    def get_investorSmsAlertSearializer(self, obj):
        SmsAlert_details = InvestorSmsAlert.objects.filter(request_no=obj).first()
        serializer = InvestorSmsAlertSearializer(instance=SmsAlert_details)
        return serializer.data

    def get_investorOtherDetailsSearializer(self, obj):
        Other_details = InvestorOtherDetails.objects.filter(request_no=obj).first()
        serializer = InvestorOtherDetailsSearializer(instance=Other_details)
        return serializer.data
    
    class Meta:
        model = RequestDetails
        fields = '__all__'



#  User Detail Searializer

class UserEmailIdSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username','email'] 