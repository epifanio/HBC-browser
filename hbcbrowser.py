#/usr/local/bin/python36


import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from hbc_browser_gui import HBCBrowserGui
import pyproj
import pandas as pd
import socket
from sys import platform
import qdarkstyle

from imagemetadata import ImageMetadata
from kmlsave import SaveKml
from querybuilder import QueryBuilder
from log import *
from configure import get_settings

import errno
from socket import error as socket_error


class MapDisplay(QObject):
    fromMain=pyqtSignal(str)

    def __init__(self, parent=None):
        super(MapDisplay, self).__init__(parent)
        self.settings = get_settings()
        self.w = HBCBrowserGui()
        self.imagelist = []
        self.imageindex = 1
        self.ZoomStepValue = 50
        self.rangevalue = 2000
        self.host = self.settings['settings']['broadcast']['ip']
        # self.host = 'localhost'
        self.port = self.settings['settings']['broadcast']['port']
        self.dirname = self.settings['settings']['hbcbrowser']['imagepath']
        self.metadatafile = self.settings['settings']['hbcbrowser']['imagemetadata']
        self.projection = "+proj=utm +no_defs +zone=19 +a=6378137 +rf=298.257223563 +towgs84=0.000,0.000,0.000 +to_meter=1"

        self.initUI()
    
    def initUI(self):
        # self.w = HBCBrowserGui()
        self.w.toolWidget.hide()
        self.w.fwd.clicked.connect(self.increaseimageindex)
        # self.w.fwd.clicked.connect(self.updatespinbox)
        # self.w.fwd.clicked.connect(self.addImage)
        self.w.rwd.clicked.connect(self.decreaseimageindex)
        # self.w.rwd.clicked.connect(self.addImage)
        # ZOOM
        self.w.ZoomStepSlider.valueChanged.connect(self.setValueZoomStepspinBox)
        self.w.ZoomStepSlider.valueChanged.connect(self.addImage)
        self.w.ZoomStepspinBox.valueChanged.connect(self.setValueZoomStepSlider)
        # self.w.ZoomStepspinBox.valueChanged.connect(self.printFunction)
        self.w.ZoomStepSlider.valueChanged.connect(self.setValue)
        self.w.ZoomStepspinBox.valueChanged.connect(self.setValue)
        # Image Index
        self.w.ImageIndexSlider.valueChanged.connect(self.setValueImageIndexspinBox)
        # self.w.ImageIndexSlider.valueChanged.connect(self.printFunction)
        self.w.ImageIndexspinBox.valueChanged.connect(self.setValueImageIndexSlider)
        self.w.ImageStepspinBox.valueChanged.connect(self.setImageIndexStepValue)
        self.w.ImageIndexSlider.valueChanged.connect(self.addImage)
        # hardcoded image file and metadata  
        self.image = QLabel()
        self.w.scrollArea_3.setWidget(self.image)
        # self.w.scrollArea_3.setWidget(self.image)
        self.getImageDir_hard()
        self.w.latitude = QLineEdit()
        self.w.longitude = QLineEdit()
        self.w.longitude.setFocusPolicy(Qt.NoFocus)
        self.w.latitude.setFocusPolicy(Qt.NoFocus)
        self.w.latitude.setFixedWidth(160)
        self.w.longitude.setFixedWidth(160)
        self.w.statusbar.addPermanentWidget(self.w.longitude, stretch=0)
        self.w.statusbar.addPermanentWidget(self.w.latitude, stretch=0)
        #self.myProj = pyproj.Proj("+proj=utm +no_defs +zone=19 +a=6378137 +rf=298.257223563 +towgs84=0.000,0.000,0.000 +to_meter=1")
        self.myProj = self.projection
        self.w.range.valueChanged.connect(self.setValuerangeSpinBox)
        self.getImageMetadata_hard()
        self.w.actionTools.triggered.connect(self.showTools)
        self.w.refresh.clicked.connect(self.on_send)
        if platform == "darwin":
            self.w.fwd.hide()
            self.w.rwd.hide()
        self.w.refresh.hide()
        self.imagemetadata = ImageMetadata()
        self.w.tools.insertTab(0, self.imagemetadata, 'Image Metadata') 
        self.savekml = SaveKml()
        self.fromMain.connect(self.savekml.from_main_signal)
        #self.w.tools.insertItem(1, self.savekml, 'Annotation') 
        self.w.tools.insertTab(1, self.savekml, 'Annotation')   
        self.querybuilder = QueryBuilder()
        #self.fromMain.connect(self.querybuilder.from_main_signal)
        #self.w.tools.insertItem(2, self.querybuilder, 'Query Builder')              
        self.w.tools.insertTab(2, self.querybuilder, 'Query Builder')  
        self.log = logS()            
        self.w.actionBroadcast.triggered.connect(self.startstoplog)
        self.w.actionBroadcast.triggered.connect(self.stopstartlog)
        self.w.actionQuit.triggered.connect(self.quitAll)
        
        self.w.show()

    def quitAll(self):
        qApp.quit()




    @pyqtSlot()
    def on_send(self):
        imagelink = '<img src="%s" alt="Smiley face" height="300"><br>' % os.path.join(self.dirname, self.imagelist[self.imageindex])
        #self.w.linklabel.setText("<a href=\"file://%s\">%s</a>" % (os.path.join(self.dirname, self.imagelist[self.imageindex]), str(record['Imagename'].values[0])))
        #self.fromMain.emit(self.w.linklabel.text())
        self.fromMain.emit(imagelink)
        self.savekml.longitude.setText(self.w.longitude.text())
        self.savekml.latitude.setText(self.w.latitude.text())
        # update query builder widgets
        self.querybuilder.qb_longitude.setText(self.w.longitude.text())
        self.querybuilder.qb_latitude.setText(self.w.latitude.text())




    def startstoplog(self):
        if self.w.actionBroadcast.isChecked():
            #self.log = logS()
            self.log.start()
            self.log.LonUpdated.connect(self.w.longitude.setText)
            self.log.LatUpdated.connect(self.w.latitude.setText)
            #self.log.RollUpdated.connect(self.w.RollSpinBox.setValue)
            #self.log.PitchUpdated.connect(self.w.PitchSpinBox.setValue)
            #self.log.GainUpdated.connect(self.w.HandlingSpinBox.setValue)
            #self.log.AltUpdated2.connect(self.w.Alt.setText)
            #self.log.AltUpdated.connect(self.w.ZoomSpinBox.setValue)
            #self.log.LookAtLonUpdated.connect(self.w.lookatLon.setText)
            #self.log.LookAtLatUpdated.connect(self.w.lookatLat.setText)
            #self.log.LookAtAltitudeUpdated.connect(self.w.lookatAlt.setText)
            #self.log.LookAtRangeUpdated.connect(self.w.RangeSpinBox.setValue)
            
            self.log.toggle()
        else :
            self.log.stop()
    
    
    def stopstartlog(self):
        if not self.w.actionBroadcast.isChecked():
            #self.log = logS()
            self.log.stop()
            self.log.toggle()
        else:
            self.log.stop()
            self.log.toggle()





    def setValuerangeSpinBox(self, r):
        self.rangevalue = int(r)
        self.w.range.setSingleStep(1)
        self.w.range.setValue(self.rangevalue)
        if self.w.zoomto.isChecked():
            self.zoom_to()
        
    def showTools(self):
        if self.w.toolWidget.isVisible():
            self.w.toolWidget.hide()
            #self.savekml.hide()
        else:
            self.w.toolWidget.show()
            #self.savekml.show()


    def zoom_to(self):
        lon = self.w.longitude.text()
        lat = self.w.latitude.text()
        distance = self.rangevalue
        ossim_zoom_xml = '<Set target=":navigator" vref="wgs84"><Camera><longitude>%s</longitude><latitude>%s</latitude><altitude>%s</altitude><heading>0</heading><pitch>0</pitch><roll>0</roll><altitudeMode>absolute</altitudeMode><range>%s</range></Camera></Set>' % (
            lon, lat, distance, distance)
        try:
            ossimposition = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ossimposition.settimeout(10)
            ossimposition.connect((self.host, int(self.port)))
            ossimposition.settimeout(None)
            ossimposition.send(bytes(ossim_zoom_xml, "UTf-8"))
            ossimposition.close()
        except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
                raise serr
                print('No connection')
            # self.w.statusbar.showMessage("System Status | Connection failed")
        
        try:
            ossimposition = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ossimposition.settimeout(10)
            ossimposition.connect((self.host, int(9000)))
            ossimposition.settimeout(None)
            ossimposition.send(bytes(ossim_zoom_xml, "UTf-8"))
            ossimposition.close()
        except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
                raise serr
                print('No connection')
            # self.w.statusbar.showMessage("System Status | Connection failed")
        try:
            ossimposition = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ossimposition.settimeout(10)
            ossimposition.connect((self.host, int(7000)))
            ossimposition.settimeout(None)
            ossimposition.send(bytes(ossim_zoom_xml, "UTf-8"))
            ossimposition.close()
        except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
                raise serr
                print('No connection')
            # self.w.statusbar.showMessage("System Status | Connection failed")
        print(ossim_zoom_xml)
        # self.w.statusbar.showMessage("System Status | Normal")
        


    def getImageDir_hard(self):
        # self.dirname = '/Volumes/OSX 1/habcam_jpg_2015'
        # self.dirname = '/Volumes/ss1/habcam_jpg_2015'
        # self.dirname = '/media/epinux/ss1/habcam_jpg_2015'
        # self.dirname = '/Users/epi/Desktop/ImageBrowser/images'
        # self.dirname = '/Users/epi/Desktop/images'
        if self.dirname:
            self.imagelist = os.listdir(self.dirname)
            self.w.ImageIndexspinBox.setMaximum(len(self.imagelist) - 1)
            self.w.ImageIndexSlider.setMaximum(len(self.imagelist) - 1)

    def getImageMetadata_hard(self):
        # self.metadatafile = '/Users/epi/notebooks/USBL/projectdata.ft'

        # self.metadatafile = '/Users/epi/projectdata.ft'
        # self.metadatafile = '/media/epinux/ss1/projectdata.ft'
        self.imageMetadata = pd.read_feather(self.metadatafile)
        self.imageMetadata.index = pd.to_datetime(self.imageMetadata['index'])
        self.imageMetadata = self.imageMetadata.loc[self.imageMetadata['Imagename'].isin((i.replace('.jpg', '') for i in self.imagelist))]
        print(self.imageMetadata.columns)
        



    def updatespinbox(self):
         self.w.ImageIndexspinBox.setValue(self.imageindex)
         self.w.ImageIndexSlider.update()
         self.w.ImageIndexspinBox.update()
         print('fwd pressed')
    
    def decreaseimageindex(self):
        self.imageindex=self.imageindex-self.w.ImageStepspinBox.value()
        self.w.ImageIndexSlider.setValue(self.imageindex)
        self.w.ImageIndexspinBox.setValue(self.imageindex)
        self.w.ImageIndexspinBox.update()
    
    def increaseimageindex(self):
        self.imageindex = self.imageindex+self.w.ImageStepspinBox.value()
        self.w.ImageIndexSlider.setValue(self.imageindex)
        self.w.ImageIndexspinBox.setValue(self.imageindex)
        self.w.ImageIndexspinBox.update()

    
    def addImage(self):
        #self.w.image.clear()
        #self.w.image.setGeometry(QRect(0, 0, 1360, 1024))
         
        if any(self.imagelist) is not None:            
            self.pixmap = QPixmap(os.path.join(self.dirname, self.imagelist[self.imageindex]))
            print('orig size:', self.pixmap.width(), self.pixmap.height())
            width=self.pixmap.width()*(self.ZoomStepValue/100.)
            height=self.pixmap.height()*(self.ZoomStepValue/100.)
            self.pixmap = self.pixmap.scaled(width, height, Qt.KeepAspectRatio)
            print('height', self.image.height())
            print('width', self.image.width())
            print('heightMM', self.image.heightMM())
            print('widthMM', self.image.widthMM())
            #self.w.image.clear()         
            self.image.setGeometry(QRect(0, 0, width, height))
            self.image.setPixmap(self.pixmap)
            
            #
            #self.imageeast = str(self.imageMetadata['Xutm'].values[0])
            #self.imagenorth = str(self.imageMetadata['Yutm'].values[0])
            #self.w.statusbar.showMessage("Image %s" % self.imageMetadata.index[0])
            
            record = self.imageMetadata[self.imageMetadata['Imagename'] == self.imagelist[self.imageindex][:-4]]
            if len(record) !=0:
                self.w.longitude.setText(str(record['habcam_lon'].values[0]))
                self.w.latitude.setText(str(record['habcam_lat'].values[0]))
                
                # METADATA
                self.imagemetadata.imageeast.setText(str(record['Xutm_adj'].values[0]))
                self.imagemetadata.imagenorth.setText(str(record['Yutm_adj'].values[0]))
                self.imagemetadata.hbcdepth.setText(str(record['V_Depth'].values[0]))
                self.imagemetadata.waterdepth.setText(str(record['Water_Depth'].values[0]))
                self.imagemetadata.altimeter.setText(str(record['Altimeter'].values[0]))
                self.imagemetadata.salinity.setText(str(record['Salinity'].values[0]))
                self.imagemetadata.temperature.setText(str(record['Temp'].values[0]))
                self.imagemetadata.O2.setText(str(record['O2'].values[0]))
                self.imagemetadata.CDOM.setText(str(record['Cdom'].values[0]))
                self.imagemetadata.chlorophyll.setText(str(record['Chlorophyll'].values[0]))
                self.imagemetadata.turbidity.setText(str(record['Turb'].values[0]))
                # test QtDateTime
                self.imagemetadata.dateTimeEdit.setDateTime(record.index[0])
                self.imagemetadata.linklabel.setText("<a href=\"file://%s\">%s</a>" % (os.path.join(self.dirname, self.imagelist[self.imageindex]), str(record['Imagename'].values[0])))
                self.imagemetadata.linklabel.setOpenExternalLinks(True)
                
                self.w.statusbar.showMessage("Image %s" % record.index[0])

                
                if self.w.zoomto.isChecked():
                    self.zoom_to()
                self.on_send()
            else:
                print('record lenght:', len(record), 'for image index: ', self.imageindex, self.imagelist[self.imageindex])
            #

        else:
            print('both image path not be set')
            print(' --- ')



    def setValueZoomStepspinBox(self, z):
        self.ZoomStepValue = int(z)
        #self.w.ZoomStepspinBox.setRange(1, 100)
        self.w.ZoomStepspinBox.setSingleStep(1)
        self.w.ZoomStepspinBox.setValue(self.ZoomStepValue)

    def setValueZoomStepSlider(self, z):
        self.ZoomStepValue = int(z)
        self.w.ZoomStepSlider.setMinimum(1)
        #self.w.ZoomStepSlider.setMaximum(100)
        self.w.ZoomStepSlider.setValue(self.ZoomStepValue)

    def setValue(self, v):
        self.Value = v
    
    def setValueImageIndexspinBox(self, z):
        self.imageindex = int(z)
        self.w.ImageIndexspinBox.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexspinBox.setValue(self.imageindex)
    
    def setValueImageIndexSlider(self, z):
        self.imageindex = int(z)
        self.w.ImageIndexSlider.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexSlider.setValue(self.imageindex)
    
    def setImageIndexStepValue(self):
        self.w.ImageIndexspinBox.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexSlider.setSingleStep(self.w.ImageStepspinBox.value())

    
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.processEvents()
    p = MapDisplay()
    sys.exit(app.exec_())

