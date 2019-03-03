#!/usr/bin/env python3

import sys
import os
import random

import pygame
from pygame import *

from subprocess import call

from bs4 import BeautifulSoup
import requests
import schedule

# Globals
followersReport = [0,0,0] # Followers, Following, Posts
followersReportPrevious = [0,0,0] # Followers, Following, Posts

# Pygame globals
display_width = 128
display_height = 128

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (90,59,60)

black_olive = (63, 63, 63) # BG
carmine_pink = (237, 110, 111) # Followers
ruddy_pink = (359, 41, 95) # Less followers
orange_yellow = (255, 216, 103) # Following
pewter_blue = (138, 176, 171) # Posts

Font = None
ScreenOn = True

def checkFollowers():
	page = requests.get("https://www.instagram.com/henrytriplette/") # Get instagram page, use your own address
	soup = BeautifulSoup(page.content, 'html.parser')

	description = soup.find("meta",  property="og:description") # Read the meta
	if description:
		x = description["content"].split(" - ")
		formatMetaString(x[0])

		print(followersReport)

def formatMetaString(string):
	global followersReport  # Needed to modify global copy of followersReport
	if string:
		inputSplitted = string.split(" ") # Input string is supposed to look like this: 3,065 Followers, 3,219 Following, 117 Posts

		# Save old value
		followersReportPrevious[0] = int(followersReport[0])
		followersReportPrevious[1] = int(followersReport[1])
		followersReportPrevious[2] = int(followersReport[2])

		followersReport[0] = int(''.join(filter(lambda x: x.isdigit(), inputSplitted[0]))) # Clean string and convert to init
		followersReport[1] = int(''.join(filter(lambda x: x.isdigit(), inputSplitted[2])))
		followersReport[2] = int(''.join(filter(lambda x: x.isdigit(), inputSplitted[4])))

def drawDisplayToggle(screen, ScreenOn):

	if ScreenOn == True:
		drawDisplay(screen)
	else:
		drawDisplayBlack(screen)

def drawDisplayBlack(screen):

	screen.fill(black)

def drawDisplay(screen):

	screen.fill(black_olive)

	pygame.font.init() # you have to call this at the start, if you want to use this module.
	myfont = pygame.font.SysFont('Arial', 16)

	followers = myfont.render('Followers', False, carmine_pink) # This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.
	screen.blit(followers,(10,5))

	if followersReport[0] > followersReportPrevious[0]:
		followersCountColor = green
	elif followersReport[0] < followersReportPrevious[0]:
		followersCountColor = ruddy_pink
	else:
		followersCountColor = white

	followersCount = myfont.render(str(followersReport[0]), False, followersCountColor)
	text_rect = followersCount.get_rect()
	text_rect.right = 120
	text_rect.top = 25
	screen.blit(followersCount,text_rect)

	following = myfont.render('Following', False, orange_yellow)
	screen.blit(following,(10,45))

	if followersReport[1] > followersReportPrevious[1]:
		followingCountColor = green
	elif followersReport[1] < followersReportPrevious[1]:
		followingCountColor = ruddy_pink
	else:
		followingCountColor = white

	followingCount = myfont.render(str(followersReport[1]), False, followingCountColor)
	text_rect = followingCount.get_rect()
	text_rect.right = 120
	text_rect.top = 65
	screen.blit(followingCount,text_rect)

	posts = myfont.render('Posts', False, pewter_blue)
	screen.blit(posts,(10,85))

	postsCount = myfont.render(str(followersReport[2]), False, white)
	text_rect = postsCount.get_rect()
	text_rect.right = 120
	text_rect.top = 100
	screen.blit(postsCount,text_rect)

def restart():
	call("sudo nohup shutdown -h now", shell=True)

def main():

	# Change display to tft screen
	os.environ["SDL_FBDEV"] = "/dev/fb1"
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	# Init pygame
	pygame.init()

	# set screen
	screen = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('@Instagram monitor')

	#Disable mouse pointer
	pygame.mouse.set_visible(False)

	# Set icon
	# icon = pygame.image.load('assets/img/icons/ico.png')
	# pygame.display.set_icon(icon)

	# Set font
	global Font
	Font = pygame.font.Font(None, 20)

	# schedule
	schedule.every(10).to(20).minutes.do(checkFollowers)

	# Screen Toggle
	global ScreenOn

	# Main L00p
	going = True
	while going:
		events = pygame.event.get()
		for e in events:
			if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
				going = False
			if e.type == KEYDOWN:
				print(e.key)

				if e.key == 51:
					print("--- checkFollowers ---")
					checkFollowers()

				if e.key == 50:
					print("--- Quit ---")
					going = False

				if e.key == 49:
					print("--- Restart ---")
					restart()

				# Use joystick to loop trought effect list
				if e.key == K_UP:
					print("--- Screen: On ---")
					ScreenOn = True

				if e.key == K_DOWN:
					print("--- Screen: Off ---")
					ScreenOn = False

		drawDisplayToggle(screen, ScreenOn)

		schedule.run_pending()
		pygame.display.flip()
		time.wait(30)

	quit()


if __name__ == '__main__':
	main()


#
