"""
This class is probably going to be deleted
"""

from tkinter import *


class Screen:
    def __init__(self, title="Assets Manager", ):

        self.__root = Tk()

        # root config
        self.__root.geometry("800x600+350+100")
        self.__root.title(title)
        # TODO self._root.iconbitmap()

        # self.__root.mainloop()

    @property
    def root(self):
        return self.__root

