from . import views,application_form,api
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # dashboards
    path('investor_dashboard/',views.investor_dashboard, name='investor_dashboard'),
    path('investor_details/',views.investor_details, name='investor_details'),
    path('depository_forms/',views.depository_forms, name='depository_forms'),
    path('investor_submitted_form/',views.investor_submitted_form, name='investor_submitted_form'),
    path('investor_manage_profile/',views.investor_manage_profile, name='investor_manage_profile'),
    path('investor_profile_split/',views.investor_profile_split, name='investor_profile_split'),
    path('investor_profile_merge/',views.investor_profile_merge, name='investor_profile_merge'),
    path('investor_profile_create/',views.investor_profile_create, name='investor_profile_create'),

    # profile  
    path('delete_credit_card/', views.delete_credit_card, name='delete_credit_card'),
    path('delete_bank/', views.delete_bank, name='delete_bank'),
    path('delete_nominee/', views.delete_nominee, name='delete_nominee'),

    # investors
    path('investor_profile_submit/',views.investor_profile_submit, name='investor_profile_submit'),
    path('create_profile_form/',views.create_profile_form, name='create_profile_form'),
    path('getFormStatus/<int:profile_id>/<int:depository_id>/',views.getFormStatus, name='getFormStatus'),
    path('fetchDocumentManager/<str:nt>/', views.fetch_document_manager, name='fetch_document_manager'),
    path('fetchMaritalStatus/<str:nt>/', views.fetch_marital_status, name='fetch_marital_status'),


    # path('investor_documents_upload/',views.investor_documents_upload, name='investor_documents_upload'),
    # path('investor_document_submit/',views.investor_document_submit, name='investor_document_submit'),
    # path('investor_documents_gallery/',views.investor_documents_gallery, name='investor_documents_gallery'),
    
    # application forms
    path('investor_application_form/',application_form.investor_application_form, name='investor_application_form'),
    path('investorIdentityDetailsSave/',application_form.investorIdentityDetailsSave, name='investorIdentityDetailsSave'),
    path('investorAddressDetailsSave/',application_form.investorAddressDetailsSave, name='investorAddressDetailsSave'),
    path('investorBankDetailsSave/',application_form.investorBankDetailsSave, name='investorBankDetailsSave'),
    path('investorAdditionalKycDetailsSave/',application_form.investorAdditionalKycDetailsSave, name='investorAdditionalKycDetailsSave'),
    path('investorNomineeDetailsSave/',application_form.investorNomineeDetailsSave, name='investorNomineeDetailsSave'),
    path('investorGaurdianDetailsSave/',application_form.investorGaurdianDetailsSave, name='investorGaurdianDetailsSave'),
    path('investorDeclarationDetailsSave/',application_form.investorDeclarationDetailsSave, name='investorDeclarationDetailsSave'),
    path('investorStandingInstructionsSave/',application_form.investorStandingInstructionsSave, name='investorStandingInstructionsSave'),
    path('investorSmsAlertsSave/',application_form.investorSmsAlertsSave,name='investorSmsAlertsSave'),
    path('investorAccountTypeDetailsSave/',application_form.investorAccountTypeDetailsSave,name='investorAccountTypeDetailsSave'),
    path('investorOtherDetailsSave/',application_form.investorOtherDetailsSave, name='investorOtherDetailsSave'),
    path('application_form_print/<str:pk>/',application_form.application_form_print, name='application_form_print'),
    path('application_form_print_masked/<str:pk>/',application_form.application_form_print_masked, name='application_form_print_masked'),
    path('fecthImageCount/<str:it>/<str:rn>/',application_form.fecthImageCount, name='fecthImageCount'),
    path('fecthImages/<str:it>/<str:rn>/',application_form.fecthImages, name='fecthImages'),
    path('modalimageupload/',application_form.modalimageupload, name='modalimageupload'),
    path('document_upload_save/',application_form.document_upload_save, name='document_upload_save'),


    # Api
    path('requestDetailsAPI/<int:pk>/',api.requestDetailsAPI, name='requestDetailsAPI'),
    path('identityDetailsAPI/<int:pk>/',api.identityDetailsAPI, name='identityDetailsAPI'),
    path('addressDetailsAPI/<int:pk>/',api.addressDetailsAPI, name='addressDetailsAPI'),
    path('additionalKycDetailsAPI/<int:pk>/',api.additionalKycDetailsAPI, name='additionalKycDetailsAPI'),
    path('nomineeDetailsAPI/<int:pk>/',api.nomineeDetailsAPI, name='nomineeDetailsAPI'),
    path('accountTypeAPI/<int:pk>/',api.accountTypeAPI, name='accountTypeAPI'),
    path('gaurdianDetailsAPI/<int:pk>/',api.gaurdianDetailsAPI, name='gaurdianDetailsAPI'),
    path('declarationAPI/<int:pk>/',api.declarationAPI, name='declarationAPI'),
    path('standingInstructionsAPI/<int:pk>/',api.standingInstructionsAPI, name='standingInstructionsAPI'),
    path('smsAlertAPI/<int:pk>/',api.smsAlertAPI, name='smsAlertAPI'),
    path('bankDetailsAPI/<int:pk>/',api.bankDetailsAPI, name='bankDetailsAPI'),
    path('otherDetailsAPI/<int:pk>/',api.otherDetailsAPI, name='otherDetailsAPI'),
    path('userEmailIdApi/',api.userEmailIdApi, name='userEmailIdApi'),
#   documents details:

    path('document_checkbox/',views.document_checkbox, name='document_checkbox'),

# profile merge/split
    path('profile_merge_request/',views.profile_merge_request, name='profile_merge_request'),
    path('profile_merge_approved/',views.profile_merge_approved, name='profile_merge_approved'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)