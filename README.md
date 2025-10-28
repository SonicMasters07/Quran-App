---

🌙 Quran App

<p align="center">
  <img src="resources/images/ui/_preview/banner.png" alt="Quran App Banner" width="100%">
</p>A modern desktop Quran application built with Python (PyQt5) and the AlQuran Cloud API.
Search any Surah:Ayah, view translations in Arabic, English, and Urdu, and listen to recitations — all in a beautifully designed, responsive interface.


---

✨ Features

🔍 Search any Ayah using the Surah:Ayah format (e.g., 2:255)

🕌 Multilingual display: Arabic • English • Urdu

🎧 Audio playback: Stream recitations when the “Audio” option is checked

🪶 Modern design: Soft gradients, rounded widgets, and balanced spacing

💾 Lightweight & Portable: Works without global VLC installation

🧱 Packaged EXE: Runs as a standalone app built with PyInstaller



---

🧠 Technologies Used

Component	Purpose

Python	Core programming language
PyQt5	GUI framework
VLC (python-vlc)	Audio playback
Requests	API communication (alquran.cloud)
PyInstaller	Executable packaging



---

🖼️ UI Preview

<p align="center">
  <img src="resources/images/ui/_preview/ui.png" alt="App UI Preview" width="80%">
</p>> Minimal purple-white design with balanced readability and soft styling.




---

⚙️ Setup for Developers

# Clone the repository
git clone https://github.com/<yourusername>/QuranApp.git
cd QuranApp

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py


---

💻 For End Users

If you downloaded the .exe release:

1. Simply run QuranApp.exe


2. Keep the VLC_README.txt file beside the .exe


3. ✅ No need to install VLC separately




---

🧰 Build .exe (Optional)

pyinstaller --noconsole --onefile --icon=quran.ico main.py

After building, ensure the VLC_README.txt file stays beside your generated .exe in the dist/ folder.


---

📦 Requirements

PyQt5
requests
python-vlc


---

📂 Project Structure

Quran-App/
│
├── main.py
├── README.md
├── requirements.txt
├── quran.ico
│
├── VLC_README.txt
│
├── resources/
│   └── images/
│       └── ui/
│           └── _preview/
│               ├── banner.png
│               └── ui.png
│
└── dist/
    └── QuranApp.exe


---

🕋 Credits

Quran Data API: alquran.cloud

Recitations: Mishary Rashid Alafasy (public access)

Purpose: Built sincerely for the benefit of the Ummah — Fi Sabeelillah.



---

👨‍💻 Developer

Muhammad Hussnain Faraz
📍 BS Computer Science — GCUF Samundri Sub-Campus, Pakistan
💜 Passionate about Islamic software, AI, and open-source development.


---

🧿 License

Open-sourced under the MIT License.
Use, modify, and share — for the sake of Allah (سُبْحَانَهُ وَتَعَالَى).


---

⭐ Support:
If you find this project beneficial, give it a star ⭐ on GitHub — more Islamic software projects are on the way!


---