import winsound
import time
from time import sleep
import os
from plyer import notification

def send_notification (title, message) :

    notification.notify (

        title = title,
        message = message,
        timeout = 17
	)

if __name__ == "__main__" :

    os.system ("cls")

    title = str (input ("\033[1;32mPlease enter a title for your task to be shown : "))
    waiting = float (input ("\033[1;31mWaiting Timer ( describe in seconds ) : "))
    lol = str (input (f"\033[1;35mShould this message be shown every {waiting} seconds for only today ( y for yes and n for no ) : "))
    message = str (input ("\033[1;33mMessage to be shown : "))

    print ("\n\n\033[1;34mOkay. Notification Set.")

    if lol.lower () == "n" :

        sleep (waiting)

        winsound.Beep (636, 600)

        send_notification (title.title (), message.title ())

    elif lol.lower () == "y" :

        kate = int (86400 / waiting)

        for i in range (1, (kate + 1)):

            sleep (waiting)

            winsound.Beep (636, 600)

            send_notification (title.title (), message.title ())
