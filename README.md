# ---

# 

# \# 🌙 Quran App

# 

# A modern desktop Quran application built with \*\*Python (PyQt5)\*\* and the \*\*AlQuran Cloud API\*\*.

# Search any \*\*Surah:Ayah\*\*, view translations in \*\*Arabic, English, and Urdu\*\*,

# and optionally listen to the recitation — all in a beautifully designed, responsive interface.

# 

# ---

# 

# \## ✨ Features

# 

# \* 🔍 \*\*Search any Ayah\*\* using `Surah:Ayah` format (e.g., `2:255`)

# \* 🕌 \*\*Multilingual display:\*\* Arabic • English • Urdu

# \* 🎧 \*\*Audio playback:\*\* Stream recitation when the “Audio” option is checked

# \* 🪶 \*\*Modern design:\*\* Styled PyQt5 UI with soft gradients and rounded corners

# \* 💾 \*\*Lightweight \& Portable:\*\* Works even without installing VLC globally

# \* 🧱 \*\*Packaged EXE:\*\* Runs as a standalone app via PyInstaller

# 

# ---

# 

# \## 🧠 Technologies Used

# 

# | Component            | Description                                                 |

# | -------------------- | ----------------------------------------------------------- |

# | \*\*Python\*\*           | Core programming language                                   |

# | \*\*PyQt5\*\*            | GUI framework for the interface                             |

# | \*\*VLC (python-vlc)\*\* | Audio playback library                                      |

# | \*\*Requests\*\*         | For API calls to \[alquran.cloud](https://alquran.cloud/api) |

# | \*\*PyInstaller\*\*      | Used to create portable `.exe` builds                       |

# 

# ---

# 

# \## 🖼️ Preview

# 

# !\[App Screenshot](resources/images/ui\_preview.png)

# 

# > \*(Designed with a minimal purple-white aesthetic, rounded widgets, and balanced spacing for readability.)\*

# 

# ---

# 

# \## ⚙️ Setup Instructions

# 

# \### 🐍 For Developers

# 

# 1\. \*\*Clone the repository:\*\*

# 

# &nbsp;  ```bash

# &nbsp;  git clone https://github.com/<yourusername>/QuranApp.git

# &nbsp;  cd QuranApp

# &nbsp;  ```

# 

# 2\. \*\*Create and activate a virtual environment\*\* (recommended):

# 

# &nbsp;  ```bash

# &nbsp;  python -m venv venv

# &nbsp;  venv\\Scripts\\activate

# &nbsp;  ```

# 

# 3\. \*\*Install dependencies:\*\*

# 

# &nbsp;  ```bash

# &nbsp;  pip install -r requirements.txt

# &nbsp;  ```

# 

# 4\. \*\*Run the app:\*\*

# 

# &nbsp;  ```bash

# &nbsp;  python main.py

# &nbsp;  ```

# 

# ---

# 

# \### 💻 For End Users

# 

# If you downloaded the \*\*`.exe` release\*\*:

# 

# \* Simply run `QuranApp.exe`

# \* Keep the \*\*`vlc/` folder\*\* in the same directory

# \* No need to install VLC separately ✅

# 

# ---

# 

# \## 🧰 Build `.exe` (Optional)

# 

# To create a standalone Windows executable:

# 

# ```bash

# pyinstaller --noconsole --onefile --icon=quran.ico main.py

# ```

# 

# Then copy your \*\*`vlc/` folder\*\* beside the generated `.exe` in the `dist/` folder.

# 

# ---

# 

# \## 📦 Requirements

# 

# ```

# PyQt5

# requests

# python-vlc

# ```

# 

# ---

# 

# \## 📂 Folder Structure

# 

# ```

# Quran-App/

# │

# ├── main.py

# ├── README.md

# ├── requirements.txt

# ├── quran.ico

# │

# ├── VLC/

# │   ├── libvlc.dll

# │   ├── libvlccore.dll

# │   └── plugins/

# │

# ├── resources/

# │   └── images/

# │       ├── banner.png

# │       └── ui\_preview.png

# │

# └── dist/

# &nbsp;   ├── QuranApp.exe

# &nbsp;   └── vlc/

# ```

# 

# ---

# 

# \## 🧑‍💻 Developer

# 

# \*\*Developed by:\*\* \*Muhammad Hussnain Faraz\*

# 📍 \*BS Computer Science — GCUF Samundri Sub-Campus, Pakistan\*

# 💜 Passionate about Islamic software, AI, and open-source development.

# 

# ---

# 

# \## 🕋 Credits

# 

# \* \*\*Quran Data API:\*\* \[alquran.cloud](https://alquran.cloud/api)

# \* \*\*Recitations:\*\* Mishary Rashid Alafasy (public access)

# \* \*\*Purpose:\*\* Built sincerely for the benefit of the Ummah, \*Fi Sabeelillah.\*

# 

# ---

# 

# \## 🧿 License

# 

# This project is open-source under the \*\*MIT License\*\*.

# Feel free to fork, enhance, and share — \*for the sake of Allah (سُبْحَانَهُ وَتَعَالَى).\*

# 

# ---



