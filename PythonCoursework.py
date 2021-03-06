import ffmpeg
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle('Video/audio formats converter')
		self.setGeometry(300, 250, 300, 350)

		self.main_text = QtWidgets.QLabel(self)
		self.main_text.setText('You can convert\nVideo -> video\nAudio -> audio\nVideo -> audio | lose of video data\n' + 
						  'Audio -> video | videofile without video data\n\nAvailable in/out video formats\n' +
						  'asf | avi | mp4 | mpg | mov | m4v | wmv | dvd | mpeg\nAvailable in/out audio formats\n' +
						  'mp3 | wav | wma | aiff | au | m4a | mp4\n')
		self.main_text.move(25, 10)
		self.main_text.adjustSize()

		self.name_text = QtWidgets.QLabel(self)
		self.iextension_text = QtWidgets.QLabel(self)
		self.oextension_text = QtWidgets.QLabel(self)
		
		self.format_array = ['asf', 'avi', 'mp4', 'mpg', 'mov', 'm4v', 'wmv', 'dvd', 'mpeg', 'mp3', 'wav', 'wma', 'aiff', 'au', 'm4a']
		self.name_line = QtWidgets.QLineEdit(self)
		self.iextension_cb = QtWidgets.QComboBox(self)
		self.oextension_cb = QtWidgets.QComboBox(self)
		self.iextension_cb.addItems(self.format_array)
		self.oextension_cb.addItems(self.format_array)

		self.name_line.hide()
		self.iextension_cb.hide()
		self.oextension_cb.hide()

		self.btn1 = QtWidgets.QPushButton(self)
		self.btn1.move(50, 150)
		self.btn1.setText('Single file conversion')
		self.btn1.setFixedWidth(200)
		
		self.btn2 = QtWidgets.QPushButton(self)
		self.btn2.move(50, 190)
		self.btn2.setText('Folder files conversion')
		self.btn2.setFixedWidth(200)

		self.btn3 = QtWidgets.QPushButton(self)
		self.btn3.hide()
		self.btn3.move(50, 300)
		self.btn3.setText('CONVERT')
		self.btn3.setFixedWidth(200)

		self.input_filename = '0'
		self.input_extension = '0'
		self.output_extension = '0'
		self.ifilename = '0'
		self.ofilename = '0'

		self.btn1.clicked.connect(self.variant1)
		self.btn2.clicked.connect(self.variant2)

	def variant1(self):

		self.btn1.hide()
		self.btn2.hide()

		self.name_text.setText('Insert the name of file to convert:')
		self.name_text.move(25, 150)
		self.name_text.adjustSize()

		self.iextension_text.setText('Insert the extension of input file:\n')
		self.iextension_text.move(25, 200)
		self.iextension_text.adjustSize()

		self.oextension_text.setText('Insert the extension of output file:')
		self.oextension_text.move(25, 250)
		self.oextension_text.adjustSize()

		self.name_line.move(25, 165)
		self.name_line.resize(100, 20)
		self.name_line.show()

		self.iextension_cb.move(25, 215)
		self.iextension_cb.resize(100, 20)
		self.iextension_cb.show()

		self.oextension_cb.move(25, 265)
		self.oextension_cb.resize(100, 20)
		self.oextension_cb.show()

		self.btn3.show()
		self.btn3.clicked.connect(self.convert)

	def variant2(self):

		self.btn1.hide()
		self.btn2.hide()

		self.iextension_text.setText('Insert the extension of input files:\n')
		self.iextension_text.move(25, 150)
		self.iextension_text.adjustSize()

		self.oextension_text.setText('Insert the extension of output files:')
		self.oextension_text.move(25, 200)
		self.oextension_text.adjustSize()

		self.iextension_cb.move(25, 165)
		self.iextension_cb.resize(100, 20)
		self.iextension_cb.show()

		self.oextension_cb.move(25, 215)
		self.oextension_cb.resize(100, 20)
		self.oextension_cb.show()

		self.btn3.show()
		self.btn3.clicked.connect(self.folder_convert)

	#	Function of conversion
	def convert(self):
		self.input_filename = self.name_line.text()
		self.input_extension = self.iextension_cb.currentText()
		self.output_extension = self.oextension_cb.currentText()

		ifilename = self.input_filename + '.' + self.input_extension
		ofilename = self.input_filename + '.' + self.output_extension
		print('Starting of conversion ' + self.ifilename + '...')
		ffmpeg.input(ifilename).output(ofilename).run()
		print('End of conversion')
		exit()

	def folder_convert(self):
		self.input_extension = self.iextension_cb.currentText()
		self.output_extension = self.oextension_cb.currentText()
		for path, folder, files in os.walk(os.getcwd()):
			for file in files:
				if file.endswith(self.input_extension):
					ffmpeg.input(file).output(str(file).split('.')[0] + '.' + self.output_extension).run()
				else: 
					pass
		exit()

def application():
	app = QApplication(sys.argv)
	window = Window()

	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
    application()