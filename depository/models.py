from django.db import models
from django.contrib.auth.models import User
import random
from investor.models import Document

# Create your models here.
martial_status=(
    ('SINGLE','SINGLE'),
    ('MARRIED','MARRIED'),
    ('WIDOWED', 'WIDOWED'),
    ('DIVORCED', 'DIVORCED'),
    ('SEPARATED', 'SEPARATED'),
    ('OTHER', 'Other'),
)
title=(
    ('MR','MR'),
    ('MRS','MRS'),
    ('MS','MS'),
    ('OTHER','OTHER'),
)
relation=(
    ('MOTHER','MOTHER'),
    ('FATHER','FATHER'),
    ('WIFE','WIFE'),
    ('HUSBAND','HUSBAND'),
    ('SISTER','SISTER'),
    ('BROTHER','BROTHER'),
    ('SON','SON'),
    ('DAUGHTER','DAUGHTER'),
    ('OTHER','OTHER')
)
## Depository model to add/update new depository:
# start's here
class Depository(models.Model):
    def create_new_depository_unique_no():
        not_unique = True
        while not_unique:
            unique_ref = 'FM9DEP'+str(random.randint(111111,999999))
            if not Depository.objects.filter(depository_number=unique_ref):
                not_unique = False
        return str(unique_ref)
    depository_number  = models.CharField(max_length=12,blank=True,null=True,default=create_new_depository_unique_no)
    depository_name = models.CharField(max_length=100,blank=True,null=True)
    logo = models.ImageField(upload_to ='depository_logo/',blank=True,null=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    # ... more fields to be added

    def __str__(self):
        return f'{self.depository_name}'

# end's here
## New Application form (Investor):
# start's here:
class RequestDetails(models.Model):
    def create_new_request_unique_no():
        not_unique = True
        while not_unique:
            unique_ref = 'FM9'+str(random.randint(111111,999999))
            if not RequestDetails.objects.filter(requestno=unique_ref):
                not_unique = False
        return str(unique_ref)
    requestno  = models.CharField(max_length=12,blank=True,null=True,default=create_new_request_unique_no)
    investor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    depository = models.ForeignKey(Depository,on_delete=models.SET_NULL,null=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(blank=True,null=True)
    def __str__(self):
        return f'{self.id} - {self.requestno} - {self.investor} - {self.depository}' 
    
# end's here
  
##  Investor Bank Application Form
# start's here 

class InvestorIdentityDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='identity_details')
    applicant_first_name = models.CharField(max_length=50, blank=True, null=True)
    applicant_middle_name = models.CharField(max_length=50, blank=True, null=True)
    applicant_last_name = models.CharField(max_length=50, blank=True, null=True)
    maiden_name = models.CharField(max_length=50, blank=True, null=True)
    father_first_name = models.CharField(max_length=32, blank=True, null=True)
    father_middle_name = models.CharField(max_length=32, blank=True, null=True)
    father_last_name = models.CharField(max_length=32, blank=True, null=True)
    mother_first_name = models.CharField(max_length=32, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=32, blank=True, null=True)
    mother_last_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_last_name = models.CharField(max_length=32, blank=True, null=True)
    residence_address = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    martial_status = models.CharField(max_length=30, blank=True, null=True,choices=martial_status)
    nationality = models.CharField(max_length=64, blank=True, null=True)
    resident_status = models.CharField(max_length=64, blank=True, null=True)
    pan_no = models.CharField(max_length=12, blank=True, null=True)
    aadhar_no = models.CharField(max_length=14, blank=True, null=True)
    def __str__(self):
        return f'{self.request_no}' 
    

class InvestorAddressDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='address_details')
    residence_address = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    tel_no = models.CharField(max_length=12, blank=True, null=True)
    email_id = models.CharField(max_length=60, blank=True, null=True)
    permanent_address = models.CharField(max_length=300, blank=True, null=True)
    permanent_city = models.CharField(max_length=50, blank=True, null=True)
    permanent_district = models.CharField(max_length=50, blank=True, null=True)
    permanent_pincode = models.CharField(max_length=6, blank=True, null=True)
    permanent_state = models.CharField(max_length=60, blank=True, null=True)
    permanent_country = models.CharField(max_length=60, blank=True, null=True)
    addr_checkbox = models.BooleanField(blank=True,null=True)
    def __str__(self):
        return f'{self.request_no}' 
    

class InvestorBankDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='bank_details')
    bank_name = models.CharField(max_length=150, blank=True, null=True)
    branch_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    account_type = models.CharField(max_length=20, blank=True, null=True)
    micr_number = models.CharField(max_length=10, blank=True, null=True)
    account_no = models.CharField(max_length=20, blank=True, null=True)
    ifsc_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.request_no}' 
    
class InvestorAdditionalKycDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='kyc_details')
    dp_reference_number = models.CharField(max_length=50, blank=True, null=True)
    kycdate = models.DateField(blank=True,null=True)
    dp_id = models.CharField(max_length=10, blank=True, null=True)
    client_id = models.CharField(max_length=10, blank=True, null=True)
    first_holder_name = models.CharField(max_length=50, blank=True, null=True)
    second_holder_name = models.CharField(max_length=50, blank=True, null=True)
    third_holder_name = models.CharField(max_length=50, blank=True, null=True)
    first_holder_pancard = models.CharField(max_length=12, blank=True, null=True)
    second_holder_pancard = models.CharField(max_length=12, blank=True, null=True)
    third_holder_pancard = models.CharField(max_length=12, blank=True, null=True)
    declaration_name = models.CharField(max_length=50, blank=True, null=True)
    declaration = models.BooleanField(default=False, blank=True,null=True)
    def __str__(self):
        return f'{self.request_no}' 
    
class InvestorNomineeDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='nominee_details')
    registration_no = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20, choices=title,blank=True, null=True)
    nominee_firstname = models.CharField(max_length=20, blank=True, null=True)
    nominee_middlename = models.CharField(max_length=20, blank=True, null=True)
    nominee_lastname = models.CharField(max_length=20, blank=True, null=True)
    nominee_nickname = models.CharField(max_length=20, blank=True, null=True)
    nominee_address = models.CharField(max_length=20, blank=True, null=True)
    nominee_city = models.CharField(max_length=50, blank=True, null=True)
    nominee_pincode = models.CharField(max_length=6, blank=True, null=True)
    nominee_state = models.CharField(max_length=60, blank=True, null=True)
    nominee_country = models.CharField(max_length=60, blank=True, null=True)
    nominee_mobile_no = models.CharField(max_length=12, blank=True, null=True)
    nominee_aadhar = models.CharField(max_length=20, blank=True, null=True)
    nominee_email = models.CharField(max_length=20, blank=True, null=True)
    nominee_date_of_birth = models.DateField(blank=True,null=True)
    nominee_relationship = models.CharField(max_length=20, blank=True, null=True)
    nominee_declaration_1 = models.BooleanField(default=False, blank=True,null=True)
    nominee_declaration_2 = models.BooleanField(default=False, blank=True,null=True)
    def __str__(self):
        return f'{self.request_no}' 
    

class InvestorGaurdianDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='gaurdian_details')
    gaurdian_name = models.CharField(max_length=100,blank=True,null=True) 
    relationship = models.CharField(max_length=50,choices=relation,blank=True,null=True) 
    pancard = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    fax_no = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.CharField(max_length=60, blank=True, null=True)
    def __str__(self):
        return f'{self.request_no}'
    
# Pending
class InvestorDeclaration(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='declaration_details')
    place = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    def __str__(self):
        return f'{self.request_no}'



# Pending...
class InvestorAccountType(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='account_details')
    status = models.CharField(max_length=50,blank=True,null=True) # want to add choice...
    sub_status = models.CharField(max_length=50,blank=True,null=True) # want to add choice...
    def __str__(self):
        return f'{self.request_no}'


class InvestorStandingInstructions(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='si_details')
    declaration_1 = models.CharField(max_length=50,blank=True,null=True) 
    declaration_2 = models.CharField(max_length=50,blank=True,null=True) 
    account_statement = models.CharField(max_length=50,blank=True,null=True) 
    declaration_3 = models.CharField(max_length=50,blank=True,null=True) 
    declaration_4 = models.CharField(max_length=50,blank=True,null=True) 
    annual_report = models.CharField(max_length=50,blank=True,null=True) 
    declaration_5 = models.CharField(max_length=50,blank=True,null=True) 

    def __str__(self):
        return f'{self.request_no}'


class InvestorSmsAlert(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='sms_details')
    declaration = models.BooleanField(default=False, blank=True,null=True)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True);
    def __str__(self):
        return f'{self.request_no}'
    
class InvestorOtherDetails(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='other_details')
    gross_annual_income_detail = models.CharField(max_length=50,blank=True,null=True) 
    occupation = models.CharField(max_length=50,blank=True,null=True) 
    declaration = models.CharField(max_length=50,blank=True,null=True) 
    other_info = models.CharField(max_length=100,blank=True,null=True) 
    test = models.CharField(max_length=100,blank=True,null=True) 
    def __str__(self):
        return f'{self.request_no}'


class InvestorDocumentUpload(models.Model):
    request_no = models.ForeignKey(RequestDetails,on_delete=models.SET_NULL,blank=True,null=True,related_name='document_details')
    document = models.ManyToManyField(Document)
    def __str__(self):
        return f'{self.request_no}'
# end's here






