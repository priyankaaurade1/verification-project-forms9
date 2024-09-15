from django import template
import base64
from math import ceil
from depository.models import Depository,RequestDetails
from core.models import InvestorDocumentManager
from datetime import datetime, timedelta
from investor.models import InvestorProfileMerge,InvestorDetail,InvestorNomineeDetail,InvestorBankDetail,DocumentUpload,Document
from investor.crypto import decrypt_image

register = template.Library()

mask_variable = 'x'

# Used for masking template functions


@register.filter
def as_chunk(lst, chunk_size):
    limit = ceil(len(lst) / chunk_size)
    for idx in range(limit):
        yield lst[chunk_size * idx : chunk_size * (idx + 1)]


def masker(length):
    s = ''
    for i in range(length):
        s = s + mask_variable
    return s

@register.filter
def encode_base64(value):
    return base64.b64encode(value).decode()

@register.filter
def checkFormStatus(value,arg):
    if RequestDetails.objects.filter(depository=Depository.objects.get(id=int(value))).filter(investor__id=int(arg)).filter(is_active=True).exists():
        return True
    else:
        return False

@register.filter
def splitString(value,arg):
    try:
        return value.split(',')[arg]
    except Exception as e:
        return ''
    
@register.filter
def queryfilter(value,arg):
    try:
        val1, val2 = arg.split(',')
        bank_detail = value.bank_details.all()[int(val1)]
        return getattr(bank_detail, val2)
    except Exception as e:
        return ''
    
@register.filter
def queryfilter1(value,arg):
    try:
        val1, val2 = arg.split(',')
        cc_detail = value.cc_details.all()[int(val1)]
        return getattr(cc_detail, val2)
    except Exception as e:
        return ''
    

    
@register.filter
def add_days(value, days):
    if datetime.strptime(value, '%Y-%m-%d').date() > (datetime.now() + timedelta(days=days)).date():
        return True
    else:
        return False


@register.filter
def merge_approvals_filter(requested_user):
    return InvestorProfileMerge.objects.filter(member=requested_user)
    
@register.filter
def checkDate(value):
    if datetime.now().date() <= datetime.strptime(value, '%Y-%m-%d').date() <= (datetime.now() + timedelta(days=7)).date():
        return True
    else:
        return False

@register.filter
def maskEmailID(value):
    user_name = value.split('@')
    domain_name = user_name[1].split('.')
    masked_email = user_name[0][0] + masker(len(user_name[0][1:-1])) + user_name[0][-1] + '@' + domain_name[0][0] + masker(len(domain_name[0][1:-1])) + domain_name[0][-1] + "." + domain_name[1]
    return masked_email

# Works only with the d/m/Y format i.e. SHORT_DATE_FORMAT (es Locale)
@register.filter
def maskDate(value):
    date = datetime.strptime(value, '%d/%m/%Y')
    split_date_list = []
    split_date_list.extend([str(date.strftime('%d')), str(date.strftime('%m')), str(date.year)])
    for i in split_date_list:
        if len(i) == 2:
            x = i[0] + mask_variable
            split_date_list = list(map(lambda z: z.replace(i, x), split_date_list))
        elif len(i) > 2:
            x = i[0] + masker(len(i[1:-1])) + i[-1]
            split_date_list = list(map(lambda z: z.replace(i, x), split_date_list))
    masked_date = '/'.join(split_date_list)
    return masked_date

# Default mask filter. Should be used for all, except Email and Date
@register.filter
def maskString(value):
    if value == "":
        return ""
    split_string = value.split(' ')
    masked_string_list = []
    for i in split_string:
        i = i[0] + masker(len(i[1:-1])) + i[-1]
        masked_string_list.append(i)
    masked_string = ' '.join(masked_string_list)
    return masked_string 

import datetime
@register.filter
def dateFormat(value):
    date = datetime.date.strftime(value, "%d/%m/%Y")
    return date


@register.filter
def filter_bank_details(requested_user):
    try:
        return [InvestorBankDetail.objects.get(document_data__user=requested_user, set_as_primary=True)]
    except InvestorBankDetail.DoesNotExist:
        return InvestorBankDetail.objects.filter(document_data__user=requested_user)[:1]

@register.filter
def filter_nominee_details(requested_user):
    try:
        return [InvestorNomineeDetail.objects.get(document_data__user=requested_user, set_as_primary=True)]
    except InvestorNomineeDetail.DoesNotExist:
        return InvestorNomineeDetail.objects.filter(document_data__user=requested_user)[:1]

@register.filter
def image_filter(requested_user):
    try:
        doc = DocumentUpload.objects.filter(user=requested_user).first()
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
        return upload_dict.items()
    except Exception as e:
        return []

@register.filter
def image_choices(image):
    return [c[0] for c in Document.document.field.choices]

@register.filter
def image_choices1(image_type):
    allowed_choices = ['AADHAR CARD SELF', 'AADHAR CARD FATHER', 'AADHAR CARD MOTHER', 'AADHAR CARD SPOUSE', 'PAN CARD SELF', 'PAN CARD FATHER', 'PAN CARD MOTHER', 'PAN CARD SPOUSE', 'PASSPORT', 'VISA', 'OVERSEA TAX', 'UTILITY BILL', 'BANK PASSBOOK', 'BANK STATEMENT', 'BANK CHEQUE', 'CREDIT CARD']
    return image_type in allowed_choices
