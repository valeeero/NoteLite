from django.http import HttpResponse
from django.shortcuts import render
from notes.utils import generate_password as gen_pass


def hello_world(request):
    return HttpResponse('<h1>Hello</h1>')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)
