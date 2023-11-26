from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)

menu_window = QWidget()

lb_question = QLabel("Введіть питання")
le_question = QLineEdit()

lb_answer = QLabel("Введіть правильну відповідь")
le_answer = QLineEdit()

lb_wrong1 = QLabel("Введдіть неправильний варіант1")
le_wrong1 = QLineEdit()

lb_wrong2 = QLabel("Введдіть неправильний варіант2")
le_wrong2 = QLineEdit()

lb_wrong3 = QLabel("Введдіть неправильний варіант3")
le_wrong3 = QLineEdit()

btn_add = QPushButton("Додати питання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

# menu_h_lines = [QHBoxLayout()]*6

menu_v_line = QVBoxLayout()

menu_h_line_1.addWidget(lb_question)
menu_h_line_1.addWidget(le_question)

menu_h_line_2.addWidget(lb_answer)
menu_h_line_2.addWidget(le_answer)

menu_h_line_3.addWidget(lb_wrong1)
menu_h_line_3.addWidget(le_wrong1)

menu_h_line_4.addWidget(lb_wrong2)
menu_h_line_4.addWidget(le_wrong2)

menu_h_line_5.addWidget(lb_wrong3)
menu_h_line_5.addWidget(le_wrong3)

menu_h_line_6.addWidget(btn_add)
menu_h_line_6.addWidget(btn_clear)

menu_v_line.addLayout(menu_h_line_1)
menu_v_line.addLayout(menu_h_line_2)
menu_v_line.addLayout(menu_h_line_3)
menu_v_line.addLayout(menu_h_line_4)
menu_v_line.addLayout(menu_h_line_5)
menu_v_line.addLayout(menu_h_line_6)

menu_v_line.addWidget(btn_back)

menu_window.setLayout(menu_v_line)