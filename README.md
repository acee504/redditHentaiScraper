# Hent<nolink>@<nolink>i.py [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
This python script will download pictures from defined subreddits.
  
To run on Windows:
1. download and install Python 3.9 from https://www.python.org/downloads/release/python-390/
2. Clone the repo
2. Hold down Shift and right click in the folder where the .py files are and open Command Prompt
4. Install requests by doing the following command ```pip install requests```
5. When its installed you can now run the script by typing ```python Hent@i.py```
To stop the script press Ctrl + C  


How to add more subreddits:
1. Navigate to the files folder and here you create a new folder with the name of the subreddit so there is a folder per subreddit
2. Now go back to the root of the repo and copy the template.py file and name it the name of the subreddit you want to download pictures from.
3. Replace the replaceme on line 4 in the file with the name of the subreddit.
4. Open Hent<nolink>@<nolink>i.py and up in the top you find some import functions, add another one with the name of the subreddit.
5. Near the bottom you also add in a new getData like the others have.