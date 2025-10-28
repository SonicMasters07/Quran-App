from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QPushButton, QCheckBox, QLineEdit
import sys
import requests
import os

# Function to locate resources (works in .exe too)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Used when running from PyInstaller EXE
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# Add local VLC folder path
vlc_path = resource_path("vlc")
if os.path.exists(vlc_path):
    os.add_dll_directory(vlc_path)

import vlc

def resource_path(relative_path):
    import sys, os
    #for icon
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


class Ayah(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quran App")

        #for icon
        icon_path = resource_path("quran.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.setGeometry(500, 300, 950, 450)
        self.setStyleSheet("""
            QMainWindow {
            border-radius: 12px;
            }
        """)

        self.label1 = QLabel("Arabic", self)
        self.label2 = QLabel("English", self)
        self.label3 = QLabel("Urdu", self)
        self.btn = QPushButton("Search", self)
        self.bar = QLineEdit(self)
        self.check = QCheckBox("Audio", self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.label2, 1, 0)
        self.layout.addWidget(self.label3, 2, 0)
        self.layout.addWidget(self.btn, 4, 1)
        self.layout.addWidget(self.bar, 4, 0)
        self.layout.addWidget(self.check, 3, 1)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        central_widget.setAutoFillBackground(True)
        central_widget.setStyleSheet("background-color: #F6F5FC; border-radius: 12px;")
        self.setCentralWidget(central_widget)

        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
        QLabel {
            background-color: #F9F9FB;        /* soft white-gray background */
            color: #222;                      /* dark gray text for good contrast */
            font-family: 'Segoe UI', Arial;   /* modern, readable font */
            font-size: 15px;
            font-weight: 500;
            padding: 8px 12px;                /* internal spacing */
            border-radius: 6px;               /* smooth rounded edges */
            border: 1px solid #D0D0D0;        /* subtle border */
        }
        """)
        self.btn.setMinimumSize(200, 40)
        self.bar.setMinimumSize(200, 40)
        self.bar.setStyleSheet("""
        QLineEdit {
            background-color: #FFFFFF;         /* background color */
            color: #222222;                    /* text color */
            font-family: 'Segoe UI', Arial;
            font-size: 15px;
            font-weight: 500;
            padding: 6px 10px;                 /* inner spacing for text */
            border: 1px solid #B0B0B0;
            border-radius: 6px;
            selection-background-color: #A68EF7;  /* text highlight color */
            selection-color: white;               /* highlight text color */
        }
        QLineEdit:focus {
            border: 1px solid #8B6BF9;         /* highlight border when focused */
            background-color: #F8F6FF;
        }
        """)

        self.btn.setStyleSheet("""
        QPushButton {
            background-color: #8B6BF9;       /* soft purple base */
            color: white;                    /* white text */
            font-family: 'Segoe UI', Arial;
            font-size: 15px;
            font-weight: 600;
            padding: 8px 18px;               /* inner spacing */
            border: none;                    /* clean edge */
            border-radius: 6px;              /* rounded corners */
        }

        QPushButton:hover {
        background-color: qlineargradient(
        spread:pad, x1:0, y1:0, x2:0, y2:1,
        stop:0 #B09CFF, stop:1 #9B7FFF);
        }

        QPushButton:pressed {
            background-color: #6A4ED9;       /* darker shade when pressed */
        }

        QPushButton:disabled {
            background-color: #C8C8C8;       /* gray when disabled */
            color: #666666;
        }
        """)

        self.check.setStyleSheet("""
        QCheckBox {
            font-family: 'Segoe UI', Arial;
            font-size: 15px;
            font-weight: 500;
            color: #222;
            spacing: 8px; /* space between box and text */
        }

        /* Unchecked box */
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 4px;
            border: 2px solid #8B6BF9;
            background-color: #FFF;
        }

        /* Hover effect */
        QCheckBox::indicator:hover {
            border: 2px solid #A68EF7;
        }

        /* Checked box */
        QCheckBox::indicator:checked {
            background-color: #8B6BF9;
            border: 2px solid #8B6BF9;
            image: url(); /* no icon */
        }

        /* Optional: disabled state */
        QCheckBox::indicator:disabled {
            background-color: #E0E0E0;
            border: 2px solid #C0C0C0;
        }
        """)

        self.bar.setPlaceholderText("Enter the Surah:Ayah Number :")
        self.label1.setWordWrap(True)
        self.label2.setWordWrap(True)
        self.label3.setWordWrap(True)

        self.btn.clicked.connect(self.ayah)

    def ayah(self):
        ayah_number = self.bar.text()
        base_url = "http://api.alquran.cloud/v1/ayah"
        versions = ["ar.alafasy", "en.sahih", "ur.jalandhry"]

        url1 = f"{base_url}/{ayah_number}/{versions[0]}"
        url2 = f"{base_url}/{ayah_number}/{versions[1]}"
        url3 = f"{base_url}/{ayah_number}/{versions[2]}"
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        response3 = requests.get(url3)
        self.quran_data1 = self.check1(response1)
        quran_data2 = self.check2(response2)
        quran_data3 = self.check3(response3)

        try:
            self.set1 = f"Arabic {ayah_number}: {self.quran_data1["data"]["text"]}"
            self.set2 = f"English {ayah_number}: {quran_data2["data"]["text"]}"
            self.set3 = f"Urdu {ayah_number}: {quran_data3["data"]["text"]}"
            audio_url = self.quran_data1["data"].get("audio")

            if self.check.isChecked() and audio_url:
                if not hasattr(self, "player"):
                    self.player = vlc.MediaPlayer(audio_url)
                self.player.stop()
                self.player = vlc.MediaPlayer(audio_url)
                self.player.play()
            else:
                if hasattr(self, "player"):
                    self.player.stop()

        except:
            self.set1 = "Ayah not valid"
            self.set2 = "Ayah not valid"
            self.set3 = "Ayah not valid"

        self.label1.setText(self.set1)
        self.label2.setText(self.set2)
        self.label3.setText(self.set3)

    def check1(self, response1):
        if response1.status_code == 200:
            quran_data1 = response1.json()
            return quran_data1
        else:
            return None

    def check2(self, response2):
        if response2.status_code == 200:
            quran_data2 = response2.json()
            return quran_data2
        else:
            return None

    def check3(self, response3):
        if response3.status_code == 200:
            quran_data3 = response3.json()
            return quran_data3
        else:
            return None

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("quran.ico"))) #for icon
    window = Ayah()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


