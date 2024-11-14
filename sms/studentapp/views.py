
from django.shortcuts import render
def homepage(request):
    return render(request ,'HomePage.html')
def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')
