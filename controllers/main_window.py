from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QPushButton
from PyQt5 import uic
from models.student_model import StudentModel
from controllers.student_form import StudentForm
import pathlib
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        root_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(root_path / "views/main_window.ui", self)
        self._student_model = StudentModel()
        self.load_students()
        self._student_new = StudentForm()
        self.newEstudentAction.triggered.connect(lambda: self.create_student())
        self._student_new.student_saved.connect(self.load_students)

        
    def load_students(self):
        students_list = self._student_model.get_students()
        self.studentsTable.setRowCount(len(students_list))
        self._studentDBHandler = StudentModel()
        for i, student in enumerate(students_list):
            id, first_name, last_name, email = student
            self.studentsTable.setItem(i, 0, QTableWidgetItem(str(id)))
            self.studentsTable.setItem(i, 1, QTableWidgetItem(str(first_name)))
            self.studentsTable.setItem(i, 2, QTableWidgetItem(str(last_name)))
            self.studentsTable.setItem(i, 3, QTableWidgetItem(str(email)))
            self.studentsTable.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

            edit_button = QPushButton ("Editar")
            edit_button.clicked.connect(self.edit_student)
            edit_button.setProperty("row", i)
            self.studentsTable.setCellWidget(i, 4, edit_button)
            
    def edit_student(self):
        sender = self.sender()
        row = sender.property("row")
        student_id = self.studentsTable.item(row, 0).text()
        self._student_new.load_student_data(student_id)
        self._student_new.show()
    
    def create_student(self):
        self._student_new.reset_form()
        self._student_new.show()


    def closeEvent(self, ev) -> None:
        self._student_model.close()
        return super().closeEvent(ev)
