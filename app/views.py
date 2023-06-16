from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from app.models import *


import csv

def bank_upload(file_path):
    a='C:\\Users\\nirak\\OneDrive\\Desktop\\REST-API\\rest_api\\Scripts\\project5\\bank.csv'
    with open(a,'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)
        for i in csv_data:
            bn=i[0].strip()
            isinstance=bank(bankname=bn)
            isinstance.save()
        return HttpResponse('successfully saved all data')
def branch_upload(file_path):
    a='C:\\Users\\nirak\\OneDrive\\Desktop\\REST-API\\rest_api\\Scripts\\project5\\branch1.csv'
    with open(a ,'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)
        for i in csv_data:
            bankname = i[0]
            
            bo = bank.objects.filter(bankname=bankname)[0]
            instance = branch(
                    bankname=bo,            
                      
                    ifsc = i[1],
                    branch = i[2],
                    address =i[3],
                    contact=i[4],
                    city = i[5],
                    district = i[6],
                    state = i[7],)
                                  
            instance.save()


       

        return HttpResponse('successfull upload all data to your bank data base')

def display(request):
    BO=branch.objects.all()
    d = {'BO': BO}
    return render(request, 'display.html',d)