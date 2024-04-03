from django.shortcuts import render

from .models import  Member

# Create your views here.
def about_team(request):
    members = Member.objects.all()

    return render(request, 'team/about_team.html', {'members': members})