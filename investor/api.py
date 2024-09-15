from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import Group, Permission,User
from core.models import ErrorsModel
from .serializer import RequestDetailsSearializer,IdentityDetailsSearializer,AddressDetailsSearializer,BankDetailsSearializer,AdditionalKycDetailsSearializer,NomineeDetailsSearializer,AccountTypeSearializer,GaurdianDetailsSearializer,DeclarationSearializer,StandingInstructionsSearializer,InvestorSmsAlertSearializer,InvestorOtherDetailsSearializer,UserEmailIdSearializer
from depository.models import Depository,RequestDetails,InvestorIdentityDetails,InvestorAddressDetails,InvestorBankDetails,InvestorAdditionalKycDetails,InvestorNomineeDetails,InvestorAccountType,InvestorGaurdianDetails,InvestorDeclaration,InvestorStandingInstructions,InvestorSmsAlert,InvestorOtherDetails
import sys

## API to view Request:

@login_required(login_url='/login') 
@api_view(['GET'])
def requestDetailsAPI(request,pk):
    try:
        requestDetail = RequestDetails.objects.get(id=int(pk))
        serializer = RequestDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        pass

# InvestorIdentityDetails


@login_required(login_url='/login') 
@api_view(['GET'])
def identityDetailsAPI(request,pk):
    try:
        if pk==9999: # To get latest formData
            requestDetail = InvestorIdentityDetails.objects.filter(request_no__investor=request.user)[0]
            print(requestDetail)
        else:
            requestDetail = InvestorIdentityDetails.objects.filter(request_no__id=int(pk)).first()
        serializer = IdentityDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
        


# InvestorAddressDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def addressDetailsAPI(request,pk):
    try:
        if pk==9999:
            try:
                print(RequestDetails.objects.filter(investor=request.user).latest('id'))
            
                requestDetail = InvestorAddressDetails.objects.filter(request_no__investor=request.user)[0]
            except Exception as e:
                print(e)
                # print(requestDetail)
        else:
            requestDetail = InvestorAddressDetails.objects.filter(request_no__id=int(pk)).first()
        serializer = AddressDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorBankDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def bankDetailsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorBankDetails.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorBankDetails.objects.filter(request_no__id=int(pk)).first()
        
        serializer = BankDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorAdditionalKycDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def additionalKycDetailsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorAdditionalKycDetails.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorAdditionalKycDetails.objects.filter(request_no__id=int(pk)).first()  
        serializer = AdditionalKycDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorNomineeDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def nomineeDetailsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorNomineeDetails.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorNomineeDetails.objects.filter(request_no__id=int(pk)).first()
          
        serializer = NomineeDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorAccountType
@login_required(login_url='/login') 
@api_view(['GET'])
def accountTypeAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorAccountType.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorAccountType.objects.filter(request_no__id=int(pk)).first()
        serializer = AccountTypeSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorGaurdianDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def gaurdianDetailsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorGaurdianDetails.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorGaurdianDetails.objects.filter(request_no__id=int(pk)).first()

        serializer = GaurdianDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorDeclaration
@login_required(login_url='/login') 
@api_view(['GET'])
def declarationAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorDeclaration.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorDeclaration.objects.filter(request_no__id=int(pk)).first()
        serializer = DeclarationSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorStandingInstructions
@login_required(login_url='/login') 
@api_view(['GET'])
def standingInstructionsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorStandingInstructions.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorStandingInstructions.objects.filter(request_no__id=int(pk)).first()
        serializer = StandingInstructionsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorSmsAlert
@login_required(login_url='/login') 
@api_view(['GET'])
def smsAlertAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorSmsAlert.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorSmsAlert.objects.filter(request_no__id=int(pk)).first()

        serializer = InvestorSmsAlertSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# InvestorOtherDetails
@login_required(login_url='/login') 
@api_view(['GET'])
def otherDetailsAPI(request,pk):
    try:
        if pk==9999:
            requestDetail = InvestorOtherDetails.objects.filter(request_no__investor=request.user)[0]
        else:
            requestDetail = InvestorOtherDetails.objects.filter(request_no__id=int(pk)).fist()
        serializer = InvestorOtherDetailsSearializer(requestDetail)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    


# User Api

@login_required(login_url='/login') 
@api_view(['GET'])
def userEmailIdApi(request):
    try:       
        userDetail = User.objects.all()
        serializer = UserEmailIdSearializer(userDetail,many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
