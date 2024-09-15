from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json,sys
from django.contrib.auth.models import User
from .models import InvestorDetail,InvestorNomineeDetail,InvestorCreditCard,Document,DocumentUpload,InvestorProfileMerge,InvestorBankDetail
from django.shortcuts import render, get_object_or_404
from depository.models import Depository,RequestDetails
from .crypto import decrypt_image
from core.models import ErrorsModel,InvestorDocumentManager,InvestorMaritalManager
from django.contrib.auth.hashers import make_password
from core.models import UserType,UserTypeRole
from django.http import JsonResponse
import datetime
# Create your views here.

## Investor Dashboard
@login_required(login_url='/login')
def investor_dashboard(request):
    return render(request, 'investors/dashboard/dashboard.html')

from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
def fetch_document_manager(request, nt):
    try:
        selected_data = list(item[0] for item in InvestorDocumentManager.objects.get(nationality=nt).documents.all().values_list('document'))
    except ObjectDoesNotExist:
        selected_data = []  
    
    data = {
        'selected_data': selected_data,
    }
    return JsonResponse(data)

def fetch_marital_status(request, nt):
    selected_status = list(item[0] for item in InvestorMaritalManager.objects.get(marital=nt).documentss.all().values_list('document'))
    print(selected_status,"====================================================")
    data = {
        'selected_status': selected_status,
    }
    return JsonResponse(data)

@login_required(login_url='/login')
def investor_manage_profile(request):
    return render(request, 'investors/dashboard/investor_manage_profile.html')

@login_required(login_url='/login')
def investor_submitted_form(request):
    lis = list(InvestorProfileMerge.objects.filter(investor=request.user,status='ACCEPTED').values_list('member',flat=True))
    lis.append(request.user.id)
    context={
        'requestDetails':RequestDetails.objects.filter(investor__id__in=lis)
    }
    return render(request, 'investors/dashboard/submitted_forms.html',context)

@login_required(login_url='/login')
def investor_profile_split(request):
    return render(request, 'investors/dashboard/profile_split.html')

@login_required(login_url='/login')
def investor_profile_merge(request):
    return render(request, 'investors/dashboard/profile_merge.html')

@login_required(login_url='/login')
def investor_profile_create(request):
    print(make_password(request.user.password))
    return render(request, 'investors/dashboard/create_profile.html')

@login_required(login_url='/login')
def depository_forms(request):
    context={
        'depository': Depository.objects.all(),
        'profiles':InvestorProfileMerge.objects.filter(investor=request.user,status='ACCEPTED'),
    }
    return render(request, 'investors/dashboard/depository_forms.html', context)

## Investor Profile
@login_required(login_url='/login')
def investor_details(request):
    form_status=1
    if request.GET.get('profile_id'):
        ipm = InvestorProfileMerge.objects.get(id=request.GET.get('profile_id'))
        if ipm.investor==request.user:
            user = ipm.member
            if ipm.permission=='Read':
                form_status = 0
        else:
            return HttpResponse('''Don't be over smart 🫡''')
    else:
        user = request.user
    # upload img
    doc = DocumentUpload.objects.filter(user=user).first()
    if doc:
        
        # uploded date 
        aadhar_sef_date = doc.documents.filter(document='AADHAR CARD SELF').order_by('-date_updated').first()
        aadhar_father_date = doc.documents.filter(document='AADHAR CARD FATHER').order_by('-date_updated').first()
        aadhar_mother_date = doc.documents.filter(document='AADHAR CARD MOTHER').order_by('-date_updated').first()
        aadhar_spouse_date = doc.documents.filter(document='AADHAR CARD SPOUSE').order_by('-date_updated').first()
        pan_sef_date = doc.documents.filter(document='PAN CARD SELF').order_by('-date_updated').first()
        pan_father_date = doc.documents.filter(document='PAN CARD FATHER').order_by('-date_updated').first()
        pan_mother_date = doc.documents.filter(document='PAN CARD MOTHER').order_by('-date_updated').first()
        pan_spouse_date = doc.documents.filter(document='PAN CARD SPOUSE').order_by('-date_updated').first()
        passport_date = doc.documents.filter(document='PASSPORT').order_by('-date_updated').first()
        visa_date = doc.documents.filter(document='VISA').order_by('-date_updated').first()
        overtax_date = doc.documents.filter(document='OVERSEA TAX').order_by('-date_updated').first()
        passbook_date = doc.documents.filter(document='BANK PASSBOOK').order_by('-date_updated').first()
        utility_date = doc.documents.filter(document='UTILITY BILL').order_by('-date_updated').first()
        statement_date = doc.documents.filter(document='BANK STATEMENT').order_by('-date_updated').first()
        cheque_date = doc.documents.filter(document='BANK CHEQUE').order_by('-date_updated').first()
        cc_date = doc.documents.filter(document='CREDIT CARD').order_by('-date_updated').first()
        document_choices = [c[0] for c in Document.document.field.choices]
        upload_dict = {choice: [] for choice in document_choices}
        for choice in document_choices:
        # Filter the documents based on the choice and retrieve them
            documents = doc.documents.filter(document=choice)
            # Iterate over the filtered documents and process them
            for document in documents:
                if document:
                    decrypted_image = decrypt_image(document.image, document.key, document.tag, document.iv)
                    upload_dict[choice].append((decrypted_image, document.id, document.set_as_primary))

        context={
            'user':user,
            'form_status':form_status,
            'upload_dict': upload_dict,
            'aadhar_sef_date':aadhar_sef_date,'aadhar_father_date':aadhar_father_date,'aadhar_mother_date':aadhar_mother_date,'aadhar_spouse_date':aadhar_spouse_date,
            'pan_sef_date':pan_sef_date,'pan_father_date':pan_father_date,'pan_mother_date':pan_mother_date,'pan_spouse_date':pan_spouse_date,
            'passport_date':passport_date,'passbook_date':passbook_date,'visa_date':visa_date,'overtax_date':overtax_date,'utility_date':utility_date,'statement_date':statement_date,'cheque_date':cheque_date,'cc_date':cc_date,
        }
        return render(request, 'investors/dashboard/investor_details.html', context)
    else:
        context={
            'user':user,
            'form_status':form_status,
        }
        return render(request, 'investors/dashboard/investor_details.html',context)
    
import traceback

## Investor Profile Save
@login_required(login_url='/login')
def investor_profile_submit(request):
    response_data={}
    try:
        if request.POST.get('profile_id'):
            ipm = InvestorProfileMerge.objects.get(id=request.POST.get('profile_id'))
            if ipm.investor==request.user:
                user = ipm.member
                if not ipm.permission=='Read/Write':
                    return HttpResponse('''Don't be over smart 🫡''')
        else:
            user = request.user      
        user_details, created = InvestorDetail.objects.update_or_create(
        user=user,
        defaults={
            'first_name' : request.POST.get('first_name',''), 
            'middle_name' : request.POST.get('middle_name',''), 
            'last_name' : request.POST.get('last_name',''), 
            'nationality' : request.POST.get('nationality',''), 
            'dob' : None if request.POST.get('dob','')=='' else request.POST.get('dob'), 
            'martial_status' : request.POST.get('martial_status',''), 
            'father_first_name' : request.POST.get('father_first_name',''), 
            'father_middle_name' : request.POST.get('father_middle_name',''), 
            'father_last_name' : request.POST.get('father_last_name',''), 
            'mother_first_name' : request.POST.get('mother_first_name',''), 
            'mother_middle_name' : request.POST.get('mother_middle_name',''), 
            'mother_last_name' : request.POST.get('mother_last_name',''), 
            'spouse_first_name' : request.POST.get('spouse_first_name',''), 
            'spouse_middle_name' : request.POST.get('spouse_middle_name',''), 
            'spouse_last_name' : request.POST.get('spouse_last_name',''), 
            'flat_no' : request.POST.get('flat_no',''), 
            'bldg_no' : request.POST.get('bldg_no',''), 
            'street_name' : request.POST.get('street_name',''), 
            'city' : request.POST.get('city',''), 
            'district' : request.POST.get('district',''), 
            'pincode' : request.POST.get('pincode',''), 
            'state' : request.POST.get('state',''), 
            'country' : request.POST.get('country',''), 
            'mobile_no' : request.POST.get('mobile_no',''), 
            'tel_no' : request.POST.get('tel_no',''), 
            'email_id' : request.POST.get('email_id',''), 
            'alternate_email_id' : request.POST.get('alternate_email_id',''), 
            'primary_contact' : request.POST.get('primary_contact',''), 
            'secondary_contact' : request.POST.get('secondary_contact',''), 
            'employeement' : request.POST.get('employeement',''), 
            'company_name' : request.POST.get('company_name',''), 
            'landmark' : request.POST.get('landmark',''), 
            'income' : request.POST.get('income') if request.POST.get('income')!='' else 0  ,
            'gender' : request.POST.get('gender',''), 

        }
        )
        # bank details form start 
        try:
            for i in range(1,int(request.POST.get('bank_form_len'))+1):
                if request.POST.get(f'bank_id_{i}'):
                    data = InvestorBankDetail.objects.get(id=request.POST.get(f'bank_id_{i}'))
                    if request.POST.get(f'bank_name_{i}'):
                        data.bank_name=request.POST.get(f'bank_name_{i}','')
                        data.branch_address=request.POST.get(f'branch_address_{i}','') 
                        data.account_type=request.POST.get(f'account_type_{i}','') 
                        data.pincode=request.POST.get(f'pincode_{i}','')
                        data.account_type=request.POST.get(f'account_type_{i}','')
                        data.micr_number=request.POST.get(f'micr_number_{i}','')
                        data.account_no=request.POST.get(f'account_no_{i}','')
                        data.ifsc_number=request.POST.get(f'ifsc_number_{i}','')
                        data.pb_entry_from=None if request.POST.get(f'pb_entry_from_{i}','')=='' else request.POST.get(f'pb_entry_from_{i}')
                        data.pb_entry_to=None if request.POST.get(f'pb_entry_to_{i}','')=='' else request.POST.get(f'pb_entry_to_{i}')
                        data.st_entry_from=None if request.POST.get(f'st_entry_from_{i}','')=='' else request.POST.get(f'st_entry_from_{i}')
                        data.st_entry_to=None if request.POST.get(f'st_entry_to_{i}','')=='' else request.POST.get(f'st_entry_to_{i}')
                        data.set_as_primary=True if request.POST.get(f'bank_details_radio_{i}','') in ['True','true'] else False
                        data.save()
                    else:
                        data.delete()
                else:
                    if request.POST.get(f'bank_name_{i}'):
                        InvestorBankDetail.objects.create(
                        document_data=user_details,
                        bank_name=request.POST.get(f'bank_name_{i}',''),
                        branch_address=request.POST.get(f'branch_address_{i}',''),
                        account_type=request.POST.get(f'account_type_{i}','') ,
                        pincode=request.POST.get(f'pincode_{i}',''),
                        micr_number=request.POST.get(f'micr_number_{i}',''),
                        account_no=request.POST.get(f'account_no_{i}',''),
                        ifsc_number=request.POST.get(f'ifsc_number_{i}',''),
                        pb_entry_from=None if request.POST.get(f'pb_entry_from_{i}','')=='' else request.POST.get(f'pb_entry_from_{i}'),
                        pb_entry_to=None if request.POST.get(f'pb_entry_to_{i}','')=='' else request.POST.get(f'pb_entry_to_{i}'),
                        st_entry_from=None if request.POST.get(f'st_entry_from_{i}','')=='' else request.POST.get(f'st_entry_from_{i}'),
                        st_entry_to=None if request.POST.get(f'st_entry_to_{i}','')=='' else request.POST.get(f'st_entry_to_{i}'),
                        set_as_primary=True if request.POST.get(f'bank_details_radio_{i}','') in ['True','true'] else False,             
                        ) 
                    else:
                        pass             
        except Exception as e:
            print(e) 
        # bank details form end

        # credit card details form start
        try:
            for i in range(1,int(request.POST.get('cc_form_len'))+1):
                if request.POST.get(f'cc_id_{i}'):
                    data = InvestorCreditCard.objects.get(id=request.POST.get(f'cc_id_{i}'))
                    if request.POST.get(f'cc_bank_name_{i}'):
                        data.cc_bank_name=request.POST.get(f'cc_bank_name_{i}','') 
                        data.cc_number=request.POST.get(f'cc_number_{i}','') 
                        data.cc_limit=request.POST.get(f'cc_limit_{i}','') 
                        data.cc_type=request.POST.get(f'cc_type_{i}','') 
                        data.set_as_primary=True if request.POST.get(f'cc_details_radio_{i}','') in ['True','true'] else False
                        data.save()
                    else:
                        data.delete()
                else:
                    if request.POST.get(f'cc_bank_name_{i}'):
                        InvestorCreditCard.objects.create(
                        document_data=user_details,
                        cc_bank_name=request.POST.get(f'cc_bank_name_{i}',''),
                        cc_number=request.POST.get(f'cc_number_{i}',''),
                        cc_limit=request.POST.get(f'cc_limit_{i}',''),
                        cc_type=request.POST.get(f'cc_type_{i}',''),
                        set_as_primary=True if request.POST.get(f'cc_details_radio_{i}','') in ['True','true'] else False, 
                        )
                    else:
                        pass
        except Exception as e:
            print(e) 
        
        # credit card details form end
        # nominee details form start
        try:
            for i in range(1,int(request.POST.get('nominee_form_len'))+1):
                if request.POST.get(f'nominee_id_{i}'):
                    data = InvestorNomineeDetail.objects.get(id=request.POST.get(f'nominee_id_{i}'))
                    if request.POST.get(f'nominee_firstname_{i}'):
                        data.nominee_firstname=request.POST.get(f'nominee_firstname_{i}','') 
                        data.nominee_middlename=request.POST.get(f'nominee_middlename_{i}','') 
                        data.nominee_lastname=request.POST.get(f'nominee_lastname_{i}','') 
                        data.nominee_nickname=request.POST.get(f'nominee_nickname_{i}','') 
                        data.nominee_date_of_birth=None if request.POST.get(f'nominee_date_of_birth_{i}','')=='' else request.POST.get(f'nominee_date_of_birth_{i}')
                        data.nominee_relationship=request.POST.get(f'nominee_relationship_{i}','') 
                        data.nominee_address=request.POST.get(f'nominee_address_{i}','') 
                        data.nominee_email=request.POST.get(f'nominee_email_{i}','') 
                        data.nominee_aadhar=request.POST.get(f'nominee_aadhar_{i}','') 
                        data.set_as_primary=True if request.POST.get(f'nominee_details_radio_{i}','') in ['True','true'] else False
                        data.registration_no=request.POST.get(f'registration_no_{i}','') 
                        data.title=request.POST.get(f'title_{i}','') 
                        data.nominee_city=request.POST.get(f'nominee_city_{i}','') 
                        data.nominee_pincode=request.POST.get(f'nominee_pincode_{i}','') 
                        data.nominee_state=request.POST.get(f'nominee_state_{i}','') 
                        data.nominee_country=request.POST.get(f'nominee_country_{i}','') 
                        data.nominee_mobile_no=request.POST.get(f'nominee_mobile_no{i}','') 
                        data.nominee_declaration_1=request.POST.get(f'nominee_declaration_1{i}','') 
                        data.nominee_declaration_2=request.POST.get(f'nominee_declaration_2{i}','')
                        data.save()
                    else:
                        data.delete()
                else:
                    if request.POST.get(f'nominee_firstname_{i}'):                      
                        InvestorNomineeDetail.objects.create(
                        document_data=user_details,
                        nominee_firstname=request.POST.get(f'nominee_firstname_{i}',''),
                        nominee_middlename=request.POST.get(f'nominee_middlename_{i}',''),
                        nominee_lastname=request.POST.get(f'nominee_lastname_{i}',''),
                        nominee_nickname=request.POST.get(f'nominee_nickname_{i}',''),
                        nominee_date_of_birth=None if request.POST.get(f'nominee_date_of_birth_{i}','')=='' else request.POST.get(f'nominee_date_of_birth_{i}'),
                        nominee_relationship=request.POST.get(f'nominee_relationship_{i}',''),
                        nominee_address=request.POST.get(f'nominee_address_{i}',''),
                        nominee_email=request.POST.get(f'nominee_email_{i}',''),
                        nominee_aadhar=request.POST.get(f'nominee_aadhar_{i}',''),
                        set_as_primary=True if request.POST.get(f'nominee_details_radio_{i}','') in ['True','true'] else False, 
                        registration_no=request.POST.get(f'registration_no_{i}',''),
                        title=request.POST.get(f'title_{i}',''),
                        nominee_city=request.POST.get(f'nominee_city_{i}',''),
                        nominee_pincode=request.POST.get(f'nominee_pincode_{i}',''),
                        nominee_state=request.POST.get(f'nominee_state_{i}',''),
                        nominee_country=request.POST.get(f'nominee_country_{i}',''),
                        nominee_mobile_no=request.POST.get(f'nominee_mobile_no_{i}',''),
                        nominee_declaration_1=request.POST.get(f'nominee_declaration_1_{i}',''),
                        nominee_declaration_2=request.POST.get(f'nominee_declaration_2_{i}',''),
                        )
                    else:
                        pass
        except Exception as e:
            print(e) 
    
        # nominee details form end
       
        aadhar_card_self = request.FILES.getlist('aadhar_card_self')
        aadhar_card_father = request.FILES.getlist('aadhar_card_father')
        aadhar_card_mother = request.FILES.getlist('aadhar_card_mother')
        aadhar_card_spouse = request.FILES.getlist('aadhar_card_spouse')
        pan_card_self = request.FILES.getlist('pan_card_self')
        pan_card_father = request.FILES.getlist('pan_card_father')
        pan_card_mother = request.FILES.getlist('pan_card_mother')
        pan_card_spouse = request.FILES.getlist('pan_card_spouse')
        passport = request.FILES.getlist('passport')
        oversea_tax_id = request.FILES.getlist('oversea_tax_id')
        visa = request.FILES.getlist('visa')
        bill = request.FILES.getlist('bill')
        bank_passbook = request.FILES.getlist('bank_passbook')
        bank_statement = request.FILES.getlist('bank_statement')
        bank_cheque = request.FILES.getlist('bank_cheque')
        cc_sign = request.FILES.getlist('cc_sign')        
        document_details, created = DocumentUpload.objects.update_or_create(
        user=user,
        defaults={   
            'bill_date':None if request.POST.get('bill_date','')=='' else request.POST.get('bill_date'), 
            'bill_name':request.POST.get('bill_name',''),
            'bill_number':request.POST.get('bill_number',''),
            'date_updated':request.POST.get('date_updated',''),
            'pp_id':request.POST.get('pp_id',''),
            'client_id_1':request.POST.get('client_id_1',''),
            'client_id_2':request.POST.get('client_id_2',''),
            'client_id_3':request.POST.get('client_id_3',''),
            'client_id_4':request.POST.get('client_id_4',''),
            'broker_name':request.POST.get('broker_name',''),
            'aadhar_self_no':request.POST.get('aadhar_self_no',''),
            'aadhar_father_no':request.POST.get('aadhar_father_no',''),
            'aadhar_mother_no':request.POST.get('aadhar_mother_no',''),
            'aadhar_spouse_no':request.POST.get('aadhar_spouse_no',''),
            'pancard_self_no':request.POST.get('pancard_self_no',''),
            'pancard_father_no':request.POST.get('pancard_father_no',''),
            'pancard_mother_no':request.POST.get('pancard_mother_no',''),
            'pancard_spouse_no':request.POST.get('pancard_spouse_no',''),
            'passport_data':request.POST.get('passport_data',''),
            'oversea_tax':request.POST.get('oversea_tax',''),
            'visa_no':request.POST.get('visa_no',''),
        }        
        ) 
        
        try:           
            image_list = [aadhar_card_self,aadhar_card_father,aadhar_card_mother,aadhar_card_spouse,
                            pan_card_self,pan_card_father,pan_card_mother,pan_card_spouse ,
                            passport, oversea_tax_id, visa, bill, bank_passbook,bank_statement,bank_cheque, cc_sign,]
            document_names = {'AADHAR CARD SELF': aadhar_card_self,'AADHAR CARD FATHER':aadhar_card_father,'AADHAR CARD MOTHER':aadhar_card_mother,'AADHAR CARD SPOUSE':aadhar_card_spouse,
                            'PAN CARD SELF': pan_card_self,'PAN CARD FATHER':pan_card_father,'PAN CARD MOTHER':pan_card_mother,'PAN CARD SPOUSE':pan_card_spouse ,
                            'PASSPORT': passport, 'OVERSEA TAX': oversea_tax_id, 'VISA': visa, 'UTILITY BILL': bill, 'BANK PASSBOOK': bank_passbook, 'BANK STATEMENT': bank_statement,'BANK CHEQUE':bank_cheque,'CREDIT CARD': cc_sign, }
            for document_name, images in zip(document_names.keys(), image_list):
                for image in images:
                    data = image.read()
                    Document.objects.create(image=data, document_data=document_details, document=document_name)

        except Exception as e:
            print("There was an error: " + e.args[0] + ". The line where the code failed was " + str(traceback.extract_stack()[-1][1]))
        response_data['message'] = 'Data has been saved successfully'
    except Exception as e:
        print("There was an error: " + e.args[0] + ". The line where the code failed was " + str(traceback.extract_stack()[-1][1]))
        ErrorsModel.objects.create(error_caught_function=f'investor_profile_submit - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)   
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")
   

def document_checkbox(request):
    response_data={}
    try:
        trigger = True if request.POST.get('trigger','') in ['True','true'] else False
        document_id = request.POST.get('id')
        doc = Document.objects.get(id=document_id)
        doc.set_as_primary = trigger
        doc.save()
        response_data['message'] = 200
    except Exception as e:
        print(e)
        ErrorsModel.objects.create(error_caught_function=f'document_checkbox - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)   
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def profile_merge_request(request):
    response_data={}
    try:
        username = request.POST.get('username','')
        member_profile = User.objects.get(username=username)
        investor_profile = request.user
        if not InvestorProfileMerge.objects.filter(investor=investor_profile,member=member_profile).exists():
            InvestorProfileMerge.objects.create(investor=investor_profile,member=member_profile,relation=request.POST.get('relation',''),status='PENDING APPROVAL')
            response_data['message'] = 'Profile has been to added, Kindly refresh to check the status'
        else:
            response_data['message'] = 'Profile already exists'        
    except Exception as e:
        print(e)
        ErrorsModel.objects.create(error_caught_function=f'profile_merge_request - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)   
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def profile_merge_approved(request):
    response_data={}
    print(response_data,'==============================')
    try:
        approved_id = request.POST.get('approved_id','')
        if approved_id:
            ipm = InvestorProfileMerge.objects.get(id=approved_id)
            print(ipm)
            ipm.status='ACCEPTED'
            ipm.save()
            response_data['message'] = 'Successfully Approved'
        else:
            response_data['message'] = 'Error has occured'
    except Exception as e:
        print(e)
        ErrorsModel.objects.create(error_caught_function=f'profile_merge_approved - {sys.exc_info()[-1].tb_lineno}',error_message=e,error_caught_user=request.user)   
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getFormStatus(request,profile_id,depository_id):
    response_data = {}
    if RequestDetails.objects.filter(depository=Depository.objects.get(id=int(depository_id))).filter(investor__id=int(profile_id)).filter(is_active=True).exists():
        
        response_data['message'] = 200
    else:
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")    


def create_profile_form(request):
    response_data={}
    try:
        email_id = request.POST.get('emailid','')
        relation = request.POST.get('relation','')
        if email_id and relation:
            if not User.objects.filter(username=email_id).exists():
                user = User.objects.create(username= email_id,password=make_password(request.user.password),)
                try:
                    user_type, created = UserType.objects.update_or_create(
                    user=user,
                    defaults={
                        'user_type':UserTypeRole.objects.get(role='INVESTOR'),
                    })
                except Exception as e:
                    print(e)
                    user.delete()
                    response_data['message'] = 'It seems some error has occured while cteating profile'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")  
                try:  
                    if not InvestorProfileMerge.objects.filter(investor=request.user,member=user).exists() :
                        InvestorProfileMerge.objects.create(investor=request.user,member=user,relation=relation,status='ACCEPTED',permission='Read/Write')
                    else:                    
                        user.delete()
                        response_data['message'] = f'relation cannot be more than once'
                        return HttpResponse(json.dumps(response_data), content_type="application/json")  
                except Exception as e:
                    print(e,'2')
                    user.delete()
                    response_data['message'] = 'It seems some error has occured while adding profile'
                    return HttpResponse(json.dumps(response_data), content_type="application/json")  
                response_data['message'] = f'profile for {email_id} has been created successfully. Kindly visit profile page for more.'
                return HttpResponse(json.dumps(response_data), content_type="application/json")  
            else:
                response_data['message'] = f'User with 👉 {email_id} already exists'
                return HttpResponse(json.dumps(response_data), content_type="application/json")  
        else:
            response_data['message'] = 'Please fill all the details'
            return HttpResponse(json.dumps(response_data), content_type="application/json")  
    except Exception as e:
        print(e,'3')
        response_data['message'] = 'It seems some error has occured'
        return HttpResponse(json.dumps(response_data), content_type="application/json")  

# delete button  
def delete_credit_card(request):
    response_data = {}
    cc_id = request.POST.get('cc_id')
    try:
        if cc_id:
            try:
                credit_card = InvestorCreditCard.objects.get(id=cc_id)
                credit_card.delete()
                response_data['message'] = 'Successfully Deleted'
            except InvestorCreditCard.DoesNotExist:
                response_data['message'] = 'Credit card does not exist'
        else:
            response_data['message'] = 'It seems some error has occurred'
    except Exception as e:
        print(e)
        response_data['message'] = 'It seems some error has occurred'
    return redirect('investor_details')

def delete_bank(request):
    response_data = {}
    bank_id = request.POST.get('bank_id')
    try:
        if bank_id:
            try:
                bank = InvestorBankDetail.objects.get(id=bank_id)
                bank.delete()
                response_data['message'] = 'Successfully Deleted'
            except InvestorBankDetail.DoesNotExist:
                response_data['message'] = 'Bank does not exist'
        else:
            response_data['message'] = 'It seems some error has occurred'
    except Exception as e:
        print(e)
        response_data['message'] = 'It seems some error has occurred'
    return redirect('investor_details')

def delete_nominee(request):
    response_data = {}
    nominee_id = request.POST.get('nominee_id')
    try:
        if nominee_id:
            try:
                bank = InvestorNomineeDetail.objects.get(id=nominee_id)
                bank.delete()
                response_data['message'] = 'Successfully Deleted'
            except InvestorNomineeDetail.DoesNotExist:
                response_data['message'] = 'Bank does not exist'
        else:
            response_data['message'] = 'It seems some error has occurred'
    except Exception as e:
        print(e)
        response_data['message'] = 'It seems some error has occurred'
    return redirect('investor_details')

