from win10toast import ToastNotifier
import time
def Notify(MessageTitle,MessageBody):
	toaster = ToastNotifier()
	toaster.show_toast(MessageTitle,
	                   MessageBody,
	                   icon_path="logo.ico",
	                   duration=3,threaded=True)
	from playsound import playsound
	playsound('Notification.mp3')
	while toaster.notification_active(): time.sleep(0.1)