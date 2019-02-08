from win10toast import ToastNotifier
def Notify(MessageTitle,MessageBody):
	toaster = ToastNotifier()
	MessageTitle=sys.argv[1]
	MessageBody=sys.argv[2]
	toaster.show_toast(MessageTitle,
	                   MessageBody,
	                   icon_path="logo.ico",
	                   duration=10,threaded=True)
	from playsound import playsound
	playsound('Notification.mp3')
	while toaster.notification_active(): time.sleep(0.1)