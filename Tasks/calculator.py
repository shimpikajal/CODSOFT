#Task No :2 
#simpple GUI based Calculator
#In this Task I have used PyQt6 for making GUI Based Calculator
#importing Required PYqt6 imports 
'''the Design of this calculator is done in Qt designer using pyuic6 commnad the main ui file is converted in python code 
and then required methods have Addded '''

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        
        Form.resize(306, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.clear = QtWidgets.QPushButton(parent=Form)
        self.clear.setGeometry(QtCore.QRect(20, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.clear.setObjectName("clearbtn")
        self.num7btn = QtWidgets.QPushButton(parent=Form)
        self.num7btn.setGeometry(QtCore.QRect(20, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.num7btn.setFont(font)
        self.num7btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num7btn.setObjectName("num7btn")
        self.powbtn = QtWidgets.QPushButton(parent=Form)
        self.powbtn.setGeometry(QtCore.QRect(20, 440, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.powbtn.setFont(font)
        self.powbtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.powbtn.setObjectName("powbtn")
        self.num1btn = QtWidgets.QPushButton(parent=Form)
        self.num1btn.setGeometry(QtCore.QRect(20, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num1btn.setFont(font)
        self.num1btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num1btn.setObjectName("num1btn")
        self.delbtn = QtWidgets.QPushButton(parent=Form)
        self.delbtn.setGeometry(QtCore.QRect(90, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.delbtn.setFont(font)
        self.delbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.delbtn.setObjectName("clearbtn")
        self.num8btn = QtWidgets.QPushButton(parent=Form)
        self.num8btn.setGeometry(QtCore.QRect(90, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num8btn.setFont(font)
        self.num8btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num8btn.setObjectName("num8btn")
        self.num5btn = QtWidgets.QPushButton(parent=Form)
        self.num5btn.setGeometry(QtCore.QRect(90, 320, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num5btn.setFont(font)
        self.num5btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num5btn.setObjectName("num5btn")
        self.num2btn = QtWidgets.QPushButton(parent=Form)
        self.num2btn.setGeometry(QtCore.QRect(90, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num2btn.setFont(font)
        self.num2btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num2btn.setObjectName("num2btn")
        self.zerobtn = QtWidgets.QPushButton(parent=Form)
        self.zerobtn.setGeometry(QtCore.QRect(90, 440, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.zerobtn.setFont(font)
        self.zerobtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.zerobtn.setObjectName("zerobtn")
        self.dotbtn = QtWidgets.QPushButton(parent=Form)
        self.dotbtn.setGeometry(QtCore.QRect(160, 440, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.dotbtn.setFont(font)
        self.dotbtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.dotbtn.setObjectName("dotbtn")
        self.num3btn = QtWidgets.QPushButton(parent=Form)
        self.num3btn.setGeometry(QtCore.QRect(160, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num3btn.setFont(font)
        self.num3btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num3btn.setObjectName("num3btn")
        self.num6btn = QtWidgets.QPushButton(parent=Form)
        self.num6btn.setGeometry(QtCore.QRect(160, 320, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num6btn.setFont(font)
        self.num6btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num6btn.setObjectName("num6btn")
        self.num9btn = QtWidgets.QPushButton(parent=Form)
        self.num9btn.setGeometry(QtCore.QRect(160, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num9btn.setFont(font)
        self.num9btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num9btn.setObjectName("num9btn")
        self.percentbtn = QtWidgets.QPushButton(parent=Form)
        self.percentbtn.setGeometry(QtCore.QRect(160, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.percentbtn.setFont(font)
        self.percentbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.percentbtn.setObjectName("percentbtn")
        self.dividebtn = QtWidgets.QPushButton(parent=Form)
        self.dividebtn.setGeometry(QtCore.QRect(230, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.dividebtn.setFont(font)
        self.dividebtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.dividebtn.setObjectName("dividebtn")
        self.mulbtn = QtWidgets.QPushButton(parent=Form)
        self.mulbtn.setGeometry(QtCore.QRect(230, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.mulbtn.setFont(font)
        self.mulbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.mulbtn.setObjectName("mulbtn")
        self.subbtn = QtWidgets.QPushButton(parent=Form)
        self.subbtn.setGeometry(QtCore.QRect(230, 320, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.subbtn.setFont(font)
        self.subbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.subbtn.setObjectName("subbtn")
        self.addbtn = QtWidgets.QPushButton(parent=Form)
        self.addbtn.setGeometry(QtCore.QRect(230, 380, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.addbtn.setObjectName("addbtn")
        self.equalbtn = QtWidgets.QPushButton(parent=Form)
        self.equalbtn.setGeometry(QtCore.QRect(230, 440, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.equalbtn.setFont(font)
        self.equalbtn.setStyleSheet("background-color: rgb(244, 163, 0);")
        self.equalbtn.setObjectName("equalbtn")
        self.num4btn = QtWidgets.QPushButton(parent=Form)
        self.num4btn.setGeometry(QtCore.QRect(20, 320, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.num4btn.setFont(font)
        self.num4btn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.num4btn.setObjectName("num4btn")
        self.label2 = QtWidgets.QLineEdit(parent=Form)
        self.label2.setGeometry(QtCore.QRect(18, 90, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label2.setFont(font)
        self.label2.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label2.setObjectName("outputbox")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.zerobtn.clicked.connect(self.press_zero)
        self.num1btn.clicked.connect(self.num_1)
        self.num2btn.clicked.connect(self.num_2)
        self.num3btn.clicked.connect(self.num_3)
        self.num4btn.clicked.connect(self.num_4)
        self.num5btn.clicked.connect(self.num_5)
        
        self.num6btn.clicked.connect(self.num_6)
        self.num7btn.clicked.connect(self.num_7)
        self.num8btn.clicked.connect(self.num_8)
        self.num9btn.clicked.connect(self.num_9)
        self.addbtn.clicked.connect(self.press_addbtn)
        self.subbtn.clicked.connect(self.press_subbtn)
        self.dividebtn.clicked.connect(self.press_divbtn)
        self.dotbtn.clicked.connect(self.press_dotbtn)
        self.mulbtn.clicked.connect(self.press_mulbtn)
        self.equalbtn.clicked.connect(self.press_equalbtn)
        self.percentbtn.clicked.connect(self.perss_percentbtn)
        self.powbtn.clicked.connect(self.calculate_power)
        self.clear.clicked.connect(self.press_clear)
        self.delbtn.clicked.connect(self.press_del)
        
        
   
    # appending label text
 
   
 
    def press_zero(self):
        
        text = self.label2.text()
        self.label2.setText(text + "0")
 
    def num_1(self):
        
        text = self.label2.text()
        self.label2.setText(text + "1")
 
    def num_2(self):
        
        text = self.label2.text()
        self.label2.setText(text + "2")
 
    def num_3(self):
        
        text = self.label2.text()
        self.label2.setText(text + "3")
 
    def num_4(self):
         text = self.label2.text()
         self.label2.setText(text + "4")
 
    def num_5(self):
    
        text = self.label2.text()
        self.label2.setText(text + "5")
 
    def num_6(self):
        
        text = self.label2.text()
        self.label2.setText(text + "6")
 
    def num_7(self):
        
        text = self.label2.text()
        self.label2.setText(text + "7")
 
    def num_8(self):
        
        text = self.label2.text()
        self.label2.setText(text + "8")
 
    def num_9(self):

        text = self.label.text()
        self.label2.setText(text + "9")
 
   
    def press_addbtn(self):                                 #method for addition
        
        text = self.label2.text()
        self.label2.setText(text + " + ")
 
    def press_subbtn(self):                                 #method for subtraction
        
        text = self.label2.text()
        self.label2.setText(text + " - ")
 
    def press_divbtn(self):                                  #method for dividation
        
        text = self.label2.text()
        self.label2.setText(text + " / ")
 
    def press_mulbtn(self):                                  #method for multiplication
        
        text = self.label2.text()
        self.label2.setText(text + " * ")
 
    def press_dotbtn(self): 

        text = self.label2.text()
        self.label2.setText(text + ".")
    def press_clear(self):
        
        self.label2.setText("")
 
    def press_del(self):                               #method for del
        
        text = self.label2.text()
        print(text[:len(text)-1])
        self.label2.setText(text[:len(text)-1])

    def perss_percentbtn(self):                       #method for percent
        text = self.label2.text()
        self.label2.setText(text + "%")

    def calculate_power(self):                         #method for power
        input_text = self.label2.text()
        
        base, exponent = map(float, input_text.split(','))
        result = base ** exponent
        self.label2.setText(f"Result: {result}")
    def press_equalbtn(self):
 
        
        equation = self.label2.text()
 
        try:
            
            ans = eval(equation)
 
            
            self.label2.setText(str(ans))
 
        except:
            
            self.label2.setText("Wrong Input")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        
        Form.setWindowTitle(_translate("Form", "calculator"))
        self.clear.setText(_translate("Form", "C"))
        self.num7btn.setText(_translate("Form", "7"))
        self.powbtn.setText(_translate("Form", "^"))
        self.num1btn.setText(_translate("Form", "1"))
        self.delbtn.setText(_translate("Form", "Del"))
        self.num8btn.setText(_translate("Form", "8"))
        self.num5btn.setText(_translate("Form", "5"))
        self.num2btn.setText(_translate("Form", "2"))
        self.zerobtn.setText(_translate("Form", "0"))
        self.dotbtn.setText(_translate("Form", "."))
        self.num3btn.setText(_translate("Form", "3"))
        self.num6btn.setText(_translate("Form", "6"))
        self.num9btn.setText(_translate("Form", "9"))
        self.percentbtn.setText(_translate("Form", "%"))
        self.dividebtn.setText(_translate("Form", "/"))
        self.mulbtn.setText(_translate("Form", "X"))
        self.subbtn.setText(_translate("Form", "-"))
        self.addbtn.setText(_translate("Form", "+"))
        self.equalbtn.setText(_translate("Form", "="))
        self.num4btn.setText(_translate("Form", "4"))
        self.label2.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
