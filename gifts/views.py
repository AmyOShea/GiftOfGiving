from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def gifts(request):
    """ View to render gifts template """
    return render(request, 'gifts/gifts.html')