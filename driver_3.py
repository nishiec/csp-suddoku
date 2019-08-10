#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

import sys
from heapq import heappush, heappop
from collections import deque

ROW = "ABCDEFGHI"
COL = "123456789"
emptytiles = []
domain = {}

#def test(board):
#    print(board)

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

#def fullBoard(board):
#    """Will be used to check that board is completed"""
#    for x in range(0,9):
#        for y in range(0,9):
#            if board[x][y]==0:
#                return False
#    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    setBoard(board) 
    for row in range(0,9):
        for col in range(0,9):
            if(board[(ROW[row] + COL[col])] != 0):
                #removes impossible values from domain 
                #of unassigned variables
                forwardchecking(domain, board, ROW[row], COL[col])
    mrv_tile = findMRV()
    print(mrv_tile)
#    print(emptytiles)
#    print(mrv_value[0])
#    print(mrv_value[1])
    for d in domain[mrv_tile]:
        if checkValid(board,mrv_tile[0], mrv_tile[1], d ):
            board[mrv_tile] = d
            for e in emptytiles:
                if e == mrv_tile:
                    emptytiles.remove(e)
            
    print_board(board)
        
    
    
   
    #forwardchecking(domain, board, mrv_value[0], mrv_value[1] )
                
                   
    
    return None
#    solved_board = board
#    return solved_board
    
def findMRV():
    mrv = None
    m = 10
    for e in emptytiles:
        length = len(domain[e])
        if length < m:
            m = length 
            mrv = e

    return mrv #return 
            

def setBoard(board):
    """Set up board and domain."""
    #set domain for empty and non empty tiles
    #empty tiles have initially a domain of all numbers
    for row in range(0,9):
        for col in range (0,9):
            if(board[(ROW[row] + COL[col])]== 0):
                domain[(ROW[row] + COL[col])] = set([1,2,3,4,5,6,7,8,9]) 
                emptytiles.append((ROW[row] + COL[col]))
            else:
                domain[(ROW[row] + COL[col])] = set( [board[(ROW[row] + COL[col])]]  )                
    #print(domain)

def forwardchecking(domain, board, letter, number):
    
    tile = board[letter+number]
    allconflictingtiles = set()
    rowtiles = []
    columntiles = [] 
    gridtiles = []    
    x = ord(letter) - ord('A') #distance away from A1
    y = ord(number) - ord('1') #B3 --> distance is (1,2)
    for col in COL:
        if col != number:
            rowtiles.append(letter+col) # all the other tiles in the row
            
    for row in ROW:
        if row != letter:
            columntiles.append(row+number) # all the other tiles in the column 
                    
    for row in range((x//3)*3, ((x//3)*3)+3): #all the other tiles in the grid section
        for col in range((y//3)*3, ((y//3)*3)+3):
            if row != x or col != y:
                gridtiles.append(chr(row + ord('A')) + chr(col + ord('1')))
    allconflictingtiles = set(rowtiles+columntiles+gridtiles)
    #allconflictingtiles.add(columntiles)
    #allconflictingtiles.add(gridtiles)
    #allconflictingtiles.add(rowtiles)
    
    for tiles in allconflictingtiles:
        if tile in domain[tiles]:
            domain[tiles].remove(tile) 
       
def checkValid(board, letter, number, dom):
    allconflictingtiles = set()
    rowtiles = []
    columntiles = [] 
    gridtiles = []    
    x = ord(letter) - ord('A') #distance away from A1
    y = ord(number) - ord('1') #B3 --> distance is (1,2)
    for col in COL:
        if col != number:
            rowtiles.append(letter+col) # all the other tiles in the row
            
    for row in ROW:
        if row != letter:
            columntiles.append(row+number) # all the other tiles in the column 
                    
    for row in range((x//3)*3, ((x//3)*3)+3): #all the other tiles in the grid section
        for col in range((y//3)*3, ((y//3)*3)+3):
            if row != x or col != y:
                gridtiles.append(chr(row + ord('A')) + chr(col + ord('1')))
    allconflictingtiles = set(rowtiles+columntiles+gridtiles)
    
    for t in allconflictingtiles:
        if board[t] == dom:
            print(board[t])
            return False 
    return True


    

if __name__ == '__main__':
#    #  Read boards from source.
#    src_filename = 'sudokus_start.txt'
#    try:
#        srcfile = open(src_filename, "r")
#        sudoku_list = srcfile.read()
#    except:
#        print("Error reading the sudoku file %s" % src_filename)
#        exit()
#
#    # Setup output file
#    out_filename = 'output.txt'
#    outfile = open(out_filename, "w")
#
#    # Solve each board using backtracking
#    for line in sudoku_list.split("\n"):
#
#        if len(line) < 9:
#            continue
#
#        # Parse boards to dict representation, scanning board L to R, Up to Down
#        board = { ROW[r] + COL[c]: int(line[9*r+c])
#                  for r in range(9) for c in range(9)}
#
#        # Print starting board. TODO: Comment this out when timing runs.
#        print_board(board)
#
#        # Solve with backtracking
#        solved_board = backtracking(board)
#
#        # Print solved board. TODO: Comment this out when timing runs.
#        print_board(solved_board)
#
#        # Write board to file
#        outfile.write(board_to_string(solved_board))
#        outfile.write('\n')
#
#    print("Finishing all boards in file.")
    
    
# individual testing (for my use)
    
    print("hi")
    
    for line in sys.argv[1].split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)


        backtracking(board)

        
        # Solve with backtracking
        #solved_board = backtracking(board)
    
    
    
    