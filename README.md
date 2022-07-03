# novels-dl
![Activity](https://shields.io/github/last-commit/danrog303/novels-dl)
![Gitmoji](https://img.shields.io/badge/gitmoji-%20📝%20🏗️-FFDD67.svg)
> Ebook downloading tool for polish light novel website named novelki.pl 

## 📝 Purpose of the project
Website https://novelki.pl/ contains many interesting books, but its huge drawback is that it only allows you to
read light novels through an online reader. This project allows you to download light novels and export them to an epub file.
Epub files are files that can be opened on e-book readers. Epub files can be easily converted to mobi format and opened on Kindle e-readers. 
They can also be easily converted to PDF format. The easiest way to do this is to use Calibre program.

## ✨ Features
- Log-in support (novelki.pl requires you to log in to download the content of any light novel)
- Localization (depending on the system language, the script will display information in English or Polish)
- Generation of an e-book as an .epub file
- Downloading basic metadata and embedding it in the .epub file
- Downloading a cover image and embedding it in the .epub file
- Generating a table of contents embedded in an .epub file
- Downloading both text and images
- Bypassing HTTP error 429 (Too Many Requests)
- Selection of paragraph style (Polish: hyphens with indentation or English: quotes with margins)
- Automatic correction of the formatting of some e-books (for example, removal of redundant &lt;br&gt; tags)

## 🔧 How to use?
1. First you need to create a free account on novelki.pl   
   ``https://novelki.pl/auth/register``.
2. if you have not already done so, you need to download Python interpreter. Python version 3.9 or higher is required!
3. Then you need to download the source code of the script
   ```
   $ git clone https://github.com/danrog303/novels-dl
   $ cd novels-dl/
   ```
4. The next step is to activate Python virtual environment
   ```
   # Instructions for Linux and macOS:
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ python3 -m pip install -r requirements.txt
   
   # Instructions for Windows:
   $ python3 -m venv venv
   $ venv scripts/activate
   $ python3 -m pip install -r requirements.txt
   ```
5. Finally, run the wizard, which takes you step-by-step through the process of downloading the light novel.
   ```
   python3 novels_cli.py
   ```