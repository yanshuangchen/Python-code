import sys
import datetime
from tkinter import *
import tkinter.messagebox as mb
import pygame
from pygame.sprite import Group

from tkinter.scrolledtext import ScrolledText
from special_effects import button_hover1,button_leave1,button_hover2
from settings import *
from ship import Ship
import game_functions1 as gf1
from game_stats import Gamestats

def ending(mode,score,ai_settings):
	pygame.quit()
	root1=Tk()
	root1.withdraw()
	if mode==1:
		mb.showinfo(title='Game Over',message='You lose!')
		with open('.\log\\log.txt','a',encoding='utf-8') as f:
			f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'		(Boss mode)		'+'Failed\n')
	elif mode==2:
		with open('.\log\\log.txt','a') as f:
			f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'		(Normal mode)		'+str(score)+'\n')
		with open('.\log\\record of the Normal mode.txt','r') as f:
			highest=float(f.readline())
		if score>highest:
			with open('.\log\\record of the Normal mode.txt','w') as f:
				f.write(str(score))
			mb.showinfo(title='恭喜',message='最终得分：'+str(score)+' ,打破纪录!')
		else:	mb.showinfo(title='结算',message='最终得分：'+str(score))
	else:
		score+=ai_settings.punishment
		with open('.\log\\log.txt','a') as f:
			f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'		(Boss mode)		'+str(score)+'s\n')
		with open('.\log\\record of the Boss mode.txt','r') as f:
			highest=float(f.readline())
		if score<highest:
			with open('.\log\\record of the Boss mode.txt','w') as f:
				f.write(str(score))
			mb.showinfo(title='恭喜',message='共用时'+str(score)+'秒,打破纪录!')
		else:	mb.showinfo(title='结算',message='共用时'+str(score)+'秒!')
	root1.destroy()
	sys.exit(0)
	
	
def about():
	global root
	root=Tk()
	root.title('about')
	root.geometry('310x300')
	scroll_text = ScrolledText(root, width=41, height=20)
	scroll_text.pack()
	scroll_text.insert(END,f'About the game:\n')
	scroll_text.insert(END,f'------------------rules------------------')
	scroll_text.insert(END,f'1. In the normal mode, you need to shoot down as many enemies as you can while keeping yourself safe to get a higher score.\n')
	scroll_text.insert(END,f'2. In the boss mode, you need to beat the enemies as fast as possible to get a better record, which takes your abilities as well as you luck!\n')
	scroll_text.insert(END,f"3. File 'log.txt' records all the results while file 'record.txt' only records the highest records.\n")
	scroll_text.insert(END,f'-----------------warning-----------------')
	scroll_text.insert(END,f"To ensure a perfect gaming experience,\nplease don't change the sizes of the windows!\n")
	scroll_text.insert(END,f'-----------------------------------------')
	scroll_text.insert(END,f'Producer:yizuichu\n')
	scroll_text.insert(END,f'Github:buwangchuxinyizuichu\n')
	scroll_text.insert(END,f'-----------------------------------------')
	scroll_text.insert(END,f'Thanks for playing!\n')
	scroll_text.config(state=DISABLED)  # 禁止编辑
	scroll_text.see(END)  # 滚动到底部
	scroll_text.config(state=NORMAL)  # 允许编辑
	c1=Button(root,text='<--Go Back',width=10,height=1,command=root.destroy)
	c1.place(x=100,y=265)
	c1.bind('<Enter>',button_hover2)
	c1.bind('<Leave>',button_leave1)
	root.mainloop()
