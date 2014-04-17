from subprocess import Popen 
import curses
import sys

class OstmannBrett:

   def convert(self, input):
      return "clips/"+input + ".mp3"
   
   def runMusic(self,input):
     return Popen(["mpg123", self.convert(input)])

continueReading = True
laufende = [None, None, None]
counter = 0

def f(x):
    ostmann = OstmannBrett()
    return ostmann.runMusic(x)

stdscr = curses.initscr()
while(continueReading):
    inputA = chr(stdscr.getch())
    if(inputA == 'Q'):
       laufende[0].terminate()
       laufende[1].terminate()
       laufende[2].terminate()
       curses.endwin()
       continueReading = False
    else:
       if (laufende[counter] != None):
           laufende[counter].terminate() 
       laufende[counter] = f(inputA)
       counter = (counter + 1) % 3
