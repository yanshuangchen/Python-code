import pygame
from tkinter import *
from time import sleep

def button_hover1(event):
	event.widget.configure(bg='red',fg='white')
def button_hover2(event):
	event.widget.configure(bg='gray',fg='white')
def button_hover3(event):
	event.widget.configure(bg='green',fg='white')
def button_leave1(event):
	event.widget.configure(bg='white',fg='black')


def count_down(ai_settings,screen,background):
	font=pygame.font.Font(None, 100)
	for i in range(3,0,-1):
		text=font.render(str(i), True, (255, 255, 255))
		text_rect=text.get_rect(center=(ai_settings.screen_width // 2, ai_settings.screen_height // 2))
		screen.blit(text, text_rect)
		pygame.display.flip()
		sleep(1)
		screen.blit(background, (0, 0))
