from PyQt5 import Qt
import sys
app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(app, Qt.QIcon(r"C:\Users\Sanket's_PC\Desktop\Project\Resource"))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')


