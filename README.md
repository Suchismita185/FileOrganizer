# 📂 File Organizer Using Python

A simple Python command-line application that automatically organizes files into folders based on their file extensions.

## 🚀 Features

- Organizes files according to their extensions.
- Automatically creates folders for different file types.
- Supports custom target directory paths.
- Prevents overwriting existing files by adding numeric suffixes.
- Handles files without extensions.
- Displays file movement progress in the terminal.
- Includes basic error handling.
- Uses only Python standard library modules.

## 🛠️ Technologies Used

- Python 3
- os
- shutil
- sys

## 📋 Prerequisites

Install Python 3 on your system.

No external libraries are required.

## 📥 Installation

Clone this repository:

```bash
git clone https://github.com/Suchismita185/FileOrganizer.git
```

Navigate to the project directory:

```bash
cd FileOrganizer
```

## ▶️ Usage

Run the program:

```bash
python file_organizer.py
```

Enter the directory path when prompted.

Alternatively, provide the target directory as a command-line argument:

```bash
python file_organizer.py "C:\Users\YourName\Downloads"
```

Replace the example path with your actual directory.

## 📁 Example

Before organizing:

```text
Downloads/
├── photo.jpg
├── document.pdf
├── notes.txt
└── script.py
```

After organizing:

```text
Downloads/
├── jpg/
│   └── photo.jpg
├── pdf/
│   └── document.pdf
├── txt/
│   └── notes.txt
└── py/
    └── script.py
```

## ⚙️ How It Works

1. Accepts a target directory from the user.
2. Identifies files and extracts their extensions.
3. Creates folders based on the extensions.
4. Moves files into the corresponding folders.
5. Generates unique filenames to avoid overwriting existing files.
6. Displays a summary of the operation.

## ⚠️ Important Note

This program moves files rather than copying them. Test it on a sample directory before organizing important files.

## 🎯 Learning Outcomes

This project demonstrates practical use of Python file handling, directory management, exception handling, command-line arguments, and automation.

## 📄 License

This project is available for educational and personal use.
