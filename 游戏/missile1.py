import pygame
from pygame.sprite import Sprite
import random

class Missile1(Sprite):
	def __init__(self,ai_settings,screen,boss):
		super(Missile1,self).__init__()
		self.screen=screen
		self.rect=pygame.Rect(0,0,ai_settings.missile1_width,ai_settings.missile1_height)
		self.rect.centerx=boss.rect.centerx+random.uniform(-550,550)
		self.rect.top=boss.rect.bottom
		self.y=float(self.rect.y)
		self.color=ai_settings.missile1_color
		self.speed_factor=ai_settings.missile12_speed_factor
	def update(self):
		self.y+=self.speed_factor
		self.rect.y=self.y
	def draw_missile1(self):
		pygame.draw.rect(self.screen,self.color,self.rect)


class Missile1_(Sprite):
	def __init__(self,ai_settings,screen,alien):
		super(Missile1_,self).__init__()
		self.ai_settings=ai_settings
		self.screen=screen
		self.direction=random.randint(1,4)
		self.rect=pygame.Rect(0,0,ai_settings.missile1_width,ai_settings.missile1_height)
		if self.direction==1:
			self.rect=pygame.Rect(0,0,ai_settings.missile1_width,ai_settings.missile1_height)
			self.rect.top=alien.rect.bottom
		elif self.direction==2:
			self.rect=pygame.Rect(0,0,ai_settings.missile1_width,ai_settings.missile1_height)
			self.rect.bottom=alien.rect.top
		elif self.direction==3:
			self.rect=pygame.Rect(0,0,ai_settings.missile1_height,ai_settings.missile1_width)
			self.rect.right=alien.rect.left
		elif self.direction==4:
			self.rect=pygame.Rect(0,0,ai_settings.missile1_height,ai_settings.missile1_width)
			self.rect.left=alien.rect.right
		self.rect.centerx=alien.rect.centerx+random.uniform(-5,5)
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		self.color=ai_settings.missile1_color
		self.speed_factor=ai_settings.missile12_speed_factor
		self.screen_rect=screen.get_rect()
	def update(self):
		if self.direction==1:
			self.y+=self.speed_factor
			self.rect.y=self.y
		elif self.direction==2:
			self.y-=self.speed_factor
			self.rect.y=self.y
		elif self.direction==3:
			self.x-=self.speed_factor
			self.rect.x=self.x
		else:
			self.x+=self.speed_factor
			self.rect.x=self.x
		
	def check_edges(self):
		if self.rect.top>=self.ai_settings.screen_height or self.rect.bottom<=0 or self.rect.right>=self.screen_rect.right or self.rect.left<=0:
			return True
			
	def draw_missile1(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
