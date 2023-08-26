import os, time as t, itertools, tkinter, ctypes
from tkinter import filedialog as tkFileDialog

os.system('pip install colorama pystyle')
import pystyle as ps
from colorama import init, Fore as f, Back as b, Style as s
init()

ctypes.windll.kernel32.SetConsoleTitleW('YouTubeAutoDownloader by eltrevii')
os.system('cls' if os.name == 'nt' else 'clear')

intro_text = '''
importing modules
loading text
setting up variables
loading functions
distracting you
displaying this text
eating bing chilling
learning portuguese manito
reading this text
'''

banner1 = '''
       _ _                  _ _ 
      | | |                (_|_)
   ___| | |_ _ __ _____   ___ _ 
  / _ \\ | __| '__/ _ \\ \\ / / | |
 |  __/ | |_| | |  __/\\ V /| | |
  \\___|_|\\__|_|  \\___| \\_/ |_|_|
                                
                                                      
'''

banner2 = '''
                                 _       
                                | |      
  _ __  _ __ ___  ___  ___ _ __ | |_ ___ 
 | '_ \\| '__/ _ \\/ __|/ _ \\ '_ \\| __/ __|
 | |_) | | |  __/\\__ \\  __/ | | | |_\\__ \\
 | .__/|_|  \\___||___/\\___|_| |_|\\__|___/
 | |                                     
 |_|                                     

'''

banner3 = '''

┓┏┏┳┓┏┓     ┳┓┓ 
┗┫ ┃ ┣┫┓┏╋┏┓┃┃┃ 
┗┛ ┻ ┛┗┗┻┗┗┛┻┛┗┛
                
'''

banner4 = '''

 ▄▀▀▄▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀▀▄      ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█   █   █ █   █   █ ▐  ▄▀   ▐ █ █   ▐ █ █   ▐     ▐  ▄▀   ▐ █  █ █ █ █    █  ▐ ▐  ▄▀   ▐ █   █   █ 
▐  █▀▀▀▀  ▐  █▀▀█▀    █▄▄▄▄▄     ▀▄      ▀▄         █▄▄▄▄▄  ▐  █  ▀█ ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀  
   █       ▄▀    █    █    ▌  ▀▄   █  ▀▄   █        █    ▌    █   █     █        █    ▌   ▄▀    █  
 ▄▀       █     █    ▄▀▄▄▄▄    █▀▀▀    █▀▀▀        ▄▀▄▄▄▄   ▄▀   █    ▄▀        ▄▀▄▄▄▄   █     █   
█         ▐     ▐    █    ▐    ▐       ▐           █    ▐   █    ▐   █          █    ▐   ▐     ▐   
▐                    ▐                             ▐        ▐        ▐          ▐                  

'''

time = 1
enter = False
for i in range(4):
	time += 1

	if i == 3:
		t.sleep(1)
		time = True
		enter = True		

	ps.Anime.Fade(
		ps.Center.Center(eval("banner" + str(eval('i+1')))),
		ps.Colors.black_to_red,
		ps.Colorate.Vertical,
		time=time, interval=0.035,
		enter=enter
	)


print(
	f'''{f.YELLOW}YTAutoDL
by {f.RED}eltrevii{f.YELLOW} ({f.BLUE}https://github.com/eltrevii{f.YELLOW})'''
	)

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = tkFileDialog.askdirectory(
	parent=root,
	initialdir=currdir,
	title='Select a path to download the videos'
)

print(tempdir)

url = 'hello world'
urls = []

while url != '':	
	url = input(f.GREEN + '> ')
	urls.append(url)

bool_urls = [i != "" for i in urls]
urls_new = list(itertools.compress(urls, bool_urls))

print(urls_new)
os.system('pause')

for i in urls_new:
	os.system('yt-dlp --no-warnings --no-playlist -q -o "tempdir\\%(title)s.%(ext)s" ' + i)
	print(f'[{ sum((urls_new.index(i), 1)) }/{ len(urls_new) }] done: ' + i)