from datetime import datetime
from threading import Timer
from plyer import notification
import sys
import platform

def getReminder(self):
    x=datetime.today()
    y = (x + timedelta(days=1)).replace(hour=11, minute=0, second=0)
    delta_t=y-x

    secs=delta_t.seconds+1

    def get_Notify():
        SearchMe=str(platform.platform())
        d="Windows-10"
        a=SearchMe.startswith(d)
        
        if a == True:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("SPC","Today is your schedule!!!")
        else:

























            from PyQt5 import Qt
            import sys
            app = Qt.QApplication(sys.argv)
            systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon(r'C:\Users\logo2.bmp'))
            systemtray_icon.show()
            systemtray_icon.showMessage('Title', 'Content')
    
    t = Timer(secs, get_Notify)
    t.start()

    get_Notify(SearchMe)

getReminder()