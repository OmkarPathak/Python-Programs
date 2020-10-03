print("run using the command pythonw pythonnotification.py if you havent")
import time
from plyer import notification
if __name__=="__main__":
    while(True):
        notification.notify(
        title = "please drink water",
        message = "drink water to keep yourself hydrated",
        app_icon="", #if you have a icon file for water glass image paste its path here
        timeout=10
        )
        time.sleep(60*60)

    
