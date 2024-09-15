from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(RequestDetails)
admin.site.register(InvestorIdentityDetails)
admin.site.register(InvestorAddressDetails)
admin.site.register(InvestorBankDetails)
admin.site.register(InvestorNomineeDetails)
admin.site.register(InvestorAdditionalKycDetails)
admin.site.register(InvestorGaurdianDetails)
admin.site.register(InvestorDeclaration)
admin.site.register(InvestorAccountType)
admin.site.register(InvestorStandingInstructions)
admin.site.register(InvestorSmsAlert)
admin.site.register(InvestorOtherDetails)
admin.site.register(Depository)
admin.site.register(InvestorDocumentUpload)
# admin.site.register(ChooseInvestorIdentityDetailsField)