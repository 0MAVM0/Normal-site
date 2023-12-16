from django.shortcuts import render


def games(request):
    return render(request, 'games/home.html')

def tetris(request):
    return render(request, 'games/tetris.html')
