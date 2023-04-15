from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox
app = QApplication([])
main_win = QWidget()
mainLayout = QVBoxLayout()
Layout_top = QHBoxLayout()
Layout_Box = QHBoxLayout()
Layout_Answer = QHBoxLayout()
main_win.setWindowTitle('Memory Card')
question = QLabel('2+2*2=?')
RadioGroupBox = QGroupBox('Варианты ответов')
ButtonGroup = QButtonGroup()
rbtn_1 = QRadioButton('6')
rbtn_2 = QRadioButton('4')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('8')

ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnswerButton = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Результат теста')
answer = QLabel('6')
RAnswer = QLabel('Правильный ответ')
AnswerLayout = QVBoxLayout()
AnswerLayout.addWidget(answer)
AnswerLayout.addWidget(RAnswer)
AnsGroupBox.setLayout(AnswerLayout)
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

Layout_top.addWidget(question)
Layout_Box.addWidget(RadioGroupBox)
Layout_Box.addWidget(AnsGroupBox)
Layout_Answer.addWidget(AnswerButton)

mainLayout.addLayout(Layout_top)
mainLayout.addLayout(Layout_Box)
mainLayout.addLayout(Layout_Answer)
main_win.setLayout(mainLayout)
AnsGroupBox.hide()
 
main_win.total = 0
main_win.col_right = 0
nom_question = []

def show_question():
    AnsGroupBox.hide()
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)
    RadioGroupBox.show()
    AnswerButton.setText('Ответить')

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    AnswerButton.setText('Следующий вопрос')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.question)
    show_question()

def show_correct(res):
    RAnswer.setText(str(res))
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.col_right +=1
        show_correct(True)
    else:
        show_correct(False)

class Question():
    def __init__(self,question,right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

def click_on():
    if AnswerButton.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def next_question():
    
    current_question = randint(0, len(question_list) - 1)
    if not current_question in nom_question:
        nom_question.append(current_question)
        main_win.total +=1
        answer.setText(question_list[current_question].right_answer)
        print('Всего вопросов:', main_win.total)
        print('Верных ответов:', main_win.col_right)
        print('Рейтинг:', int(main_win.col_right / main_win.total * 100), '%')
        print(nom_question)
        ask(question_list[current_question])
    else:
        next_question()

    if len(nom_question) == main_win.total:
        print('Вопросы закончились')

question_list = [Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Французский', 'Испанский'), Question('Государственный язык России', 'Русский', 'Российский', 'Украинский', 'Беларусский'), Question('Государственный язык Германии', 'Немецкий', 'Российский', 'Германский', 'Русский')]
AnswerButton.clicked.connect(click_on)

main_win.show()
app.exec_()