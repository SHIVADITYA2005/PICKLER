<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://img.icons8.com/color/96/python.png" width="90" alt="Python Logo">
</p>

<h1 align="center">🐍 PICKLER – Simple File Pickling GUI</h1>

<p align="center">
  <i>A lightweight, beginner-friendly Python app that makes pickling files effortless through a clean Tkinter GUI.</i>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/GUI-Tkinter-yellow?logo=windowsterminal&logoColor=white" alt="Tkinter Badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Stable-success" alt="Status"></a>
</p>

---

## 🧠 Overview

**PICKLER** is a simple yet powerful **Python desktop GUI tool** that helps users **pickle and unpickle files** of any type — `.txt`, `.jpg`, `.xlsx`, `.py`, and more.  
Built with **Tkinter**, it offers a **multi-frame interface** that guides users from a welcome screen to a file uploader, and finally to the pickler module — all without any console interaction.

> ⚡ “Turning Python serialization into a visual, beginner-friendly experience.”

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 🖥️ **Welcome Screen** | Displays the current timestamp and your system's IP address. |
| 📂 **File Uploader** | Allows you to browse and select any file type for pickling. |
| 🥒 **Pickle & Unpickle** | Convert files into `.pkl` and retrieve their original form instantly. |
| 🔁 **Multi-frame Navigation** | Switch easily between Welcome, Upload, and Pickler screens. |
| 🎨 **User-Friendly GUI** | Minimalist, intuitive, and built entirely with Tkinter. |

---

## 🧩 Technologies Used

| Component | Technology |
|------------|-------------|
| Programming Language | **Python 3.x** |
| GUI Library | **Tkinter** |
| Serialization | **pickle module** |
| Utility Modules | **datetime**, **socket** |
| Platform | Cross-platform (Windows/Linux/Mac) |

---

## 🧱 System Architecture

```plaintext
┌──────────────────────────────┐
│        PICKLER GUI           │
│  (Tkinter Multi-Frame App)   │
└──────────────┬───────────────┘
               │
    ┌──────────▼───────────┐
    │  File Uploader Frame │  ← Selects files via Tkinter filedialog
    └──────────┬───────────┘
               │
    ┌──────────▼───────────┐
    │  Pickler/Unpickler   │  ← Uses pickle.dump() & pickle.load()
    └──────────┬───────────┘
               │
    ┌──────────▼───────────┐
    │  Welcome Frame       │  ← Displays timestamp & IP info
    └──────────────────────┘
⚙️ Installation & Setup
🪜 Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/PICKLER.git
cd PICKLER
🪜 Step 2: Run the Application
bash
Copy code
python pickler.py
✅ That’s it! The GUI will launch instantly — no dependencies, no setup scripts.

🧠 How It Works
1️⃣ Launch the app — The Welcome screen displays your system IP and current timestamp.
2️⃣ Upload any file — Browse and select files of any type.
3️⃣ Pickle it — Save the file in serialized .pkl format.
4️⃣ Unpickle — Restore the original file content with one click.

👨‍💻 Author

Developed by:
🧑‍💻 Shivaditya
🎓 B.Tech CSE (AIML), SRM Institute of Science & Technology, NCR Campus

🪪 License

This project is open-source under the MIT License.
Feel free to modify, fork, or contribute with attribution.

```
<p align="center"> <img src="https://img.icons8.com/color/96/python.png" width="70" alt="Python Logo"> </p> <h3 align="center">"Simplifying Python serialization, one GUI at a time."</h3> <p align="center"> <a href="https://github.com/SHIVADITYA2005/PICKLER"> <img src="https://img.shields.io/github/stars/SHIVADITYA2005/PICKLER?style=social" alt="GitHub stars"> </a> <a href="https://github.com/SHIVADITYA2005/PICKLER/fork"> <img src="https://img.shields.io/github/forks/SHIVADITYA2005/PICKLER?style=social" alt="GitHub forks"> </a> </p> 
