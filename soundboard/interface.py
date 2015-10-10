#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
#import player

class Interface():
	def __init__(self):
		self.root = Tk()
		self.root.wm_title("Soundboard")
		
		main_frame = Frame(
			borderwidth = 3,
			relief = GROOVE
			)
		main_frame.grid(column = 0, row = 0)

		song_label = Label(main_frame,
			text = "Song",
			font = ("hack", 12, "bold")
			)
		song_label.grid(row = 0, padx = 3, pady = 3, sticky = 'new')

		play_button = Checkbutton(main_frame, 
			text = "Play", 
			height = 3,
			wraplength = 80, 
			indicatoron = False,
			font = ("hack", 10)
			)
		play_button.grid(row = 1, padx = 3, pady = 3, sticky = 'ew')

		loop_checkbox = Checkbutton(main_frame, 
			text = "Loop",
			font = ("hack", 10)
			)
		loop_checkbox.grid(row = 2, padx = 3, pady = 3, sticky = 'ew')

		vol_slider = Scale(main_frame, 
			from_= 100, 
			to = 0,
			orient = VERTICAL, 
			length = 350,
			tickinterval = 10,
			borderwidth = 2,
			relief = RIDGE,
			font = ("hack", 10)
			)
		vol_slider.grid(row = 3, sticky = 'ews', padx = 5, pady = 3)

		self.root.mainloop()

if __name__ == "__main__":
	app = Interface()



