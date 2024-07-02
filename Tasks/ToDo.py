

#Task1
# Ttitle : To do list

'''the Design of this todo list is done in Qt designer using pyuic6 commnad the main ui file is converted in python code 
and then required methods have Addded '''




from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def add_task(self):
        # Get the text from the input fields
        item1 = self.task_edit.text()
        item2 = self.deadlin_edit.text()        
        # Check if both inputs are filled
        if item1 and item2:
            # Combine the inputs and add to the list widget
            combined_item = f"Task  : {item1}     -  Deadline :  {item2}"
            self.listWidget.addItem(combined_item)
        
            # Clear the input fields
            self.task_edit.clear()
            self.deadlin_edit.clear()
    def reset_task(self):
        self.listWidget.clear()   
    def delete_task(self):
        clicked=self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)
    def view_task(self):
        if self.listWidget.count()==0:
             QtWidgets.QMessageBox.information(self, "Warning", "Please add the task", QtWidgets.QMessageBox.StandardButton.Ok)
        else: 
             for index in range(self.listWidget.count()):
               item = self.listWidget.item(index)
             print(f"Item {index+1}: {item.text()}")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(782, 592)
        Form.setStyleSheet("")
        self.l1 = QtWidgets.QLabel(parent=Form)
        self.l1.setGeometry(QtCore.QRect(250, 30, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.l1.setFont(font)
        self.l1.setStyleSheet("color: rgb(0, 0, 0);")
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(parent=Form)
        self.l2.setGeometry(QtCore.QRect(110, 70, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        self.l2.setFont(font)
        self.l2.setStyleSheet("color: rgb(85, 0, 127);")
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(parent=Form)
        self.l3.setGeometry(QtCore.QRect(70, 130, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(False)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLabel(parent=Form)
        self.l4.setGeometry(QtCore.QRect(70, 185, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(14)
        font.setBold(False)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.task_edit = QtWidgets.QLineEdit(parent=Form)
        self.task_edit.setGeometry(QtCore.QRect(70, 150, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_edit.setFont(font)
        self.task_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_edit.setText("")
        self.task_edit.setObjectName("task_edit")
        self.deadlin_edit = QtWidgets.QLineEdit(parent=Form)
        self.deadlin_edit.setGeometry(QtCore.QRect(70, 210, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deadlin_edit.setFont(font)
        self.deadlin_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.deadlin_edit.setText("")
        self.deadlin_edit.setObjectName("deadlin_edit")
        self.addbtn = QtWidgets.QPushButton(parent=Form)
        self.addbtn.setGeometry(QtCore.QRect(120, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(15)
        font.setBold(True)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.addbtn.setObjectName("addbtn")
        self.viewbtn = QtWidgets.QPushButton(parent=Form)
        self.viewbtn.setGeometry(QtCore.QRect(270, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(15)
        self.viewbtn.setFont(font)
        self.viewbtn.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.viewbtn.setObjectName("viewbtn")
        self.deletebtn = QtWidgets.QPushButton(parent=Form)
        self.deletebtn.setGeometry(QtCore.QRect(400, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(15)
        font.setBold(True)
        self.deletebtn.setFont(font)
        self.deletebtn.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.deletebtn.setObjectName("deletebtn")
        self.resetbtn = QtWidgets.QPushButton(parent=Form)
        self.resetbtn.setGeometry(QtCore.QRect(520, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(15)
        font.setBold(True)
        self.resetbtn.setFont(font)
        self.resetbtn.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.resetbtn.setObjectName("resetbtn")
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(60, 320, 681, 241))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")

    # calling the methods here 
        #for adding the task
        self.addbtn.clicked.connect(self.add_task)
        #for reseting the widget
        self.resetbtn.clicked.connect(self.reset_task)
        #for delething the task
        self.deletebtn.clicked.connect(self.delete_task)
        #for viewing the task
        self.viewbtn.clicked.connect(self.view_task)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "To-Do List"))
        self.l1.setText(_translate("Form", "To-Do List Application"))
        self.l2.setText(_translate("Form", "Orginzational system always works so..review your To Do List....!"))
        self.l3.setText(_translate("Form", "Enter the Task"))
        self.l4.setText(_translate("Form", "Enter Deadline"))
        self.addbtn.setText(_translate("Form", "Add Task"))
        self.viewbtn.setText(_translate("Form", "View Tasks"))
        self.deletebtn.setText(_translate("Form", "Delete Task"))
        self.resetbtn.setText(_translate("Form", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
