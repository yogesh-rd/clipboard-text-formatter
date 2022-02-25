# remove-newline-characters
A GUI tool made using `tkinter` for removing newline characters from your clipboard. Replaces every  `\n` with a whitespace, ideal for copy pasting text from PDFs into your own documents.

## Running the Application
(Developed using Python 3.8.10)
- Install `tkinter` - `pip3 install tk` .
- Download the source code.
- Open `app.py` and edit the `file` parameter in line 6 to point to `icon.png` in your local directory. 
- Run it as `python3 /path/to/project/dir/app.py`
- Optionally, you can use [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html) to get an executable.
- The following window should open.

![Screenshot](https://raw.githubusercontent.com/yogesh-rd/remove-newline-characters/main/screenshot.png)
## Using the Application
- Copy some text.
- Click on the "Remove newline characters" button.
- Paste the text.