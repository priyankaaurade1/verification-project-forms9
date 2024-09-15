from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class CustomUserTypeInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = "UserType"

class CustomizedUserAdmin (UserAdmin):
    inlines = (CustomUserTypeInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(UserTypeRole)
admin.site.register(ChooseInvestorFields)
admin.site.register(InvestorIdentityDetailsField)
admin.site.register(InvestorAddressDetailsField)
admin.site.register(InvestorBankDetailsField)
admin.site.register(InvestorAdditionalKycDetailsField)
admin.site.register(InvestorNomineeDetailsField)
admin.site.register(InvestorGaurdianDetails)
admin.site.register(InvestorDeclarationField)
admin.site.register(InvestorAccountTypeField)
admin.site.register(InvestorStandingInstructionsField)
admin.site.register(InvestorSmsAlertField)
admin.site.register(InvestorOtherDetailsField)
admin.site.register(ErrorsModel)
admin.site.register(UserType)
admin.site.register(InvestorDocumentManager)
admin.site.register(InvestorSelectDocument)
admin.site.register(InvestorMaritalManager)


