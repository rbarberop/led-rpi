# 5 x 5 font definition

from .drawpixel import drawpixel

alphabet = {}

alphabet["a"] = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1]]
alphabet["b"] = [[1,1,1,0],[1,0,0,1],[1,1,1,0],[1,0,0,1],[1,1,1,0]]
alphabet["c"] = [[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[0,1,1,1]]
alphabet["d"] = [[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]]
alphabet["e"] = [[1,1,1,1],[1,0,0,0],[1,1,0,0],[1,0,0,0],[1,1,1,1]]
alphabet["f"] = [[1,1,1,1],[1,0,0,0],[1,1,1,0],[1,0,0,0],[1,0,0,0]]

def smallletter(pixel, character,col,color):
    for i in range(0,5):
      for j in range(0,4):
        if alphabet[character.lower()][i][j] == 1 :
            drawpixel(pixel, j+col, i+2, color)

