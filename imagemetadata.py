#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from image_metadata_ui import Ui_imagemetadata


class ImageMetadata(QWidget, Ui_imagemetadata):
    def __init__(self, parent=None):
        super(ImageMetadata, self).__init__(parent)
        self.setupUi(self)
