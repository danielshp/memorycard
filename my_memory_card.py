from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint

class Questions():
    '''содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
questions_list= []
questions_list.append(Questions('В каком веке был образован Великий Шелковый Путь ','2в до нашей эры ','15в до нашей эры','10в нашей эры','1в  нашей эры'))
questions_list.append(Questions('Какое качество  человека плохое','ненависть','пунктуальность','доброта','ум'))
questions_list.append(Questions('Какой из вариантов животное','орел','дерево','телефон','чипсы'))
questions_list.append(Questions('Какой из вариантов растение','одуванчик','собака','человек','лейка'))
questions_list.append(Questions('Какая из стран существует','Бразилия','Мироляндия','Росыя','Старбург'))
questions_list.append(Questions('Какой из вариантов видеоигра','CS GO ','Телефон','пылесос','Компьютер'))
questions_list.append(Questions('Какой из вариантов видеоблогер','PewDiePie','Джон Уик','Big Bon ','Доширак'))
questions_list.append(Questions('Жить Здорово это:','телепередача','компания','имя и фамилия','Магазин'))
questions_list.append(Questions('Какая из игр появилась раньше','Half Life','Cyberpunk 2077','World of Warcraft','Counter-Strike: Source'))
questions_list.append(Questions('Кто такой Пикачу','покемон','человек','растение','картина'))
questions_list.append(Questions('Кто такой Киану Ривз','актер','строитель','врач','генерал армии'))
questions_list.append(Questions('продолжи название фильма: Безумный Макс ...','Дорога ярости','Дорога домой','и Пришельцы','и Ангелы'))
questions_list.append(Questions('Чему приблизительно равно число Пи','3,14','5,7','99,903','57,1'))
questions_list.append(Questions('какой из языков существует','немецкий','эльфийский','неполитанский','японкий'))
questions_list.append(Questions('продолжи название книги: Сунь Цзы ...','искусство войны','и семь мушкитеров','самый известный писатель',' и чипсы'))
questions_list.append(Questions('2000 год к какому относится веку','20 век','21 век','3 век','22 век'))
questions_list.append(Questions('какой  год был  после 1 года до нашей эры','1 год н.э',' 0 год н.э','-1 год н.э',' 45 год н.э'))
questions_list.append(Questions('продолжи: 1, 6 ,11, 17','22',' 21','-22',' 24'))
questions_list.append(Questions('какой из вариантов  самая бесполезная вещь','просмотр Рен ТВ','просмотр комедийных передач','просмотр любимого сериала','занятие спортом'))
questions_list.append(Questions('продолжи: 1, б ,3, г ','5','е','ж','7'))
questions_list.append(Questions('Что такое км/ч','единица измерения скорости','смысл жизни','тоже самое что и км/с','единица измерения времени'))
questions_list.append(Questions('1 правило бойцовкского клуба','никто не должен знать о бойцовском клубе','никаких яблок в бойцовском клубе','не спрашивай людей о смысле жизни','никогда не говори'))
questions_list.append(Questions('Что такое км/ч','единица измерения скорости','смысл жизни','тоже самое что и км/с','единица измерения времени'))
questions_list.append(Questions('Кто такой Лестер','персонаж гта 5','персонаж cyberpunk2077','персонаж из фильмов форсаж','актер'))
questions_list.append(Questions('Кто такой Копатыч','медведь из Смешариков','барсук из простоквашино','растение','вид птиц'))
app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
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
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''  
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Questions):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
 
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print("Статистика\n-Всего вопросов: ",window.total, "\n-Правильных ответов: ",window.score)
        print("Рейтинг: ", (window.score/window.total * 100,"%"))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print("Рейтинг: ", (window.score/window.total * 100,"%"))
def next_questions():
    window.total+=1
    print("Статистика\n-Всего вопросов: ",window.total, "\n-Правильных ответов: ",window.score)
    cur_question = randint(0,len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_Ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_questions()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score =0
window.total = 0
next_questions()
btn_OK.clicked.connect(click_Ok) 
window.show()
app.exec()
