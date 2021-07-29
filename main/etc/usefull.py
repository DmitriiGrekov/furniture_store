from ..models import UsefullInfo 
from company.models import RubricCompany 

def usefullinfo(request):
    return {'info': UsefullInfo.objects.first(), 'title_link': 'about', }

def get_rubric_company(request):
    return {'rubric_company': RubricCompany.objects.all()}

