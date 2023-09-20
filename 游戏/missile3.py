import pygame
import random
import math
from pygame.sprite import Sprite

class Missile3(Sprite):
	def __init__(self,ai_settings,screen,boss):
		super(Missile3,self).__init__()
		self.screen=screen
		self.image=pygame.image.load('./pictures/missile3.bmp')
		self.image=pygame.transform.scale(self.image,(150,350))
		self.image=pygame.transform.rotate(self.image,180)
		self.rect=self.image.get_rect()
		self.rect.centerx=boss.rect.centerx+random.randint(-150,150)
		self.rect.top=boss.rect.bottom
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.speed_factor=ai_settings.missile3_speed_factor
	def update(self):
		number=random.randint(1,2)
		if number==1:	self.x+=8+random.uniform(-5,5)
		else:	self.x-=8+random.uniform(-5,5)
		self.y+=self.speed_factor
		self.rect.x=self.x
		self.rect.y=self.y


class Missile3_(Sprite):
	def __init__(self,ai_settings,screen,alien):
		super(Missile3_,self).__init__()
		self.screen=screen
		self.image=pygame.image.load('./pictures/missile3.bmp')
		self.image=pygame.transform.scale(self.image,(150,350))
		self.image=pygame.transform.rotate(self.image,180)
		self.rect=self.image.get_rect()
		self.rect.centerx=alien.rect.centerx
		self.rect.top=alien.rect.bottom
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.speed_factor=ai_settings.missile3_speed_factor
	def update(self):
		number=random.randint(1,2)
		if number==1:	self.x+=8+random.uniform(-5,5)
		else:	self.x-=8+random.uniform(-5,5)
		self.y+=self.speed_factor
		self.rect.x=self.x
		self.rect.y=self.y
