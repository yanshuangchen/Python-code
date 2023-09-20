import pygame

class Blood():
	def __init__(self,ai_settings,screen):
		self.ai_settings=ai_settings
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,ai_settings.screen_width,10)
		self.rect.centerx=self.screen_rect.centerx
		self.rect.top=self.screen_rect.top
		self.color=255,0,64
		self.x=float(self.rect.x)
	def update(self):
		self.x=self.ai_settings.boss_blood-1200
		self.rect.x=self.x
	def draw(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
