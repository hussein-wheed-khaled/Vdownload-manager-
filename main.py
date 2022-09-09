import moviepy
from pytube import YouTube
import os
from pathlib import Path
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog,QProgressBar,QVBoxLayout,QComboBox,QLineEdit,QListWidget,QLabel
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import time
import os
from tkinter.filedialog import *
from moviepy import editor
from pathlib import Path
class Dialog(QDialog):

    def __init__(self):
        global savep
        super(Dialog,self).__init__()
        loadUi("design.ui",self)
        n = 800
        #self.prog=QProgressBar()
        #self.pp=QComboBox
        #self.lis=QListWidget()
        self.label_10.hide()

        self.la=QLabel()
        self.label_4.hide()
        self.progressBar.setEnabled(False)
        self.progressBar.setMinimum(18)
        self.progressBar.setMaximum(n)
        savep=open("temppath.txt","r+")

        save=open("temp.txt","r+")
        r=save.readlines()
        for i in r:
         self.listWidget.addItem(str(i))

        self.progressBar.setStyleSheet("""QProgressBar {
                border-style:solid;
                color:white;
                border-color: grey;
                border-radius: 7px;
                border-width: 1px;
                text-align: center;
                
            }
            QProgressBar::chunk {
                width: 14px;
                background-color: #0000ff;
                margin: 3px;
            }

            

        """)
        self.pushButton.clicked.connect(lambda status, n_size=n: self.download(n_size))
        self.pushButton_2.clicked.connect(self.browse)



    def download(self,n):
        global path
        global url
        global savepath



        if self.lineEdit.text()[0] == "h":
            self.label_4.show()

            if self.comboBox.currentIndex()==0:        #480p
             link=self.lineEdit.text()
             url=YouTube(link)
             video = url.streams.get_lowest_resolution()

             path=QFileDialog.getSaveFileName(self, 'select file to save', str(url.title.title()))
             #QFileDialog.getSaveFileName(self, 'select file', str(url.title.title()))

             for i in range(n):
                 time.sleep(0.00001)
                 self.progressBar.setValue(i+1)
                 video.download(path[0])


             self.label_6.setText(str(url.title.title()))
             with open("temp.txt","a") as saving:
              saving.write("\n"+str(url.title.title()))
              self.listWidget.addItem("\n"+str(url.title.title()))
             with open("temppath.txt","w") as savepath:
                 savepath.write(path[0])

            elif self.comboBox.currentIndex()==1:          #720p
                link = self.lineEdit.text()
                url = YouTube(link)
                self.progressBar.setValue(19)
                video = url.streams.get_highest_resolution()

                path = QFileDialog.getSaveFileName(self, 'select file to save', str(url.title.title()))
                # QFileDialog.getSaveFileName(self, 'select file', str(url.title.title()))

                for i in range(n):
                    time.sleep(0.00001)
                    self.progressBar.setValue(i + 1)
                    video.download(path[0])

                self.label_6.setText(str(url.title.title()))
                with open("temp.txt", "a") as saving:
                    saving.write("\n" + str(url.title.title()))
                    self.listWidget.addItem(str(url.title.title()))
                with open("temppath.txt", "w") as savepath:
                    savepath.write(path[0])
            elif self.comboBox.currentIndex()==2:
                link = self.lineEdit.text()
                url = YouTube(link)
                video = url.streams.get_lowest_resolution()

                path = str("mp3")
                # QFileDialog.getSaveFileName(self, 'select file', str(url.title.title()))

                for i in range(n):
                    time.sleep(0.00001)
                    self.progressBar.setValue(i + 1)
                    video.download(path)

                video = askopenfilename()
                video = moviepy.editor.VideoFileClip(video)
                audio = video.audio
                audio.write_audiofile("mp3\\"+str(url.title.title()+"(mp3)"+".mp3"))







                self.label_6.setText(str(url.title.title()))
                with open("temp.txt", "a") as saving:
                    saving.write("\n" + str(url.title.title()))
                    self.listWidget.addItem("\n" + str(url.title.title()))
                with open("temppath.txt", "w") as savepath:
                    savepath.write(path)


        else:
            self.label_4.hide()
            self.label_10.show()
            self.label_6.setText("The link is incorrect")
    def browse(self):
        r=savep.readline()


        os.startfile(r)




import rc
app=QApplication(sys.argv)
mainw=Dialog()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainw)
widget.setFixedWidth(822)
widget.setFixedHeight(548)
widget.show()
app.exec_()


