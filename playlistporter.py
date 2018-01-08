from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#I hope to tranfer playlists from Spotify to Play Music at the moment. I want the user to open the webdriver himself and then login for me and then I continue with the transfer. The login has to be done for both Spotify and Play Music, so it will require two webdrivers
# str(str(string).encode('ascii','ignore'))[2:-1]
class Spotify: #The spotify class that controls the spotify webdriver
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.selection = set()
		self.selected = set()
		self.playlists = []
		self.songs = []
		self.importPlaylists = [[['playlist name and songs after this'],['Description of Playlist and Artists continue after this....'],['Created by and Albums continue after']]]
		print('Opening Spotify...')
		self.driver.get("https://accounts.spotify.com/en/login?utm_source=webplayer&utm_medium=&utm_campaign=&continue=https:%2F%2Fopen.spotify.com%2Fbrowse") #Directly opens the spotify login page

	# def __del__(self):
	# 	self.driver.close()

	def login(self):
		# username = input('Enter your Spotify username or email address: ')
		# password = str(getpass.getpass('Enter the password: '))
		username = "Htnamus"
		password = 'i am sad'
		print('Signing into Spotify...')
		usrfield = self.driver.find_element_by_id('login-username')
		pwdfield = self.driver.find_element_by_id('login-password')
		usrfield.send_keys(username)
		pwdfield.send_keys(password)
		pwdfield.send_keys(Keys.RETURN)
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "navBar-item")))
		print('Sign in successful')

	def fetchPlaylists(self):
		self.driver.get('https://open.spotify.com/collection/playlists')
		self.playlists = self.driver.find_elements_by_class_name('mo-info-name')
		print('The playlists in your account are: ')
		for playlist in self.playlists:
			print('\t '+ str(self.playlists.index(playlist) + 1) + '. ' +str(str(playlist.text).encode('ascii','ignore'))[2:-1])

	def selectPlaylists(self):
		for _ in range(len(self.playlists)):
			if _ != 0:
				print('Playlists selected so far:\n')
				for selec in self.selection:
					print(str(str(self.playlists[ selec ].text).encode('ascii', 'ignore'))[ 2:-1 ], end = '; ')
				print('\n')
			# pl = input('Enter the serial number of the playlist you want. Press Enter once your done with a serial number. Enter \'done\' once all your selections  are over \n')
			pl = 23
			if str(pl) == 'done':
				print('Playlists selected are:\n')
				for selec in self.selection:
					print(str(str(self.playlists[selec].text).encode('ascii','ignore'))[2:-1])
				break
			self.selection.add(int(pl)-1)
			self.selected.add(self.playlists[int(pl)-1])
			break

	def fetchSongs(self, URL):
		self.songs = []
		self.driver.get(URL)
		self.importPlaylists[0][0][0] = 'Best Themes'
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tracklist-name")))
		self.songsElements = self.driver.find_elements_by_class_name('tracklist-name')
		self.artistsAndAlbumsElements = self.driver.find_elements_by_css_selector('.artists-album')
		for songElement in self.songsElements:
			self.songs.append() #Add the names of the songs to the list

	def choosePlaylist(self):
		count = 0
		for selec in self.selected:
			print('Fetching Songs from \'' + str(str(selec.text).encode('ascii','ignore'))[2:-1] + '\'...')
			self.importPlaylists[count][0][0] = str(str(selec.text).encode('ascii','ignore'))[2:-1]
			self.fetchSongs(URL = selec.get_attribute('href')
			count += 1
)




class PMusic:
	def __init__(self): #The play music class that controls the play music webdriver
		self.driver = webdriver.Firefox()
		print('Opening Play Music...')
		self.driver.get("https://play.google.com/music/listen#/wmp") #Opens the play music playlists page
		signin = self.driver.find_element_by_css_selector('div.button-holder paper-button')
		signin.click()

	# def __del__(self):
	# 	self.driver.close()

	def login(self):
		# usrfield = self.driver.find_element_by_id('identifierId')
		# username = input('Please enter your Google Play music email ID: ')
		# usrfield.send_keys(username)
		# usrfield.send_keys(Keys.RETURN)
		# WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
		# pwdfield = self.driver.find_element_by_css_selector('.jQ9OEf .zHQkBf')
		# pwd = str(getpass.getpass('Enter the password: '))
		# pwdfield.send_keys(pwd)
		# pwdfield.send_keys(Keys.RETURN)
		# THe app isn't able to enter the password for some reason but I'll have to check it out later
		input('Please open the webdriver and login into Google Play Music. Press Enter once done')


#print('Please allow all incoming connections when asked for it\n')
spotify = Spotify()
spotify.login()
# PMusic  = PMusic()
# PMusic.login()
# spotify.fetchPlaylists()
# spotify.selectPlaylists()
# spotify.choosePlaylist()
spotify.fetchSongs(URL = 'https://open.spotify.com/user/htnamus/playlist/746pzDziRmsL0qUZ1l8kyc')
print('\nProcess terminated')