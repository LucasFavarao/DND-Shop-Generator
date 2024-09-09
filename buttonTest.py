from django.shortcuts import render, redirect
from django.http import HttpResponse


def run_script(request):
    if request.method=="POST":
        print("")