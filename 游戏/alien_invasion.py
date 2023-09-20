import sys
import random
from time import *

import pygame
from pygame.sprite import Group
from tkinter import *
from PIL import Image,ImageTk

from settings import *
from boss import Boss
from boss_blood import Blood
from ship import Ship
import game_functions1 as gf1
import game_functions2 as gf2
from game_stats import Gamestats
import special_effects
from others import about,ending
from warning import Warn
from scoreboard import Scoreboard

def run_game():
	root.destroy()
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	background=pygame.transform.smoothscale(pygame.image.load('./pictures/background.bmp'),screen.get_size())
	ship=Ship(ai_settings,screen)
	stats=Gamestats(ai_settings)
	with open('.\log\\record of the Normal mode.txt','r') as f:
		highest=int(f.readline())
	sb=Scoreboard(ai_settings,screen,stats,highest)
	bullets=Group()
	missiles1=Group()
	missiles2=Group()
	missiles3=Group()
	aliens1=Group()
	aliens2=Group()
	aliens3=Group()
	pygame.display.set_caption('Alien Invasion')
	special_effects.count_down(ai_settings,screen,background)
	while True:
		ai_settings.alien_speed_factor=0.5*(stats.score//10000)
		gf1.check_events(ai_settings,screen,ship,bullets,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3)
		if not stats.game_active:
			sleep(4)
			ending(2,stats.score,ai_settings)
		else:
			if ai_settings.skill_bullet_limit>0:
				ai_settings.count1-=1
				ai_settings.skill_bullet_limit-=1
			if not aliens1 and not aliens2 and not aliens3:
				missiles1.empty()
				missiles2.empty()
				missiles3.empty()
				num=random.randint(1,3)
				if num==1:	gf1.create_alien1(ai_settings,screen,aliens1)
				elif num==2:	gf1.create_alien2(ai_settings,screen,aliens2)
				elif num==3:	gf1.create_alien3(ai_settings,screen,aliens3)
			elif aliens1:
				gf1.create_missile1(ai_settings,screen,aliens1,missiles1)
				gf1.update_missile1(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
			elif aliens2:
				gf1.create_missile2(ai_settings,screen,aliens2,missiles2)
				gf1.update_missile2(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
			elif aliens3:
				gf1.create_missile3(ai_settings,screen,aliens3,missiles3)
				gf1.update_missile3(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
			ship.update()
			gf1.update_bullets(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
			gf1.update_aliens(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
		screen.blit(background,(0, 0))
		gf1.update_screen(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)



def Speed_Competition():
	root.destroy()
	pygame.init()
	ai_settings=Settings()
	ai_settings.ship_limit=9
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	background=pygame.transform.smoothscale(pygame.image.load('./pictures/boss_background.bmp'),screen.get_size())
	ship=Ship(ai_settings,screen)
	stats=Gamestats(ai_settings)
	bullets=Group()
	missiles1=Group()
	missiles2=Group()
	missiles3=Group()
	lasers=Group()
	boss=Boss(ai_settings,screen)
	blood=Blood(ai_settings,screen)
	pygame.display.set_caption('Alien Invasion')
	special_effects.count_down(ai_settings,screen,background)
	flag1=flag2=flag3=flag4=flag4_=0
	start=perf_counter()
	while True:
		gf2.check_events(ai_settings,screen,ship,bullets,missiles1,missiles2,missiles3,lasers)
		if not stats.game_active:
			sleep(4)	
			ending(1,0,ai_settings)
		elif not stats.game_win:
			end=perf_counter()
			seconds=end-start
			sleep(4)
			ending(3,seconds,ai_settings)
		else:
			if ai_settings.skill_bullet_limit>0:
				ai_settings.count1-=1
				ai_settings.skill_bullet_limit-=1
			if ai_settings.count1>0:
				gf2.check_bullets_missiles_collision(ai_settings,screen,bullets,missiles1,missiles2,missiles3)
			ship.update()
			boss.update()
			gf2.update_bullets(ai_settings,screen,ship,boss,blood,bullets)
			gf2.update_boss(ai_settings,stats,screen,ship,boss,bullets,missiles1,missiles2,missiles3,lasers)
			if flag1>0:
				gf2.create_missile1(ai_settings,screen,boss,missiles1)
				flag1-=1
			if flag2>0:
				gf2.create_missile2(ai_settings,screen,boss,missiles2)
				flag2-=1
			if flag3>0:
				gf2.create_missile3(ai_settings,screen,boss,missiles3)
				flag3-=1
			if flag4>0:
				warning.update()
				warning.blitme()
				pygame.display.flip()
				flag4-=1
				if flag4==0:
					gf2.create_laser(ai_settings,screen,lasers,laser_centerx,boss)
					flag4_=500
			if flag1==0 and flag2==0 and flag3==0 and flag4==0:
				skills=random.randint(1,3000)	#改变右边的值可以调整难度
				if skills==5 and not missiles3:	flag1=3
				if skills==10:	flag2=2
				if skills==15:	flag3=1
				if skills==20 and not missiles3:
					laser_centerx=boss.rect.centerx+random.randint(-500,500)
					warning=Warn(ai_settings,screen,laser_centerx,boss)
					flag4=1000
			if missiles1:
				gf2.update_missile1(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers)
			if missiles2:
				gf2.update_missile2(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers)
			if missiles3:
				gf2.update_missile3(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers)
			if flag4_:
				flag4_-=1
				gf2.update_laser(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers,flag4_)
		screen.blit(background,(0, 0))
		gf2.update_screen(ai_settings,stats,screen,ship,boss,blood,bullets,missiles1,missiles2,missiles3,lasers)
		
		
def choice():
	global root_
	root_=Toplevel()
	root_.title('start')
	root_.geometry('1280x720')
	canvas_=Canvas(root_,width=1280,height=720)
	canvas_.pack()
	bg_image_=Image.open("./pictures/start.gif")
	bg_image_=ImageTk.PhotoImage(bg_image_)
	canvas_.create_image(0, 0, anchor='nw', image=bg_image_)
	canvas_.config(width=bg_image_.width(),height=bg_image_.height())
	canvas_.create_text(600,130,text='rules',font=('Arial', 24))
	canvas_.create_text(600,180,text='1.Click UP,DOWN,LEFT,RIGHT to control the movement of the airship.',font=('Arial',15))
	canvas_.create_text(647,220,text='2.Click Left Mouse Button to fire normal bullets.                                                  ',font=('Arial',15))
	canvas_.create_text(580,260,text='3.Click E to use the special skill.                                                  ',font=('Arial',15))
	canvas_.create_text(563,300,text='4.Click C to clear the screen.                                                 ',font=('Arial',15))
	c1=Button(canvas_,text='<--Go Back',bg='white',fg='black',width=10,height=1,command=root_.destroy)
	c1.place(x=3,y=3)
	c1.bind('<Enter>',special_effects.button_hover2)
	c1.bind('<Leave>',special_effects.button_leave1)
	c2=Button(canvas_,text='Normal',width=20,height=2,command=run_game)
	c2.place(x=300,y=600)
	c2.bind('<Enter>',special_effects.button_hover1)
	c2.bind('<Leave>',special_effects.button_leave1)
	c3=Button(canvas_,text='Speed Competition',width=20,height=2,command=Speed_Competition)
	c3.place(x=800,y=600)
	c3.bind('<Enter>',special_effects.button_hover1)
	c3.bind('<Leave>',special_effects.button_leave1)
	root_.mainloop()
	
	
def Startgame():
	global root
	root=Tk()
	root.title('Alien Invasion')
	root.geometry('640x320')
	canvas=Canvas(root,width=640,height=320)
	canvas.pack()
	bg_image=Image.open("./pictures/start_background.gif")
	bg_image=ImageTk.PhotoImage(bg_image)
	canvas.create_image(0, 0, anchor='nw', image=bg_image)
	canvas.config(width=bg_image.width(), height=bg_image.height())
	canvas.create_text(bg_image.width()//2,60,
		text='Welcome To Alien Invasion',fill='white', font=('Arial', 24), tags='text')
	c1=Button(canvas,text='start game',font='20',width=20,height=2,command=choice)
	c1.place(x=320,y=180)
	c1.bind('<Enter>',special_effects.button_hover1)
	c1.bind('<Leave>',special_effects.button_leave1)
	c2=Button(canvas,text='quit game',font='20',width=20,height=2,command=root.destroy)
	c2.place(x=320,y=230)
	c2.bind('<Enter>',special_effects.button_hover1)
	c2.bind('<Leave>',special_effects.button_leave1)
	c3=Button(canvas,text='about',font='20',width=10,height=1,command=about)
	c3.place(x=10,y=275)
	c3.bind('<Enter>',special_effects.button_hover2)
	c3.bind('<Leave>',special_effects.button_leave1)
	root.mainloop()
		
if __name__=='__main__':
	Startgame()
