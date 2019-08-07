from PyQt5 import Qt
import sys
app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(app, Qt.QIcon("C:\Users\logo2.jpg"))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')

