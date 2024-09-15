from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Depository,RequestDetails,InvestorIdentityDetails,InvestorAddressDetails,InvestorBankDetails,InvestorAdditionalKycDetails,InvestorNomineeDetails
from core.models import ErrorsModel
import sys,json
# Create your views here.


