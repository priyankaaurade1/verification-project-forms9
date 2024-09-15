from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
employeement_type=(
    ('Business','Business'),
    ('Student', 'Student'),
    ('Unemployed', 'Unemployed'),
    ('Private Sector Service','Private Sector Service'),
    ('Public Sector','Public Sector'),
    ('Retired','Retired'),
    ('Govt Service','Govt Service'),
    ('Professional','Professional'),
    ('Agricultural','Agricultural'),
    ('Housewife','Housewife'),
    ('Forex Dealer','Forex Dealer'),
    ('Others','Others'),
)
martial_status=(
    ('SINGLE','SINGLE'),
    ('MARRIED','MARRIED'),
    ('WIDOWED', 'WIDOWED'),
    ('DIVORCED', 'DIVORCED'),
    ('SEPARATED', 'SEPARATED'),
)
nationality=(
    ('INDIAN','INDIAN'),
    ('NRI','NRI'),
    ('FOREIGNER','FOREIGNER')
)
bill_name=(
    ('TELEPHONE_BILL','TELEPHONE_BILL'),
    ('ELECTRIC_BILL','ELECTRIC_BILL'),
    ('UTILITY_BILL','UTILITY_BILL'),
    ('OTHER','OTHER')
)
documents=(
    ('AADHAR CARD SELF','AADHAR CARD SELF'),
    ('AADHAR CARD FATHER','AADHAR CARD FATHER'),
    ('AADHAR CARD MOTHER','AADHAR CARD MOTHER'),
    ('AADHAR CARD SPOUSE','AADHAR CARD SELF'),
    ('PAN CARD SELF','PAN CARD SELF'),
    ('PAN CARD FATHER','PAN CARD FATHER'),
    ('PAN CARD MOTHER','PAN CARD MOTHER'),
    ('PAN CARD SPOUSE','PAN CARD SPOUSE'),
    ('PASSPORT','PASSPORT'),
    ('VISA','VISA'),
    ('OVERSEA TAX','OVERSEA TAX'),
    ('UTILITY BILL','UTILITY BILL'),
    ('BANK PASSBOOK','BANK PASSBOOK'),
    ('BANK STATEMENT','BANK STATEMENT'),
    ('BANK CHEQUE','BANK CHEQUE'),
    ('CREDIT CARD','CREDIT CARD'),
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
request_status=(
    ('PENDING APPROVAL','PENDING APPROVAL'),
    ('ACCEPTED','ACCEPTED'),
    ('REJECTED','REJECTED'),
)
account_type={
    ('SAVING','SAVING'),
    ('CURRENT','CURRENT'),
    ('NRE','NRE'),
    ('NRO','NRO')
}
cc_type={
    ('Master Card','Master Card'),
    ('VISA','VISA'),
    ('Amex','Amex'),
    ('Other','Other')
}
permission=(
    ('Read/Write','Read/Write'),
    ('Read','Read'),
)
gender=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('TRANSGENDER','TRANSGENDER'),
    ('OTHER','OTHER'),
)
title=(
    ('MR','MR'),
    ('MRS','MRS'),
    ('MS','MS'),
    ('OTHER','OTHER'),

)
## Investor Profile Details

#start's here
class InvestorDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    nationality = models.CharField(max_length=64,choices=nationality,blank=True, null=True)
    dob = models.DateField(null=True,blank=True)
    martial_status = models.CharField(max_length=64,choices=martial_status,blank=True, null=True)
    father_first_name = models.CharField(max_length=32, blank=True, null=True)
    father_middle_name = models.CharField(max_length=32, blank=True, null=True)
    father_last_name = models.CharField(max_length=32, blank=True, null=True)
    mother_first_name = models.CharField(max_length=32, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=32, blank=True, null=True)
    mother_last_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=32, blank=True, null=True)
    spouse_last_name = models.CharField(max_length=32, blank=True, null=True)
    flat_no = models.CharField(max_length=50, blank=True, null=True)
    bldg_no = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    mobile_no = models.CharField(max_length=12, blank=True, null=True)
    tel_no = models.CharField(max_length=12, blank=True, null=True)
    email_id = models.CharField(max_length=60, blank=True, null=True)
    alternate_email_id = models.CharField(max_length=60, blank=True, null=True)
    primary_contact = models.CharField(max_length=64, blank=True, null=True)
    secondary_contact = models.CharField(max_length=64, blank=True, null=True)
    employeement = models.CharField(max_length=64,choices=employeement_type,blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    income = models.FloatField(null=True,blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    landmark =  models.CharField(max_length=64, blank=True, null=True)
    gender =  models.CharField(max_length=64,choices=gender,blank=True, null=True)
    def __str__(self):
        return f'{self.user}' 

# end's here    


## Investor Documents

# start's here

# 29-03-23

class DocumentUpload(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now=True)
    #  aadhar card details:
    aadhar_self_no = models.CharField(max_length=15,blank=True, null=True)
    aadhar_father_no = models.CharField(max_length=15,blank=True, null=True)
    aadhar_mother_no = models.CharField(max_length=15,blank=True, null=True)
    aadhar_spouse_no = models.CharField(max_length=15,blank=True, null=True)
    #  pan card details:
    pancard_self_no = models.CharField(max_length=15,blank=True, null=True)
    pancard_father_no = models.CharField(max_length=15,blank=True, null=True)
    pancard_mother_no = models.CharField(max_length=15,blank=True, null=True)
    pancard_spouse_no = models.CharField(max_length=15,blank=True, null=True)
    #  passport details:
    passport_data = models.CharField(max_length=15,blank=True, null=True)
    #  oversea Tax details:
    oversea_tax = models.CharField(max_length=15,blank=True, null=True)
    # visa details:
    visa_no = models.CharField(max_length=150, blank=True, null=True)
    
    # Utility bill:
    bill_name = models.CharField(max_length=64,choices=bill_name,blank=True, null=True)
    bill_date = models.DateField(blank=True,null=True)
    bill_note = models.CharField(max_length=150, blank=True, null=True)    
    bill_number = models.CharField(max_length=20, blank=True, null=True)
    
    # Demat Account
    pp_id = models.CharField(max_length=20, blank=True, null=True)
    client_id_1 = models.CharField(max_length=20, blank=True, null=True)
    client_id_2 = models.CharField(max_length=20, blank=True, null=True)
    client_id_3 = models.CharField(max_length=20, blank=True, null=True)
    client_id_4 = models.CharField(max_length=20, blank=True, null=True)
    broker_name = models.CharField(max_length=20, blank=True, null=True)
   
    def __str__(self):
        return f'{self.user} - {self.date_updated}' 

class InvestorCreditCard(models.Model):
    document_data = models.ForeignKey(InvestorDetail,on_delete=models.CASCADE,blank=True,null=True,related_name='cc_details')
    cc_bank_name = models.CharField(max_length=150, blank=True, null=True)    
    cc_number = models.CharField(max_length=50, blank=True, null=True)    
    cc_limit = models.CharField(max_length=50, blank=True, null=True)
    cc_type = models.CharField(max_length=20,choices=cc_type, blank=True, null=True)
    set_as_primary = models.BooleanField(default=False,)
    def __str__(self):
        return f'{self.document_data.user} - {self.cc_bank_name}'

class InvestorBankDetail(models.Model):
    document_data = models.ForeignKey(InvestorDetail,on_delete=models.CASCADE,blank=True,null=True,related_name='bank_details')
    bank_name = models.CharField(max_length=150, blank=True, null=True)
    branch_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    account_type = models.CharField(max_length=20,choices=account_type, blank=True, null=True)
    micr_number = models.CharField(max_length=10, blank=True, null=True)
    account_no = models.CharField(max_length=25, blank=True, null=True)
    ifsc_number = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True,null=True,auto_now=True)
    pb_entry_from = models.DateField(blank=True,null=True)
    pb_entry_to = models.DateField(blank=True,null=True)
    st_entry_from = models.DateField(blank=True,null=True)
    st_entry_to = models.DateField(blank=True,null=True)
    set_as_primary = models.BooleanField(default=False,)
    def __str__(self):
        return f'{self.document_data.user} - {self.bank_name}'
    
class InvestorNomineeDetail(models.Model):
    document_data = models.ForeignKey(InvestorDetail,on_delete=models.CASCADE,blank=True,null=True,related_name='nominee_details')
    registration_no = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20,choices=title, blank=True, null=True)
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
    nominee_relationship = models.CharField(max_length=20,choices=relation, blank=True, null=True)
    set_as_primary = models.BooleanField(default=False,)
    nominee_declaration_1 = models.BooleanField(default=False, blank=True,null=True)
    nominee_declaration_2 = models.BooleanField(default=False, blank=True,null=True)
    def __str__(self):
        return f'{self.document_data.user} - {self.nominee_firstname}'

class Document(models.Model):
    document_data = models.ForeignKey(DocumentUpload,on_delete=models.CASCADE,blank=True,null=True,related_name='documents')
    image = models.BinaryField(blank=True,null=True) 
    key = models.BinaryField(blank=True,null=True)
    tag = models.BinaryField(blank=True,null=True)
    iv = models.BinaryField(blank=True,null=True)
    document = models.CharField(max_length=64,choices=documents,blank=True, null=True)
    set_as_primary = models.BooleanField(default=False,)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.document_data.user} - {self.document} - {self.date_updated}' 

# Profile Merge/Split
class InvestorProfileMerge(models.Model):
    investor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='investor_merge')
    member = models.ForeignKey(User,on_delete=models.CASCADE,related_name='member_merge')
    relation = models.CharField(max_length=20,choices=relation,blank=True, null=True)
    permission = models.CharField(max_length=20,choices=permission,blank=True, null=True)
    status = models.CharField(max_length=20,choices=request_status,blank=True, null=True)
    date = models.DateField(blank=True,null=True,auto_now_add=True)
    # set_as_primary = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.investor} - {self.member}'
    
