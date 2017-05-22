#!/usr/bin/env python

# Author: OMKAR PATHAK

# This application was developed as I cannot remember for birthdays efficiently.
# This app helps me remind birthdays and notifies me on their birthdays.

# To store birthdays ceate a file 'reminder.data' and store birthdays in this format:
# MonthDay Name Surname

# Copy the python file to /bin:
#   sudo cp -i /path/to/your_script.py /bin
#   (your_script.py should be executable)
# Add A New Cron Job:
#   sudo crontab -e
# Scroll to the bottom and add the following line (after all the #'s):
#   @reboot python /bin/your_script.py &
# And Reboot to check if the script is working

# Or simply search for 'Startup applications' and add you script there

import time
import os

birthdayFile = '/home/omkarpathak/Documents/GITs/Python-Programs/Programs/reminder.data'
myFilePath = 'python /home/omkarpathak/Documents/GITs/Python-Programs/Programs/P63_ReminderApplication.py'

def checkStartupScript():
    ''' This function ensures that our application executes on every startup '''
    flag = 0
    fileName = open('/etc/rc.local', 'r')
    for line in fileName:
        if myFilePath in line:
            flag =1
    if flag == 0:
        addToStartup()
    fileName.close()

def addToStartup():
    fileName = open('/etc/rc.local', 'a')
    fileName.write(myFilePath + '\n')
    fileName.close()

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
            os.system('notify-send "Birthdays Today: ' + line[1] + ' ' + line[2] + '"')
    if flag == 0:
            os.system('notify-send "No Birthdays Today!"')

if __name__ == '__main__':
    checkStartupScript()
    checkTodaysBirthdays()
