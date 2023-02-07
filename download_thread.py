from PyQt5.QtCore import QThread, pyqtSignal
import subprocess

class DownloadThread(QThread):
    progress_signal = pyqtSignal(str)

    def __init__(self, url, output_file):
        QThread.__init__(self)
        self.url = url
        self.output_file = output_file

    def run(self):
        download_command = f"ffmpeg -i {self.url} -c copy {self.output_file}"
        subprocess.run(download_command, shell=True)
