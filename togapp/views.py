from django.shortcuts import render

from . import togboard

# Create your views here.

def index(request):
    if request.method == "POST":
        position = request.POST.get("pos")
        notation = request.POST.get("notation")
        tBoard = togboard.TogBoard(position)
        move = int(request.POST.get("move"))

        tBoard.makeMove(move)
        if not tBoard.finished:
            tBoard.makeRandomMove()

        html = tBoard.printPosition()
        position = tBoard.getPosition()
        turn = "White turn" if tBoard.fields[22] == 0 else "Black turn"
        moves = notation + tBoard.printNotation()

        return render(request, 'togapp/index.html', 
                      {'position': position, 'html': html, 'turn': turn, 'moves': moves})

    else:
        position = '9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,0,0,0,0,0'
        tBoard = togboard.TogBoard(position)
        html = tBoard.printPosition()
        turn = "White turn"
        moves = tBoard.printNotation()
        
        return render(request, 'togapp/index.html', 
                      {'position': position, 'html': html, 'turn': turn, 'moves': moves})
