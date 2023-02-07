from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget
import sys
from download_thread import DownloadThread

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Descargador de videos")
        self.setGeometry(100, 100, 500, 500)

        self.label = QLabel("Introduce el enlace m3u8:", self)
        self.label.move(20, 20)
        self.label.resize(150, 40)

        self.textbox = QLineEdit(self)
        self.textbox.move(180, 20)
        self.textbox.resize(200, 40)

        self.download_button = QPushButton("Descargar", self)
        self.download_button.move(200, 80)
        self.download_button.clicked.connect(self.start_download)

        self.stop_button = QPushButton("Parar", self)
        self.stop_button.move(300, 80)
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_download)

        self.list = QListWidget(self)
        self.list.move(20, 150)
        self.list.resize(450, 300)

        self.download_thread = None

    def start_download(self):
        self.download_thread = DownloadThread(self.textbox.text(), "video.mp4")
        self.download_thread.progress_signal.connect(self.update_list)
        self.download_thread.start()
        self.download_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_download(self):
        self.download_thread.terminate()
        self.download_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_list(self, message):
        self.list.addItem(message)

