from PyQt5.QtWidgets import *
from view_scraper import *


class Controller(QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ChannelLinks.get