from subprocess import call 
import curses
import threading

class OstmannBrett:

   def convert(self, input):
      return "clips/"+input + ".mp3"
   
   def foo(self):
      print "foo"

   def runMusic(self,input):
     print "HU"
     call(["mpg123", self.convert(input)])



continueReading = True

def f(x):
    ostmann = OstmannBrett()
    ostmann.runMusic(x)

stdscr = curses.initscr()
while(continueReading):
    inputA = chr(stdscr.getch())
    if(inputA == 'Q'  or inputA == 'q'):
       curses.endwin()
       continueReading = False
    else:
       thr = threading.Thread(target=f, args=(inputA), kwargs={})
       thr.start()
