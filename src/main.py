#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : serhank
# Created Date: 25/11/2021
# version ='1.0'
# ----------------------------------------------------------------------------

import tkinter
from Lyrics import Lyrics
from tkinter import *

class GUI(object):
    """
    Creates a Desktop GUI.
    """
    def __init__(self):
        """ Calls main window. """
        self.main_window()

    def main_window(self):
        """Creates search window and redirects to the lyrics screen. """

        window = Tk(className=' Get Lyrics v1.0')
        window.geometry('350x100')

        Label(window, text="Enter artist's/band's name").grid(row=1, column=0)
        Label(window, text="Enter song's name         ").grid(row=2, column=0)

        artist = tkinter.Entry()
        artist.grid(row=1, column=1)

        song = tkinter.Entry()
        song.grid(row=2, column=1)

        def openNewWindow(artist, song, lyrics):
            newWindow = Toplevel(window)
            newWindow.minsize(500, 100)
            newWindow.title(f'{artist}-{song}')
            Label(newWindow, text=lyrics).pack()

        informations = []
        def get_button(info_list: list=informations):
            """
            :param info_list: In order to get the variables outside of the function.
            :return: Returns nothing but calls the window that will display the lyrics.
            """
            while True:
                search = Lyrics() # Create the object.

                info_list.append([artist.get(), song.get()])
                # print(info_list) # Not neccessary.. For now.
                lyrics = search.get_lyrics(info_list[0][0], info_list[0][1])
                openNewWindow(info_list[0][0], info_list[0][1], lyrics)
                info_list.clear()
                break

        tkinter.Button(window,
                       text='Search',
                       command= lambda button= 'Button Clicked': get_button()).grid(row=3, column=1, sticky=tkinter.W, pady=0)

uyg = GUI()
mainloop()
