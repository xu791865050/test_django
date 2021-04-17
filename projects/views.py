from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from django.http import request
from django.views import View


def index(request):

    return HttpResponse('<h1>999999999999999999999999999999999</h1>')


class IndexView(View):

    def get(self, requset):

