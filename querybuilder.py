#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from query_builder_ui import Ui_Form





class QueryBuilder(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(QueryBuilder, self).__init__(parent)
        self.setupUi(self)
        self.qb_ellipsemajoraxis.hide()
        self.qb_ellipseminoraxis.hide()
        self.qb_ellipseorientation.hide()
        self.qb_ellipseorientation_label.hide()
        self.qb_minoraxis_lablel.hide()
        self.qb_majoraxis_label.hide()
        self.qb_shapeselection.currentIndexChanged.connect(self.getshape)
        
        
        
    def getshape(self, index):
        self.shape = self.qb_shapeselection.itemText(index)
        if self.shape == 'Ellipse':
            self.qb_ellipsemajoraxis.show()
            self.qb_ellipseminoraxis.show()
            self.qb_ellipseorientation.show()
            
            self.qb_ellipseorientation_label.show()
            self.qb_minoraxis_lablel.show()
            self.qb_majoraxis_label.show()
        else:
            self.qb_ellipsemajoraxis.hide()
            self.qb_ellipseminoraxis.hide()
            self.qb_ellipseorientation.hide()
            self.qb_ellipseorientation_label.hide()
            self.qb_minoraxis_lablel.hide()
            self.qb_majoraxis_label.hide()
