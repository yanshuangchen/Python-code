import pygame
import random
from pygame.sprite import Sprite

class Alien1(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien1,self).__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.image=pygame.image.load('./pictures/alien1.bmp')
		self.image=pygame.transform.scale(self.image,(50,50))
		self.rect=self.image.get_rect()
		self.rect.x=random.randint(100,ai_settings.screen_width-100)
		self.rect.top=self.screen_rect.top
		self.speed=ai_settings.alien_speed_factor+random.uniform(-0.2,0.2)
		self.direction=ai_settings.fleet_direction
		self.x=float(self.rect.x)
	def check_edges(self):
		if self.rect.right>=self.screen_rect.right:	return True
		elif self.rect.left<=0:	return True
	def update(self):
		self.x+=self.speed*self.direction
		self.rect.x=self.x
	

class Alien2(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien2,self).__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.image=pygame.image.load('./pictures/alien2.bmp')
		self.image=pygame.transform.scale(self.image,(40,40))
		self.rect=self.image.get_rect()
		self.rect.x=random.randint(100,ai_settings.screen_width-100)
		self.rect.top=self.screen_rect.top
		self.speed=ai_settings.alien_speed_factor+random.uniform(-0.2,0.2)
		self.direction=ai_settings.fleet_direction
		self.x=float(self.rect.x)
	def check_edges(self):
		if self.rect.right>=self.screen_rect.right:	return True
		elif self.rect.left<=0:	return True
	def update(self):
		self.x+=self.speed*self.direction
		self.rect.x=self.x


class Alien3(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien3,self).__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.image=pygame.image.load('./pictures/alien3.bmp')
		self.image=pygame.transform.scale(self.image,(75,75))
		self.rect=self.image.get_rect()
		self.rect.x=random.randint(100,ai_settings.screen_width-100)
		self.rect.top=self.screen_rect.top
		self.speed=ai_settings.alien_speed_factor+random.uniform(-0.2,0.2)
		self.direction=ai_settings.fleet_direction
		self.x=float(self.rect.x)
	def check_edges(self):
		if self.rect.right>=self.screen_rect.right:	return True
		elif self.rect.left<=0:	return True
	def update(self):
		self.x+=self.speed*self.direction
		self.rect.x=self.x
