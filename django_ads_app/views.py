from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import openpyxl

# Create your views here.
def ret_str(request):
    return HttpResponse('111')

def read_txt(request):
    with open("requirements.txt") as file:
        data = file.readlines()
    return HttpResponse(data)

def ret_json(request):
    json = {"word": "hi"}
    return JsonResponse(data=json, safe=False)

def ret_json_file(request):
    with open("data.json") as file:
        j_d = json.load(file)
    return JsonResponse(data=j_d, safe=False)

def ret_xl_file(request):
    data = []
    workbook = openpyxl.load_workbook("data.xlsx")
    worksheet = workbook['Sheet1']
    for row in worksheet.iter_rows(values_only=True):
        for cell_v in row:
            data.append(cell_v)
    return HttpResponse(data)

def ret_html(request):
    return render(request, 'home.html',
                  context={})

