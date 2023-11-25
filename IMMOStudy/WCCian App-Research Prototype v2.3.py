import webbrowser
import time

def program():
 Student = input('Enter Student Full Name \n')
 print("Greetings WCCStudent: " + Student); 
 print("loading..."); 
 time.sleep(5)
 program2()

def program2():
 print("opening student guide...")
 time.sleep(5);  
 webbrowser.open("https://justheowl.github.io/wcc-off.github.io/"); 

program()