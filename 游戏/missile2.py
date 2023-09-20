import pygame
import random
from pygame.sprite import Sprite

class Missile2(Sprite):
	def __init__(self,ai_settings,screen,boss):
		super(Missile2,self).__init__()
		self.screen=screen
		self.image=pygame.image.load('./pictures/missile2.bmp')
		self.image=pygame.transform.scale(self.image,(40,100))
		self.rect=self.image.get_rect()
		self.rect.centerx=boss.rect.centerx+random.uniform(-550,550)
		self.rect.top=boss.rect.bottom
		self.y=float(self.rect.y)
		self.speed_factor=ai_settings.missile12_speed_factor+random.uniform(-0.25,0.25)
	def update(self):
		self.y+=self.speed_factor
		self.rect.y=self.y
	

class Missile2_(Sprite):
	def __init__(self,ai_settings,screen,alien):
		super(Missile2_,self).__init__()
		self.screen=screen
		self.image=pygame.image.load('./pictures/missile2.bmp')
		self.image=pygame.transform.scale(self.image,(40,100))
		self.rect=self.image.get_rect()
		self.rect.centerx=alien.rect.centerx
		self.rect.top=alien.rect.bottom
		self.y=float(self.rect.y)
		self.speed_factor=ai_settings.missile12_speed_factor+random.uniform(-0.25,0.25)
	def update(self):
		self.y+=self.speed_factor
		self.rect.y=self.y
