import pathlib
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic   

from models.student_model import StudentModel

class StudentForm(QWidget):
    student_saved= pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self._studentHandler = StudentModel()
        mod_path= pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/student_form.ui",self)
        self.saveButton.clicked.connect(lambda: self.save_student())
        self.cancelButton.clicked.connect(lambda: self.close())
        self.student_id = None

    def save_student(self):
        if self.student_id: 
            self._studentHandler.update_student(
                self.student_id,
                self.firstNameTextField.text(),
                self.lastNameTextField.text(),
                self.emailTextField.text()
            )
        else:
            self._studentHandler.create_student(
                self.firstNameTextField.text(),
                self.lastNameTextField.text(),
                self.emailTextField.text()
            )
                
        self.student_saved.emit()
        self.close()
    
    def load_student_data(self,student_id):
        self.student_id = student_id
        student_data = self._studentHandler.get_student_by_id(student_id)
        if student_data:
            self.firstNameTextField.setText(student_data[1]),
            self.lastNameTextField.setText(student_data[2]),
            self.emailTextField.setText(student_data[3])
            
    def reset_form(self):
        self.firstNameTextField.setText(""),
        self.lastNameTextField.setText(""),
        self.emailTextField.setText("")
        self.student_id = None