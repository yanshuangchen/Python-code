import pygame.font

class Scoreboard():
	def __init__(self,ai_settings,screen,stats,highest):
		self.highest=highest
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		self.prep_score()
		self.prep_highestscore()
		self.prep_left()
	def prep_score(self):
		score_str=str(self.stats.score)
		self.score_image=self.font.render(score_str,True,self.text_color,(0,0,0))
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20
	def prep_highestscore(self):
		highest_str=str(self.highest)
		self.highest_image=self.font.render(highest_str,True,self.text_color,(0,0,0))
		self.highest_rect=self.highest_image.get_rect()
		self.highest_rect.centerx=self.screen_rect.centerx
	def prep_left(self):
		left_str=str(self.stats.ship_left)
		self.left_image=self.font.render(left_str,True,self.text_color,(0,0,0))
		self.left_rect=self.highest_image.get_rect()
		self.left_rect.right=self.screen_rect.right-20
		self.left_rect.top=60
		
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.highest_image,self.highest_rect)
		self.screen.blit(self.left_image,self.left_rect)
