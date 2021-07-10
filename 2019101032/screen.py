from game import *
from values import *
from colorama import init as coloramaInit, Fore, Style, Back
import numpy as np
class screen(game):
    def __init__(self):
        coloramaInit()
        super().__init__()
        self.grid = []
        self.colorgrid = [] 
    def createScreen(self):
        self.grid = []
        self.colorgrid = []
        row = []
        for i in range(width):
            row.append("=")
        self.grid.append(row)
        row = []
        for i in range(1,height-1):
            for j in range(width):
                if(j == 0 or j == width-1):
                    row.append("=")
                else:
                    row.append(" ")
            self.grid.append(row)
            row = []

        for i in range(width):
            row.append("=")
        self.grid.append(row)
        row = []
        for i in range(height):
            for j in range(width):
                row.append(Fore.BLACK+ Back.WHITE)
            self.colorgrid.append(row)
            row = []
    def printScreen(self):
        
        for i in range(height):
            for j in range(width):
                print(self.colorgrid[i][j] + self.grid[i][j], end="")
                print(Style.RESET_ALL,end="")
            print()
        
