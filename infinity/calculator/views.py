from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'calculator/home.html')


def blank_board(request):
    return render(request, 'calculator/board.html')


def sc(request):
    return render(request, 'calculator/sc.html')