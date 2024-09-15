from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
import json,sys
from django.contrib.auth.models import User
from investor.models import InvestorDetail,InvestorProfileMerge,Document,DocumentUpload
from core.models import ErrorsModel,ChooseInvestorFields
from depository.models import Depository,RequestDetails,InvestorIdentityDetails,InvestorAddressDetails,InvestorBankDetails,InvestorAdditionalKycDetails,InvestorNomineeDetails,InvestorAccountType,InvestorGaurdianDetails,InvestorDeclaration,InvestorStandingInstructions,InvestorSmsAlert,InvestorOtherDetails,InvestorDocumentUpload
from .serializer import RequestDetailsSearializer
## Investor Application Form


# 1. Display Page

@login_required(login_url='/login')  
def investor_application_form(request): 
    if request.POST.get('request_id','')=='' and request.POST.get('depository_id','') =='' and request.POST.get('profile_id','')=='':
        if request.session['request_id'] !='':
            rpid = request.session['request_id']
            dpid = request.session['depository_id']
            pid =  request.session['profile_id']
        elif request.session['depository_id'] !='' and request.session['profile_id']!='':
            rpid = ''
            dpid = request.session['depository_id']
            pid = request.session['profile_id']
    elif request.POST.get('depository_id','') !='' and request.POST.get('profile_id','')!='':
        rpid = request.POST.get('request_id','')
        dpid = request.POST.get('depository_id','')
        pid = request.POST.get('profile_id','')
        request.session['request_id'] = rpid 
        request.session['depository_id'] = dpid  
        request.session['profile_id'] = pid     
    else:
        return HttpResponse('It seems some error has occured, Please head bakcwards')
    
    request_id = rpid
    depository_id=dpid
    user = User.objects.get(id=int(pid))
    try:
        depository = Depository.objects.get(id=depository_id)
        requestDetails = ''
        investorIdentityDetails = ''
        investorAddressDetails = ''
        investorBankDetails = ''
        investorAdditionalKycDetails = ''
        investorNomineeDetails = ''
        investorAccountType = ''
        investorGaurdianDetails = ''
        if request_id and RequestDetails.objects.filter(id=request_id).exists():
            requestDetails = RequestDetails.objects.get(id=request_id)
            investorIdentityDetails = InvestorIdentityDetails.objects.filter(request_no = requestDetails).first()
            investorAddressDetails = InvestorAddressDetails.objects.filter(request_no = requestDetails).first()
            investorBankDetails = InvestorBankDetails.objects.filter(request_no = requestDetails).first()
            investorAdditionalKycDetails = InvestorAdditionalKycDetails.objects.filter(request_no = requestDetails).first()
            investorNomineeDetails = InvestorNomineeDetails.objects.filter(request_no = requestDetails).first()
            investorGaurdianDetails = InvestorGaurdianDetails.objects.filter(request_no = requestDetails).first()
            investorAccountType = InvestorAccountType.objects.filter(request_no = requestDetails).first()
            investorDeclaration = InvestorDeclaration.objects.filter(request_no = requestDetails).first()
            investorStandingInstructions = InvestorStandingInstructions.objects.filter(request_no = requestDetails).first()
            investorSmsAlert = InvestorSmsAlert.objects.filter(request_no = requestDetails).first()
            investorOtherDetails = InvestorOtherDetails.objects.filter(request_no = requestDetails).first()    
            context={
                'depository': depository,
                'requestDetails':requestDetails,
                #  Passing Details Which Is Already Been Saved.
                'investorIdentityDetails': investorIdentityDetails,
                'investorAddressDetails': investorAddressDetails,
                'investorBankDetails': investorBankDetails,
                'investorAdditionalKycDetails': investorAdditionalKycDetails,
                'investorNomineeDetails': investorNomineeDetails,
                'investorAccountType': investorAccountType,
                'investorGaurdianDetails': investorGaurdianDetails,
                'investorDeclaration': investorDeclaration,
                'investorStandingInstructions': investorStandingInstructions,
                'investorSmsAlert': investorSmsAlert,
                'investorOtherDetails': investorOtherDetails,
                 # Passing The Investor Fileds
                'investorIdentityDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorIdentityDetailsFields.values_list('field',flat=True)),
                'investorAddressDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAddressDetailsFields.values_list('field',flat=True)),
                'investorBankDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorBankDetailsFields.values_list('field',flat=True)),
                'investorAdditionalKycDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAdditionalKycDetailsFields.values_list('field',flat=True)),
                'investorNomineeDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorNomineeDetailsFields.values_list('field',flat=True)),
                'investorAccountTypeFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAccountTypeFields.values_list('field',flat=True)),
                'investorGaurdianDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorGaurdianDetailsFields.values_list('field',flat=True)),
                'investorDeclarationFields': list(ChooseInvestorFields.objects.get(depository=depository).investorDeclarationFields.values_list('field',flat=True)),
                'investorStandingInstructionsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorStandingInstructionsFields.values_list('field',flat=True)),
                'investorSmsAlertFields': list(ChooseInvestorFields.objects.get(depository=depository).investorSmsAlertFields.values_list('field',flat=True)),
                'investorOtherDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorOtherDetailsFields.values_list('field',flat=True)),
                # Investor Details:
                'investor_detail':InvestorDetail.objects.filter(user=user).first(),
                'user':user,
            }

        elif RequestDetails.objects.filter(depository = depository).filter(investor = user).filter(is_active = True).exists():
            requestDetails = RequestDetails.objects.filter(depository = depository).filter(investor = user).filter(is_active = True).first()
            investorIdentityDetails = InvestorIdentityDetails.objects.filter(request_no = requestDetails).first()
            investorAddressDetails = InvestorAddressDetails.objects.filter(request_no = requestDetails).first()
            investorBankDetails = InvestorBankDetails.objects.filter(request_no = requestDetails).first()
            investorAdditionalKycDetails = InvestorAdditionalKycDetails.objects.filter(request_no = requestDetails).first()
            investorNomineeDetails = InvestorNomineeDetails.objects.filter(request_no = requestDetails).first()
            investorGaurdianDetails = InvestorGaurdianDetails.objects.filter(request_no = requestDetails).first()
            investorAccountType = InvestorAccountType.objects.filter(request_no = requestDetails).first()
            investorDeclaration = InvestorDeclaration.objects.filter(request_no = requestDetails).first()
            investorStandingInstructions = InvestorStandingInstructions.objects.filter(request_no = requestDetails).first()
            investorSmsAlert = InvestorSmsAlert.objects.filter(request_no = requestDetails).first()
            investorOtherDetails = InvestorOtherDetails.objects.filter(request_no = requestDetails).first()    
            context={
                'depository': depository,
                'requestDetails':requestDetails,
                #  Passing Details Which Is Already Been Saved.
                'investorIdentityDetails': investorIdentityDetails,
                'investorAddressDetails': investorAddressDetails,
                'investorBankDetails': investorBankDetails,
                'investorAdditionalKycDetails': investorAdditionalKycDetails,
                'investorNomineeDetails': investorNomineeDetails,
                'investorAccountType': investorAccountType,
                'investorGaurdianDetails': investorGaurdianDetails,
                'investorDeclaration': investorDeclaration,
                'investorStandingInstructions': investorStandingInstructions,
                'investorSmsAlert': investorSmsAlert,
                'investorOtherDetails': investorOtherDetails,
                 # Passing The Investor Fileds
                'investorIdentityDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorIdentityDetailsFields.values_list('field',flat=True)),
                'investorAddressDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAddressDetailsFields.values_list('field',flat=True)),
                'investorBankDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorBankDetailsFields.values_list('field',flat=True)),
                'investorAdditionalKycDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAdditionalKycDetailsFields.values_list('field',flat=True)),
                'investorNomineeDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorNomineeDetailsFields.values_list('field',flat=True)),
                'investorAccountTypeFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAccountTypeFields.values_list('field',flat=True)),
                'investorGaurdianDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorGaurdianDetailsFields.values_list('field',flat=True)),
                'investorDeclarationFields': list(ChooseInvestorFields.objects.get(depository=depository).investorDeclarationFields.values_list('field',flat=True)),
                'investorStandingInstructionsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorStandingInstructionsFields.values_list('field',flat=True)),
                'investorSmsAlertFields': list(ChooseInvestorFields.objects.get(depository=depository).investorSmsAlertFields.values_list('field',flat=True)),
                'investorOtherDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorOtherDetailsFields.values_list('field',flat=True)),
                # Investor Details:
                'investor_detail':InvestorDetail.objects.filter(user=user).first(),
                'user':user,
            }        
        else:
            requestDetails = RequestDetails.objects.create(depository = depository,investor = user)        
            context = {
            'depository': depository,
            'requestDetails':requestDetails,
            # Passing The Investor Fileds
            'investorIdentityDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorIdentityDetailsFields.values_list('field',flat=True)),
            'investorAddressDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAddressDetailsFields.values_list('field',flat=True)),
            'investorBankDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorBankDetailsFields.values_list('field',flat=True)),
            'investorAdditionalKycDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAdditionalKycDetailsFields.values_list('field',flat=True)),
            'investorNomineeDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorNomineeDetailsFields.values_list('field',flat=True)),
            'investorAccountTypeFields': list(ChooseInvestorFields.objects.get(depository=depository).investorAccountTypeFields.values_list('field',flat=True)),
            'investorGaurdianDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorGaurdianDetailsFields.values_list('field',flat=True)),
            'investorDeclarationFields': list(ChooseInvestorFields.objects.get(depository=depository).investorDeclarationFields.values_list('field',flat=True)),
            'investorStandingInstructionsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorStandingInstructionsFields.values_list('field',flat=True)),
            'investorSmsAlertFields': list(ChooseInvestorFields.objects.get(depository=depository).investorSmsAlertFields.values_list('field',flat=True)),
            'investorOtherDetailsFields': list(ChooseInvestorFields.objects.get(depository=depository).investorOtherDetailsFields.values_list('field',flat=True)),
            # Investor Details:
            'investor_detail':InvestorDetail.objects.filter(user=user).first(),
            'user':user,
            }
        return render(request, 'investors/application_form.html', context)
    except Exception as e:
        print(e)
        ErrorsModel.objects.create(error_caught_function=f'investor_application_form - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)   
        return render(request, 'investors/application_form.html', context)
        # return HttpResponse("It seems some error has occured")  



## Saving/Updating Investor Application Details: 🫡

# start's here:

# Identity Details
@login_required(login_url='/login')
def investorIdentityDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
                       
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                # investor_detail = InvestorDetail.objects.filter(user=request.user).first()
                # applicant_first_name = investor_detail.first_name if investor_detail.first_name else ''
                requestNo = RequestDetails.objects.get(requestno=request_no)               
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorIdentityDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={ 
                'applicant_first_name': request.POST.get('applicant_first_name'),
                'applicant_middle_name': request.POST.get('applicant_middle_name',''),
                'applicant_last_name': request.POST.get('applicant_last_name',''),
                'father_first_name': request.POST.get('father_first_name',''),
                'father_middle_name': request.POST.get('father_middle_name',''),
                'father_last_name': request.POST.get('father_last_name',''),
                'mother_first_name': request.POST.get('mother_first_name',''),
                'mother_middle_name': request.POST.get('mother_middle_name',''),
                'mother_last_name': request.POST.get('mother_last_name',''),            
                'maiden_name': request.POST.get('maiden_name','').replace(" ", ""),
                'gender': request.POST.get('gender',''),
                'date_of_birth': None if request.POST.get('dob','')=='' else request.POST.get('dob'),
                'martial_status': request.POST.get('martial_status',''),
                'nationality': request.POST.get('nationality',''),
                'resident_status': request.POST.get('resident_status',''),
                'pan_no': request.POST.get('pan_no',''),
                'aadhar_no': request.POST.get('aadhar_no',''),
                }
                )
                response_data['message'] = f'Identity Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            print(e)
            ErrorsModel.objects.create(error_caught_function=f'investorIdentityDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            

# Address Details
@login_required(login_url='/login')
def investorAddressDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
            # for key, value in request.POST.items():
            #     print(f'{key}: {value}')
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorAddressDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'residence_address': request.POST.get('residence_address',''),
                'city': request.POST.get('city',''),
                'pincode': request.POST.get('pincode',''),
                'state': request.POST.get('state',''),
                'district': request.POST.get('district',''),
                'country': request.POST.get('country',''),
                'mobile_no': request.POST.get('mobile_no',''),
                'tel_no': request.POST.get('tel_no',''),
                'email_id': request.POST.get('email_id',''),
                'permanent_address': request.POST.get('permanent_address',''),
                'permanent_city': request.POST.get('permanent_city',''),
                'permanent_district': request.POST.get('permanent_district',''),
                'permanent_pincode': request.POST.get('permanent_pincode',''),
                'permanent_state': request.POST.get('permanent_state',''),
                'permanent_country': request.POST.get('permanent_country',''),
                }
                )
                response_data['message'] = f'Address Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorAddressDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            

# Bank Details
@login_required(login_url='/login')
def investorBankDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorBankDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'bank_name': request.POST.get('bank_name',''),
                'branch_address': request.POST.get('branch_address',''),
                'city': request.POST.get('city',''),
                'pincode': request.POST.get('pincode',''),
                'state': request.POST.get('state',''),
                'country': request.POST.get('country',''),
                'account_type': request.POST.get('account_type',''),
                'micr_number': request.POST.get('micr_number',''),
                'account_no': request.POST.get('account_no',''),
                'ifsc_number': request.POST.get('ifsc_number',''),
                }
                )
                response_data['message'] = f'Bank Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorBankDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            

# Additional Kyc Details
@login_required(login_url='/login')
def investorAdditionalKycDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorAdditionalKycDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'dp_reference_number': request.POST.get('dp_reference_number',''),
                'kycdate': None if request.POST.get('kycdate','')=='' else request.POST.get('kycdate'),
                'dp_id': request.POST.get('dp_id',''),
                'client_id': request.POST.get('client_id',''),
                'first_holder_name': request.POST.get('first_holder_name',''),
                'second_holder_name': request.POST.get('second_holder_name',''),
                'third_holder_name': request.POST.get('third_holder_name',''),
                'first_holder_pancard': request.POST.get('first_holder_pancard',''),
                'second_holder_pancard': request.POST.get('second_holder_pancard',''),
                'third_holder_pancard': request.POST.get('third_holder_pancard',''),
                'declaration_name': request.POST.get('declaration_name',''),
                'declaration': True if request.POST.get('declaration','') in ['True','true'] else False,
                }
                )
                response_data['message'] = f'Additional KYC Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorAdditionalKycDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            

# Nominee Details
@login_required(login_url='/login')
def investorNomineeDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
            # for key, value in request.POST.items():
            #     print(f'{key}: {value}')
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorNomineeDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'registration_no': request.POST.get('registration_no',''),
                'title': request.POST.get('title',''),
                'nominee_firstname': str(request.POST.get('nominee_firstname','')),
                'nominee_middlename': str(request.POST.get('nominee_middlename','')),
                'nominee_lastname': str(request.POST.get('nominee_lastname','')),
                'nominee_nickname': str(request.POST.get('nominee_nickname','')),
                'nominee_address': request.POST.get('nominee_address',''),
                'nominee_city': request.POST.get('nominee_city',''),
                'nominee_pincode': request.POST.get('nominee_pincode',''),
                'nominee_state': request.POST.get('nominee_state',''),
                'nominee_country': request.POST.get('nominee_country',''),
                'nominee_mobile_no': request.POST.get('nominee_mobile_no',''),
                'nominee_aadhar': request.POST.get('nominee_aadhar',''),
                'nominee_email': request.POST.get('nominee_email',''),
                'nominee_date_of_birth': None if request.POST.get('nominee_date_of_birth','')=='' else request.POST.get('nominee_date_of_birth'),
                'nominee_relationship': request.POST.get('nominee_relationship',''),
                'nominee_declaration_1': True if request.POST.get('nominee_declaration_1','') in ['True','true'] else False,
                'nominee_declaration_2': True if request.POST.get('nominee_declaration_2','') in ['True','true'] else False,
                'set_as_primary':True if request.POST.get(f'nominee_details_radio','') in ['True','true'] else False,
                }
                )
                response_data['message'] = f'Nominee Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorNomineeDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")


# Gaurdian Details
@login_required(login_url='/login')
def investorGaurdianDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorGaurdianDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'gaurdian_name': str(request.POST.get('gaurdian_name','')).replace(" ", "")+','+str(request.POST.get('gaurdian_name','')).replace(" ", "")+','+str(request.POST.get('gaurdian_name','')).replace(" ", ""),
                'relationship': request.POST.get('relationship',''),
                'pancard': request.POST.get('pancard',''),
                'address': request.POST.get('address',''),
                'city': request.POST.get('city',''),
                'pincode':request.POST.get('pincode',''),
                'state': request.POST.get('state',''),
                'country': request.POST.get('country',''),
                'mobile_no': request.POST.get('mobile_no',''),
                'fax_no': request.POST.get('fax_no',''),
                'email_id': request.POST.get('email_id',''),
                }
                )
                response_data['message'] = f'Gaurdian Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorGaurdianDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
  
# end's here

# Declaration Details
@login_required(login_url='/login')
def investorDeclarationDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
            print(request.POST.get('profile_id'))
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    print(requestNo)    
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorDeclaration.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'place': request.POST.get('place',''),
                'date': None if request.POST.get('date','')=='' else request.POST.get('date'),
                }
                )
                requestNo.is_active=False
                print(requestNo.is_active)
                requestNo.save()
                response_data['message'] = 700
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            print(e)
            ErrorsModel.objects.create(error_caught_function=f'investorDeclarationDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

# AccountTypeDetails
@login_required(login_url='/login')
def investorAccountTypeDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")                
                identity_details, created = InvestorAccountType.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'status': request.POST.get('status',''),
                'sub_status': request.POST.get('sub_status',''),        
                }
                )
                response_data['message'] = f'Account Type Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorAccountTypeDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
  
# StandingInstructions
@login_required(login_url='/login')
def investorStandingInstructionsSave(request):
    response_data={}
    if request.method=="POST":
        try:
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorStandingInstructions.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'declaration_1': request.POST.get('declaration_1',''),
                'declaration_2': request.POST.get('declaration_2',''),
                'declaration_3': request.POST.get('declaration_3',''),
                'declaration_4': request.POST.get('declaration_4',''),
                'declaration_5': request.POST.get('declaration_5',''),
                'account_statement': request.POST.get('account_statement',''),
                'annual_report': request.POST.get('annual_report',''),
                }
                )
                response_data['message'] = f'Standing Instructions Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorStandingInstructionsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
  

# SmsAlert
@login_required(login_url='/login')
def investorSmsAlertsSave(request):
    response_data={}
    if request.method=="POST":
        try:
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorSmsAlert.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'declaration': True if request.POST.get('declaration','') in ['True','true'] else False,
                'mobile_no': request.POST.get('mobile_no',''),
                'name': request.POST.get('name',''),
                
                }
                )
                response_data['message'] = f'Sms Alert Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'investorSmsAlertSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

# OtherDetails
@login_required(login_url='/login')
def investorOtherDetailsSave(request):
    response_data={}
    if request.method=="POST":
        try:
             
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                identity_details, created = InvestorOtherDetails.objects.update_or_create(
                request_no=requestNo,
                defaults={
                'gross_annual_income_detail': request.POST.get('gross_annual_income_detail',''),
                'occupation': request.POST.get('occupation',''),
                'declaration': request.POST.get('declaration',''),
                'other_info': request.POST.get('other_info',''),
                
                }
                )
                response_data['message'] = f'Other Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            ErrorsModel.objects.create(error_caught_function=f'InvestorOtherDetailsSave - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
  
# end's here

# application form print
# Start's here
def application_form_print(request,pk):
    if request.user.id == RequestDetails.objects.get(requestno=pk).investor.id or RequestDetails.objects.get(requestno=pk).investor.id in list(item[0] for item in InvestorProfileMerge.objects.filter(investor=request.user,status='ACCEPTED').values_list('member')) :   
        context={
            'request_details':RequestDetails.objects.get(requestno=pk)
        }        
        return render(request, 'investors/application_form/application_form_print.html', context)
    else:
        return HttpResponse(f'OOPS! YOU ARE NOT ALLOWED TO DO THIS')
def application_form_print_masked(request,pk):
    if request.user.id == RequestDetails.objects.get(requestno=pk).investor.id or RequestDetails.objects.get(requestno=pk).investor.id in list(item[0] for item in InvestorProfileMerge.objects.filter(investor=request.user,status='ACCEPTED').values_list('member')) :   
        context={
            'request_details':RequestDetails.objects.get(requestno=pk)
        }  
        return render(request, 'investors/application_form/application_form_print_masked.html', context)
    else:
        return HttpResponse(f'OOPS! YOU ARE NOT ALLOWED TO DO THIS')


#  Docuements/Images:
## Start's here 

def fecthImageCount(request,it,rn):
    user = RequestDetails.objects.get(requestno = rn).investor
    data={
        'selected_count':Document.objects.filter(document_data__user=user,document=it,set_as_primary=True).count()
    }
    return JsonResponse(data, content_type="application/json")

from investor.crypto import decrypt_image
def fecthImages(request,it,rn):
    user = RequestDetails.objects.get(requestno = rn).investor
    images = []
    documents = Document.objects.filter(document_data__user=user,document=it)
    for document in documents:
        if document:
            decrypted_image = decrypt_image(document.image, document.key, document.tag, document.iv)
            images.append((decrypted_image, document.id, document.set_as_primary))
    data={
        'images':images,
    }
    return JsonResponse(data, content_type="application/json")


def modalimageupload(request):
    response_data={}
    document_details = DocumentUpload.objects.get(user = RequestDetails.objects.get(requestno = request.POST.get('request_no')).investor)
    document_name = request.POST.get('imagetag')
    count = 0
    try:
        for image in request.FILES.getlist('files'):
            data = image.read()
            Document.objects.create(image=data, document_data=document_details, document=document_name)
            count+=1
    except Exception as e:
        print(e)
        pass
    if count > 0:
        response_data['response_code'] = 200
        response_data['message'] = f'{count} image has been uploaded' if count == 1 else f'{count} images have been uploaded'        
    else:
        response_data['response_code'] = 400
        response_data['message'] = f'It Seem''s some error has occured'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
  


@login_required(login_url='/login')
def document_upload_save(request):
    response_data={}
    if request.method=="POST":
        try:
            depository = Depository.objects.get(id=int(request.POST.get('depository','')))
            request_no = request.POST.get('request_no','')
            if depository and request_no:
                requestNo = RequestDetails.objects.get(requestno=request_no)
                if requestNo.is_active==False:
                    response_data['message'] = f'OOPS! YOU ARE NOT ALLOWED TO DO THIS'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")

                document_details, created = InvestorDocumentUpload.objects.update_or_create(
                    request_no=requestNo,
                    defaults={}
                )

                document_queryset = Document.objects.filter(document_data__user=RequestDetails.objects.get(requestno=request.POST.get('request_no')).investor, set_as_primary=True)

                document_details.document.set(document_queryset)

                response_data['message'] = f'Documents Details has been saved successfully...'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                print(e)
                response_data['message'] = f'It Seem''s Investor or Depository or RequestNo is missing'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            print(e)
            ErrorsModel.objects.create(error_caught_function=f'document_upload_save - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)
            response_data['message'] = f'It Seem''s some error has occured'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
## End's here


## Load Data From Prev Saved Form 🫡

# Start's here


# End's here