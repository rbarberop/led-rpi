# 5 x 5 font definition

from .tomatrix import tomatrix

a = [[0,1,1,1,0],[1,0,0,0,0,1],[1,1,1,1,1],[1,0,0,0,0,1],[1,0,0,0,0,1]]

def letter(character,col,color):
    for i in range(col, col+5):
        if a[1][i] == 0 :
            pixel(tomatrix(i,2))=(0,0,0)
        else:
            pixel(tomatrix(i,2))=color
