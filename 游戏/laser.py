import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
	def __init__(self,ai_settings,screen,laser_centerx,boss):
		super(Laser,self).__init__()
		self.ai_settings=ai_settings
		self.screen=screen
		self.boss=boss
		self.image=pygame.image.load('./pictures/laser.bmp')
		self.image=pygame.transform.scale(self.image,(200,ai_settings.screen_height))
		self.rect=self.image.get_rect()
		self.rect.centerx=laser_centerx
		self.rect.top=boss.rect.bottom-200
	def update(self):
		self.rect.top=self.boss.rect.bottom
