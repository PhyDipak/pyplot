import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel,QLineEdit,QPushButton,QVBoxLayout,QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
x=[1,2,3,4,5]
y=[45,56,67,78,89]
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyplot")
        self.setGeometry(0,0,400,400)
        self.setWindowIcon(QIcon('chart.png'))
        self.layout0=QVBoxLayout(self)
        layout1=QHBoxLayout()
        layout2=QHBoxLayout()
        layout3=QHBoxLayout()
        layout4=QHBoxLayout()
        layout5=QHBoxLayout()
        button=QPushButton('Plot')
        self.xl=QLineEdit()
        self.xr=QLineEdit() 
        self.yl=QLineEdit()        
        self.yr=QLineEdit()    
        self.xl.setText(f'{x[0]}')
        self.xr.setText(f'{x[-1]}')
        self.yl.setText(f'{y[0]}')
        self.yr.setText(f'{y[-1]}')
        
        self.autox=QPushButton('auto X')
        self.autoy=QPushButton('auto Y')
        
        layout1.addWidget(QLabel(text='X Range'))
        layout1.addWidget(self.xl)
        layout1.addWidget(self.xr)
        layout1.addWidget(self.autox)
        layout1.addStretch()
        layout2.addWidget(QLabel(text='Y Range'))
        layout2.addWidget(self.yl)
        layout2.addWidget(self.yr)
        layout2.addWidget(self.autoy)
        layout2.addStretch()
        
        layout3.addStretch()
        layout3.addWidget(button)
        layout3.addStretch()
        
        self.combo_box1=QComboBox()
        self.combo_box1.addItem(QIcon('icon1_1.png'),'')
        self.combo_box1.setItemData(0, 'o', role=Qt.UserRole)
        self.combo_box1.addItem(QIcon('icon2_1.png'),'')
        self.combo_box1.setItemData(1, '*', role=Qt.UserRole)
        self.combo_box1.addItem(QIcon('icon3_1.png'),'')
        self.combo_box1.setItemData(2, 's', role=Qt.UserRole)
        
        self.combo_box2=QComboBox()
        self.combo_box2.addItem(QIcon('red.png'),'')
        self.combo_box2.setItemData(0, 'red', role=Qt.UserRole)
        self.combo_box2.addItem(QIcon('green.png'),'')
        self.combo_box2.setItemData(1, 'green', role=Qt.UserRole)
        self.combo_box2.addItem(QIcon('blue'),'')
        self.combo_box2.setItemData(2, 'blue', role=Qt.UserRole)

        
        layout4.addWidget(QLabel(text='Line style'))
        layout4.addWidget(self.combo_box1)
        
        layout4.addWidget(QLabel(text='Colour'))
        layout4.addWidget(self.combo_box2)
        layout4.addStretch()
        
        layout5.addWidget(QLabel(text='Designed by Dipak'))
        layout5.addStretch()
        layout5.addWidget(QLabel(text='App Version 1.0.0'))
        
        self.fig=plt.figure()
        self.ax=self.fig.add_subplot()
        self.canvas=FigureCanvas(self.fig)
        
        self.layout0.addWidget(self.canvas)
        self.layout0.addLayout(layout1)
        self.layout0.addLayout(layout2)
        self.layout0.addLayout(layout4)
        self.layout0.addLayout(layout3)
        self.layout0.addStretch()
        self.layout0.addLayout(layout5)
        
        
                
        button.clicked.connect(self.plot)  
        self.combo_box1.currentIndexChanged.connect(self.plot)
        self.combo_box2.currentIndexChanged.connect(self.plot)
        self.autox.clicked.connect(self.autorangex)
        self.autoy.clicked.connect(self.autorangey)
        self.autox.clicked.connect(self.plot)
        self.autoy.clicked.connect(self.plot)
        
    def autorangex(self):
        self.xl.setText(f'{x[0]}')
        self.xr.setText(f'{x[-1]}')
    def autorangey(self):
        self.yl.setText(f'{y[0]}')
        self.yr.setText(f'{y[-1]}')
        
        
        
        
        
    def plot(self):
        plt.clf()
# =============================================================================
#         x=[1,2,3,4,5]
#         y=[45,56,67,78,89]
# =============================================================================
        self.ax=self.fig.add_subplot()
        self.icon_name = self.combo_box1.itemData(self.combo_box1.currentIndex(), role=Qt.UserRole)
        self.colour = self.combo_box2.itemData(self.combo_box2.currentIndex(), role=Qt.UserRole)
                 
        self.ax.plot(x,y,linestyle='-',marker=self.icon_name,color=self.colour)
        plt.xlim(float(self.xl.text()),float(self.xr.text()))  
        plt.ylim(float(self.yl.text()),float(self.yr.text()))        
        self.canvas.draw()
        
        #plt.replot()
#        plt.show()
        
        
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    windows=window()
    windows.show()
    sys.exit(app.exec())
 