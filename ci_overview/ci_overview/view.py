from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    return HttpResponse("Hello World")


def result(request):
    context = {}
    template_html = 'test.html'
    context['result'] = 'This is hello in view.py!'
    result_folder = '/home/python_proj/Django/ci_overview/ci_overview/templates'
    get_temp_command = "ls -lt " + result_folder + " |sed -n '2p' |awk '{print $NF}'" 
    result_html = os.popen(get_temp_command).read().strip('\r\n')
    return render(request, result_html, context)

