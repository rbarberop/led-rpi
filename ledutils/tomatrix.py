# This function translates a set of coordinates
# (x,y) to an integer position in the LED matrix
#
# Inputs: 
# x - column (0 - 31)
# y - row (0 - 7)
#
# Output:
# An nteger with the position of that LED

def tomatrix(col, row):
    return(((8 * col) + row) + (col % 2 * (7 - (2 * row))))