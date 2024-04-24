# Keylogger-in-Python
  - Runs silently in the background, 
  - Auto-Launch on restart
  - record **key press** logs
  - send those logs by mail (in every 1 hour)


<br>


to create exe of py file run command
pyinstaller --noconsole --onefile Keylogger.py

to auto launch exe on computer start
paste exe file at location C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp


To stop execution of this Key-Logger 
  1. go to task manager (ctrl + shift + esc)  and End process with name keylogger
  2. delete Keylogger file from Startup path (so that automatically not launch on restart)
