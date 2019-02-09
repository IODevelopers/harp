try:
	from infi.systray import SysTrayIcon
	def web_link(systray):
	    print("Hello, World!")
	def say_bye(systray):
		print("Byee World!")
		exit()
	menu_options = (( "View Dashboard",None, web_link),)
	systray = SysTrayIcon("logo.ico", "Harp", menu_options,on_quit=say_bye)
	systray.start()
except Exception as e:
	print(e)