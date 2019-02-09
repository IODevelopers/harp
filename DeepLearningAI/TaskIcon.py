try:
	from infi.systray import SysTrayIcon
	def say_hello(systray):
	    print("Hello, World!")
	def say_bye(systray):
		print("Byee World!")
		exit()
	menu_options = (( None,None, say_hello),)
	systray = SysTrayIcon("logo.ico", "Harp", menu_options,on_quit=say_bye)
	systray.start()
	while True:
		print("Annoying")
except Exception as e:
	print(e)