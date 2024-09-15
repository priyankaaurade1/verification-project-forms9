from django.db import models
from django.contrib.auth.models import User
from depository.models import Depository
# Create your models here.

## User role's:
# start's here
class UserTypeRole(models.Model):
    role = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.role}' 

class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserTypeRole,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 
# end's here    

## Catch All Errors:
# start's here:
class ErrorsModel(models.Model):
    error_caught_function = models.CharField(max_length=40,default="")
    error_message = models.CharField(max_length=100,default="")
    error_caught_user = models.CharField(max_length=40,default="")
    error_caught_date= models.DateTimeField(max_length=10,auto_now=True)
    def __str__(self):
        return f'{self.error_caught_function} - {self.error_caught_user} - {self.error_caught_date}'
#end's here

## Depository Field select
# start's here

class InvestorIdentityDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
class InvestorAddressDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
class InvestorBankDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
class InvestorAdditionalKycDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
class InvestorNomineeDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
class InvestorGaurdianDetails(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'

class InvestorDeclarationField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'

class InvestorAccountTypeField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'

class InvestorStandingInstructionsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'

class InvestorSmsAlertField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'

class InvestorOtherDetailsField(models.Model):
    field = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.field}'
    
# end's here
# adhar pan card ,nationality 
class InvestorSelectDocument(models.Model):
    document = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.document}'
    
class InvestorDocumentManager(models.Model):
    nationality = models.CharField(max_length=60)
    documents = models.ManyToManyField(InvestorSelectDocument)
    def __str__(self):
        return f'{self.nationality} '

# marital status 
class InvestorMaritalManager(models.Model):
    marital = models.CharField(max_length=20,blank=True)
    documentss = models.ManyToManyField(InvestorSelectDocument)
    def __str__(self):
        return f'{self.marital} '

## Depository field select with all dependent models
# start's here

class ChooseInvestorFields(models.Model):
    depository = models.ForeignKey(Depository, on_delete=models.SET_NULL, null=True, blank=True)
    investorIdentityDetailsFields = models.ManyToManyField(InvestorIdentityDetailsField)
    investorAddressDetailsFields = models.ManyToManyField(InvestorAddressDetailsField)
    investorBankDetailsFields = models.ManyToManyField(InvestorBankDetailsField)
    investorAdditionalKycDetailsFields = models.ManyToManyField(InvestorAdditionalKycDetailsField)
    investorNomineeDetailsFields = models.ManyToManyField(InvestorNomineeDetailsField)
    investorAccountTypeFields = models.ManyToManyField(InvestorAccountTypeField)
    investorGaurdianDetailsFields = models.ManyToManyField(InvestorGaurdianDetails)
    investorDeclarationFields = models.ManyToManyField(InvestorDeclarationField)
    investorStandingInstructionsFields = models.ManyToManyField(InvestorStandingInstructionsField)
    investorSmsAlertFields = models.ManyToManyField(InvestorSmsAlertField)
    investorOtherDetailsFields = models.ManyToManyField(InvestorOtherDetailsField)
    investorDocumentManagerFields = models.ManyToManyField(InvestorDocumentManager)
    investorMaritalManagerFields = models.ManyToManyField(InvestorMaritalManager)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.depository}'
    
# end's here