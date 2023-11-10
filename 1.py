import sys
import io

import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>382</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>110</y>
     <width>221</width>
     <height>121</height>
    </rect>
   </property>
   <property name="text">
    <string>Кнопка</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class Example(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

    def initUI(self):
        self.do_paint = False
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
        a = random.randint(50, 150)
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        qp.drawEllipse(y, x, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())