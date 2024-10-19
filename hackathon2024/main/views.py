from django.shortcuts import render

# Create your views here.
def portfolio_page(request):
    return render(request, "main/portfolio.html")

def home(request):
    return render(request, "main/home.html")