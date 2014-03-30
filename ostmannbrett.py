from subprocess import call 
import curses
class OstmannBrett:

   def convert(self, input):
      return "clips/"+input + ".mp3"

continueReading = True
ostmann = OstmannBrett()
stdscr = curses.initscr()
while(continueReading):
    inputA = chr(stdscr.getch())
    if(inputA == 'Q'  or inputA == 'q'):
       curses.endwin()
       continueReading = False
    else:
       call(["mpg123", ostmann.convert(inputA)])
