ostmannbrett
============
- works only for linux or unix
- install mpg123 => sudo apt-get install mpg123
- create directory clips => mkdir clips
- in clips/ you need a file for each possible key (mapping to clip files is case-sensitive)
-- example clips/A.mp3 will be played if you press A
-- example clips/a.mp3 will be played if you press a 
- Q and q will terminate the ostmannbrett
- start program: python ostmannbrett.py


trouble shooting
- if you kill the programm with CTRL+Q you need to call reset in terminal
