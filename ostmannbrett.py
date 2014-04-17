from subprocess import call 
import curses
class OstmannBrett:

   def convert(self, input):
      return "clips/"+input + ".mp3"
   
   def runMusic(self,input):
     call(["mpg123", self.convert(input)])

continueReading = True
ostmann = OstmannBrett()
stdscr = curses.initscr()
while(continueReading):
    inputA = chr(stdscr.getch())
    if(inputA == 'Q'  or inputA == 'q'):
       curses.endwin()
       continueReading = False
    else:
       ostmann.runMusic(inputA)
