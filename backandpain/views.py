from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def questionaire(request):
	return render(request, 'questionaire.html')