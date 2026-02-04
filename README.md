*****🎓 Free Course Downloader (Recursive)*****

A simple yet powerful Python CLI tool to recursively download free online courses from directory-style websites.
It mirrors the website’s folder structure locally and shows a live progress bar while downloading files — perfect for offline learning.

*****✨ Features*****

📥 Download entire free courses in one command

🔁 Recursive crawling of folders & subfolders

📁 Preserves original directory structure

📊 Live per-file download progress

🧹 Safe filenames (Windows / Linux compatible)

♻️ Skips already downloaded files

⚙️ Clean CLI interface using flags (-u, -o)

🧠 Who Is This For?

Students downloading free educational content
Learners who want offline access to courses
Cybersecurity / reverse-engineering learners
Anyone archiving public directory listings

*****🛠 Requirements*****

Python 3.8+

Install dependencies
```
pip install -r requirements.txt

```

*****🚀 Usage*****
Basic command
```
python downloader.py -u <COURSE_URL> -o <OUTPUT_FOLDER>
```

Example
```
python downloader.py \
  -u https://elhacker.info/Cursos/Assembly%20Language%20Programming%20for%20Reverse%20Engineering/ \
  -o Courses
```


*****📁 Output structure:*****

Courses/
 ├── Lesson01/
 ├── Lesson02/
 ├── notes.pdf
 └── videos/

*****⚙️ Command Line Options*****
Flag	Description
-u, --url	Base URL of the free course (required)
-o, --output	Output directory (default: Downloads)
-h	Show help menu
📂 How It Works

Fetches the course page

Parses directory links using BeautifulSoup

Recursively enters subfolders

Downloads files with chunked streaming

Displays a progress bar for each file

Skips files already downloaded

*****🔐 Filename Safety*****

The downloader automatically removes illegal characters:

: ? * | < > "


*****This ensures compatibility across operating systems.*****

⚠️ Disclaimer

⚠️ Important

This tool is intended only for free & publicly available courses

Do NOT use it on paid, private, or restricted content

Always respect:

Website Terms of Service

Copyright laws

Bandwidth limits

The author is not responsible for misuse.

*****📄 License*****

MIT License — free to use, modify, and share.

*****🙌 Author*****

Created by Nahid Hasan
Focused on learning automation, cybersecurity, and reverse engineering.

*****🔮 Planned Improvements*****

--delay (rate limiting)

--max-depth

--thread increase

Resume interrupted downloads

Domain restriction

Logging support

Packaging as a pip tool
