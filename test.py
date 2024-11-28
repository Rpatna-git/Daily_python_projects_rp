from PyQt6.QtWidgets import QApplication,QVBoxLayout,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton

import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid=QGridLayout()

        name_label=QLabel("Name:")
        self.name_line_edit=QLineEdit()
        calculate_button=QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label=QLabel()

        birth_date_label=QLabel("Birth date MM/DD/YYYY:")
        self.birth_date_edit=QLineEdit()

        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(birth_date_label,1,0)
        grid.addWidget(self.birth_date_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)


        self.setLayout(grid)
    def calculate_age(self):
        current_year=datetime.now().year
        user_date_if_birth=datetime.strptime(self.birth_date_edit.text(),"%m/%d/%Y").year
        age=current_year - user_date_if_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} year's old ")




app=QApplication(sys.argv)
age_calculator =AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
