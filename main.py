import sys

import PyQt5
from PyQt5.QtWidgets import *

import mainwindow_auto

# create class for out Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
	# access variables inside the UI's file

	def pressedOnButton(self):
		print("Pressed button on")

	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI File

		self.pushButton.clicked.connect(lambda: self.pressedOnButton())

# I feel better having one of these
def main():
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	#without this, the script exits immediately
	sys.exit(app.exec_())

# python bit to figure how who started this
if __name__ == "__main__":
	main()
