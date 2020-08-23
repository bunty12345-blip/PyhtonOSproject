import pyttsx3
import datetime as dt
import datetime
import os
import webbrowser
import cv2
import smtplib
import time
import imaplib
import email 
e = datetime.datetime.now()
pyttsx3.speak("Hello user Welcome to world of programs\n")
print("Hello user how can we help you ??\n")
print()

pyttsx3.speak("Choose from below any one of the options\n")
print("Choose from below any one of the options\n")

while True :
     print("1. fetch emails from gmail using python script\n")
     print("2. python code to show current date and time \n")
     print("3. python code to display current month calendar along with date ,day and year \n")
     print("4. show the device current location \n")
     print("5. python code to log into facebook account \n")
     print("6. python code to open webcam\n")
     print("7. Nothing\n")
     print()
     
     pyttsx3.speak("Please type your desired requirement\n")
     print("Please type your desired requirement", end = ' ')

     req = input()

     if ("1" in req ) or ("1." in req):
        #send emails from gmail using python script
        pyttsx3.speak("This code will send emails from your gmail account using python script")
        # Python code to illustrate Sending mail from your Gmail account  
        import smtplib 
        global s
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
  
        # Authentication 
        s.login("buntydarkcoderknight@gmail.com","xxxxxxxxxxxxxxxxxxx") 
  
        # message to be sent 
        message = "Hi, this is my first test mail send from hacker"
  
        # sending the mail 
        s.sendmail("buntydarkcoderknight@gmail.com", "jonathanjamesfamehunter007@gmail.com", message) 
  
        # terminating the session 
        s.quit()         
     elif ("2" in req) or ("2." in req):
       #python code to show current date and time
       pyttsx3.speak("This code will print and speak about the current date and time according to the device timezone")
       import datetime
       import pytz
       # using now() to get current time  
       current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
    
       # printing current time in india  
       print ("The current date and time in india is : ")  
       print (current_time)   
       pyttsx3.speak("The current  date and time in india  is :")
       pyttsx3.speak(current_time)
       
     elif ("3" in req) or ("3." in req):
       #python code to display current month calendar along with date ,day and year
       pyttsx3.speak("This code will display current month calender along with day, date and year")       
       import calendar
       # Create a plain text calendar
       c = calendar.TextCalendar(calendar.THURSDAY)
       str = c.formatmonth(2025, 1, 0, 0)
       print(str)

       # Create an HTML formatted calendar
       hc = calendar.HTMLCalendar(calendar.THURSDAY)
       str = hc.formatmonth(2025, 1)
       print(str)
       # loop over the days of a month
       # zeroes indicate that the day of the week is in a next month or overlapping month
       for i in c.itermonthdays(2025, 4):
             print(i)

             # The calendar can give info based on local such a names of days and months (full and abbreviated forms)
             for name in calendar.month_name:
                print(name)
             for day in calendar.day_name:
                print(day)
             # calculate days based on a rule: For instance an audit day on the second Monday of every month
             # Figure out what days that would be for each month, we can use the script as shown here
             for month in range(1, 13):
		     # It retrieves a list of weeks that represent the month
                mycal = calendar.monthcalendar(2025, month)
		     # The first MONDAY has to be within the first two weeks
                week1 = mycal[0]
                week2 = mycal[1]
                if week1[calendar.MONDAY] != 0:
                       auditday = week1[calendar.MONDAY]
                else:
                # if the first MONDAY isn't in the first week, it must be in the second week
        	           auditday = week2[calendar.MONDAY]
       print ("%10s %2d" % (calendar.month_name[month], auditday))
     elif ("4" in req) or ("4." in req):
        pyttsx3.speak("This code will show the current device location")
        #show the device current location
        import requests
        res = requests.get('https://ipinfo.io')
        data = res.json()
        city = data['city']
        location = data['loc'].split('.')
        latitude = location[0]
        longitude = location[1]
        print("Latitude :", latitude)
        print("Longitude :",longitude)
        print("City :",city)
        pyttsx3.speak("Latitude")
        pyttsx3.speak(latitude)
        pyttsx3.speak("Longitude")
        pyttsx3.speak(longitude)
        pyttsx3.speak("City :")
        pyttsx3.speak(city)
        
     elif ("5" in req) or ("5." in req):
        #python code to log into facebook account
        pyttsx3.speak("This code will ask you to enter email id and password and get you directed to login into facebook account")
        from selenium import webdriver 
        from time import sleep 
        from webdriver_manager.chrome import ChromeDriverManager 
        from selenium.webdriver.chrome.options import Options  
  
        usr=input('Enter Email Id:')  
        #pwd=input('Enter Password:')  
        
        from getpass import getpass 
        pwd = getpass('Enter Password:')  
  
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.get('https://www.facebook.com/') 
        print ("Opened facebook") 
        sleep(1) 
  
        username_box = driver.find_element_by_id('email') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(1) 
  
        password_box = driver.find_element_by_id('pass') 
        password_box.send_keys(pwd) 
        print ("Password entered") 
  
        login_box = driver.find_element_by_id('loginbutton') 
        login_box.click() 
  
        print ("Done") 
        input('Press anything to quit') 
        driver.quit() 
        print("Finished")     

     elif ("6" in req) or ("6." in req):
        pyttsx3.speak("This code will take the photograph of your face")
        #python code to open webcam
        import cv2
        import sys

        
        video_capture = cv2.VideoCapture(0)

        while True:
               # Capture frame-by-frame
               ret, frame = video_capture.read()

               gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
               # Display the resulting frame
               cv2.imshow('Video', frame)

               if cv2.waitKey(1):
                   break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()        

     elif ("7" in req) or ("7." in req):
        pyttsx3.speak("Thank you have a nice day !!")
        break
        