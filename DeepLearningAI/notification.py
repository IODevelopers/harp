from win10toast import ToastNotifier
import time
import sys
toaster = ToastNotifier()
MessageTitle=sys.argv[1]
MessageBody=sys.argv[2]
toaster.show_toast(MessageTitle,
                   MessageBody,
                   icon_path="logo.ico",
                   duration=10,threaded=True)
while toaster.notification_active(): time.sleep(0.1)