from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def profile(request):
    """ View to render users profile """
    return render(request, 'profiles/profile.html')