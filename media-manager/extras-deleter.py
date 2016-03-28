#!/usr/bin/python3
import configparser
from os import *

"""Deletes all the extra files in your media directories
	Removes non-video, non-music, non-image files
	As a warning, be sure you do not have important
	files in your directories

	Use config.ini to change file directories

	Default file directory structure:
	--/
	----/books
	----/movies
	----/music
	----/tv
"""

def scanDir(directory):
	# Parse Filesytem
	print("Check directory:", directory)
	subdirs = [subdir for subdir in listdir(directory) if path.isdir(path.join(directory, subdir))]
	files = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]
	print("Files:", files)

	if not subdirs:
		return
	else:
		print("Subdirs:", subdirs)
		for subdir in subdirs:
			scanDir(directory + "/" + subdir)

def main():
	# Read Config File
	config = configparser.ConfigParser()
	config.read('config.ini')
	ROOTDIR = config['DEFAULT']['RootDir']
	BOOKDIR = ROOTDIR + "/" + config['DEFAULT']['BookDir']
	MOVIEDIR = ROOTDIR + "/" + config['DEFAULT']['MovieDir']
	MUSICDIR = ROOTDIR + "/" + config['DEFAULT']['MusicDir']
	TVDIR = ROOTDIR + "/" + config['DEFAULT']['TVDir']
	
	scanDir(MUSICDIR)

if __name__ == "__main__":
	main()
