from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('845x600')
root.title('Algebra')



def start():
    btn1 = Button(text = 'Числа та операції з ними', command = lambda: operaziyi())
    btn1.place(x = 0, y = 1 )
def operaziyi():
    label = Label(text = 'Виберіть вкладку', font = 'Times 15')
    label.place(x = 175, y = 1)
    btn2 = Button(text = 'Розкладання многочлена на множники', command = lambda: roz_na_mn_1())
    btn2.place(x = 150, y = 27)
    btn4 = Button(text = 'Формули скороченого множення', command = lambda: fsm())
    btn4.place(x = 150, y = 54)
    btn5 = Button(text = 'Операції з дробами', command = lambda: droby_tabs()).place(x= 150, y = 81)

def roz_na_mn_1():
    a = Label(text = 'a', font = "Times 15 italic", fg = '#008000')
    a.place(x = 415, y = 27)
    global a_e
    a_e = Entry(width = '4')
    a_e.place(x = 410, y = 54)
    c = Label(text = 'c', font = 'Times 15 italic', fg = '#008000')
    c.place(x = 460, y = 27)
    global c_
    c_ = Entry(width = '4')
    c_.place(x = 455, y = 54)
    plus = Label(text = '+')
    plus.place(x = 495, y = 52)
    x = Label(text = 'x')
    x.place(x = 440, y = 52 )
    a_1 = Entry(text = a_e.get(), width = '4')
    a_1.place(x = 520, y = 54)
    a_2 = Label(text = 'a', font = "Times 15 italic", fg = '#008000')
    a_2.place(x = 525, y = 27)
    x_ = Label(text = 'x')
    x_.place(x = 555, y = 52 )
    d = Label(text = 'd', font = "Times 15 italic", fg = '#008000')
    d.place(x = 575, y = 27)
    global d_
    d_ = Entry(width = '4')
    d_.place(x = 570, y = 54)
    dorivnyue = Label(text = '=', font = 'Times 15 italic', fg = '#008000')
    dorivnyue.place(x = 600, y = 50)
    dorivnyue_ = Label(text = 'a ( c + d )', fg = '#008000', font = 'Times 15 italic')
    dorivnyue_.place(x = 645, y = 25 )
    btn3 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_4(rezult_1))
    btn3.place(x = 450, y = 75)
    if a_1.get() != a_e.get():
        messagebox.showerror('Помилка', 'а не дорівнює а')



    a_3 = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 131)
    global a_4
    a_4 = Entry(width = '4')
    a_4.place(x = 410, y = 158)
    x_ = Label(text = 'x').place(x = 440, y = 156)
    d_1 = Label(text = 'd', font = 'Times 15 italic', fg = '#008000').place(x = 460, y = 131)
    global d_2
    d_2 = Entry(width = '4')
    d_2.place(x = 455, y = 158)
    plus = Label(text = '+').place(x = 495, y = 156)
    a_6 = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 525, y = 131)
    global a_5
    a_5 = Entry(width = '4')
    a_5.place(x = 520, y = 158)
    x_ = Label(text = 'x').place(x = 555, y = 156)
    c_1 = Label(text = 'c', font = 'Times 15 italic', fg = '#008000').place(x = 575, y = 131)
    global c_2
    c_2 = Entry(width = '4')
    c_2.place(x = 570, y = 158)
    b = Label(text = 'b', font = 'Times 15 italic', fg = '#008000').place(x = 640, y = 131)
    plus = Label(text = '+').place(x = 610, y = 156)
    global b_
    b_ = Entry(width = '4')
    b_.place(x = 635, y = 158)
    x_ = Label(text = 'x').place(x = 665, y = 156)
    d_3 = Label(text = 'd', font = 'Times 15 italic', fg = '#008000').place(x = 685, y = 131)
    global d_4
    d_4 = Entry(width = '4')
    d_4.place(x = 680, y = 158)
    plus = Label(text = '+').place(x = 715, y = 156)
    plus = Label(text = '+').place(x = 415, y = 210)
    b_2 = Label(text = 'b', font = 'Times 15 italic', fg = '#008000').place(x = 445, y = 183)
    global b_3
    b_3 = Entry(width = '4')
    b_3.place(x = 440, y = 212)
    x_ = Label(text = 'x').place(x = 470, y = 210)
    c_3 = Label(text = 'c', font = 'Times 15 italic', fg = '#008000').place(x = 490, y = 183)
    global c_4
    c_4 = Entry(width = '4')
    c_4.place(x = 485, y = 212)
    dorivnyue_6 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 515, y = 210)
    dorivnyue_7 = Label(text = '( d + c )(a + b )', font = 'Times 15 italic', fg = '#008000').place(x = 545, y = 178)
    btn6 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_3(rezult_3)).place(x = 450, y = 239)


    a_7 = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 283)
    global a_8
    a_8 = Entry(width = '4')
    a_8.place(x = 410, y = 310) 
    stepin = Label(text = '2m + 1', font = 'Times 10 italic', fg = '#008000').place(x = 435, y = 278)
    global stepin_
    stepin_ = Entry(width = '2')
    stepin_.place(x = 445, y = 300)
    minus = Label(text = '+', font = 'Times 15 italic', fg = '#008000').place(x = 470, y = 300)
    one = Label(text = '1', font = 'Times 15 italic', fg = '#008000').place(x = 500, y = 302.5)
    dorivnyue_8 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 530, y = 302.5)
    dorivnyue_9 = Label(text = '( a + 1 ) ', font = 'Times 15 italic', fg = '#008000').place(x = 560, y = 278)
    dorivnyue_10 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_7(rezult_7)).place(x = 450, y = 339)

def perehod_4(rezult_1):
    rezult_1()

def rezult_1():
    a_entry = a_e.get()
    c_entry = c_.get()
    d_entry = d_.get()
    dorivnyue_2 = a_entry + '•' + '(' + c_entry + '+' + d_entry + ')'
    dorivnyue_3 = Label(text = dorivnyue_2, font = 'Times 15 italic', fg = '#FF0000')
    dorivnyue_3.place(x = 645, y = 48)

def perehod_3(rezult_3):
    rezult_3()
def rezult_3():
    a_entry = a_4.get()
    b_entry = b_.get()
    c_entry = c_2.get()
    d_entry = d_2.get()
    dorivnyue_4 = '(' + d_entry + ' + ' + c_entry + ')(' + a_entry + ' + ' + b_entry + ')'
    dorivnyue_5 = Label(text = dorivnyue_4, font = 'Times 15 italic', fg = '#FF0000').place(x = 545, y = 207.5)

def perehod_7(rezult_7):
    rezult_7()
def rezult_7():
    a_entry = a_8.get()
    stepin_entry = stepin_.get()
    dorivnyuye = '(' + a_entry + ' +' + ' 1 ' + ')'
    dorivnyuye1 = Label(text = dorivnyuye , font = 'Times 15 italic', fg = '#FF0000').place(x = 560, y = 302.5)


def fsm():
    a = Label(text = '( a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 27)
    global a_
    a_= Entry(width = '4')
    a_.place(x = 420, y = 54)
    b= Label(text = 'b )', font = 'Times 15 italic', fg = '#008000').place(y = 27, x = 470)
    global b_
    b_= Entry(width = '4')
    b_.place(x = 465, y = 54)
    plus = Label(text = '+').place(x = 450, y = 52)
    x = Label(text = '•').place(x = 510,y = 52)
    a1 = Label(text = '( a', font = 'Times 15 italic', fg = '#008000').place(x = 535, y = 27)
    a_1 = Entry(width = '4').place(x = 535, y = 54)
    b1 = Label(text = 'b )', font = 'Times 15 italic', fg = '#008000').place(y = 27, x = 585)
    b_1 = Entry(width = '4').place(x = 580, y = 54)
    plus = Label(text = '+').place(x = 565, y = 52)
    dorivnyue_fsm_1 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 615, y = 50)
    dorivnyue_fsm_2 = Label(text = 'a² - b²', font = 'Times 15 italic', fg = '#008000').place(x = 650, y = 27)
    btn5 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_2(rezult_2)).place(x = 500, y = 75)


    a_2 = Label(text = '( a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 120)
    plus_minus = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000')
    plus_minus.place(x = 460, y = 120)
    global a_3
    a_3 = Entry(width = '4')
    a_3.place(x = 415,y = 147)
    global plus_minus_
    plus_minus_ = Entry(width = '4')
    plus_minus_.place(x = 460, y = 147)
    b_2 = Label(text = 'b )²', font = 'Times 15 italic', fg = '#008000').place(x = 505,y = 120)
    global b_3
    b_3 = Entry(width = '4')
    b_3.place(x = 505, y = 147)
    dorivnyue_fsm_1 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 545, y = 142.5)
    dorivnyue_fsm_4 = Label(text = 'a² +/- 2ab + b²', font = 'Times 15 italic', fg = '#008000').place(x = 580, y = 115)
    dorivnyue_fsm_5 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_4(rezult_4)).place(x = 500, y = 174)


    a_4 = Label(text = '( a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 219)
    global a_5
    a_5 = Entry(width = '4')
    a_5.place(x = 415, y = 244)
    plus_minus_2 = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000').place(x = 460, y = 219)
    global plus_minus_1
    plus_minus_1 = Entry(width = '4')
    plus_minus_1.place(x = 460, y = 244)
    b_4 = Label(text = 'b )', font = 'Times 15 italic', fg = '#008000').place(x = 505, y = 219)
    global b_5
    b_5 = Entry(width = '4')
    b_5.place(x = 505, y = 244)
    x_ = Label(text = '•', font = 'Times 15 italic', fg = '#008000').place(x = 550, y = 238)
    a_6 = Label(text = '( a²', font = 'Times 15 italic', fg = '#008000').place(x = 580, y = 219)
    global a_7
    a_7 = Entry(width = '4')
    a_7.place(x = 580, y = 244)
    plus_minus_3 = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000').place(x = 625, y = 219)
    global plus_minus_4
    plus_minus_4 = Entry(width = '4')
    plus_minus_4.place(x = 625, y = 244)
    a_8 = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 670, y = 219)
    global a_9
    a_9 = Entry(width = '4')
    a_9.place(x = 670, y = 244)
    x_1 = Label(text = '•', font = 'Times 15 italic', fg = '#008000').place(x = 715, y = 238)
    b_6 = Label(text = 'b²', font = 'Times 15 italic', fg = '#008000').place(x = 760, y = 219)
    global b_7
    b_7 = Entry(width = '4')
    b_7.place(x = 760, y = 244)
    plus_ = Label(text = '+', font = 'Times 15 italic', fg = '#008000').place(x = 805, y = 238)
    plus_ = Label(text = '+', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 276)
    b_8 = Label(text = 'b²', font = 'Times 15 italic', fg = '#008000').place(x = 465, y = 267)
    global b_9
    b_9 = Entry(width = '4')
    b_9.place(x = 460, y = 289)
    dorivnyue_fsm_6 = Label(text = 'a³ +/- b³', font = 'Times 15 italic', fg = '#008000').place(x = 550, y = 262    )
    dorivnyue_fsm_7 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 505, y = 286)
    dorivnyue_fsm_8 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_5(rezult_5)).place(x = 500, y = 316)



    a_10 = Label(text = '( a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 363)
    global a_11
    a_11 = Entry(width = '4')
    a_11.place(x = 415, y = 390)
    plus_minus_5 = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000').place(x = 460, y = 363)
    global plus_minus_6
    plus_minus_6 = Entry(width = '4')
    plus_minus_6.place(x = 460, y = 390)
    b_10 = Label(text = 'b )³', font = 'Times 15 italic', fg = '#008000').place(x = 505, y = 363)
    global b_11
    b_11 = Entry(width = '4')
    b_11.place(x = 505, y = 390)
    dorivnyue_fsm_11 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 550, y = 385)
    dorivnyue_fsm_12 = Label(text = '( a³ +/- 3a²b + 3ab² +/- b³ )', font = 'Times 15 italic', fg = '#008000').place(x = 595, y = 360)
    dorivnyue_fsm_13 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_6(rezult_6)).place(x = 500, y = 417)

def perehod_2(rezult_2):
    rezult_2()
def rezult_2():
    global a_entry
    a_entry = a_.get()
    global b_entry
    b_entry = b_.get()
    dorivnyue_fsm_3 = a_entry + '²' + ' - ' + b_entry + '²'
    dorivnyue_fsm_4 = Label(text = dorivnyue_fsm_3, font = 'Times 15 italic', fg = '#FF0000')
    dorivnyue_fsm_4.place(x = 645, y = 50)

def perehod_4(rezult_4):
    rezult_4()
def rezult_4():
    a_entry = a_3.get()
    b_entry = b_3.get()
    p_m_entry = plus_minus_.get()
    dorivnyue_fsm_1 = a_entry + '² ' + p_m_entry + ' 2 • ' + a_entry + ' • ' + b_entry + ' + ' + b_entry + '²'
    dorivnyue_fsm_2 = Label(text = dorivnyue_fsm_1, font = 'Times 15 italic', fg = '#FF0000').place(x = 580, y = 137)

def perehod_5(rezult_5):
    rezult_5()
def rezult_5():
    a_entry = a_5.get()
    b_entry = b_5.get()
    p_m_entry = plus_minus_4.get()
    dorivnyue_fsm_9 = a_entry + '³ ' + p_m_entry + ' ' + b_entry + '³'
    dorivnyue_fsm_10 = Label(text = dorivnyue_fsm_9, font = 'Times 15 italic', fg = '#FF0000').place(x = 550, y = 283.5)

def perehod_6(rezult_6):
    rezult_6()
def rezult_6():
    a_entry = a_11.get()
    b_entry = b_11.get()
    p_m_entry = plus_minus_6.get()
    if p_m_entry == '+':
        dorivnyue_fsm_14 = a_entry + '³ ' + '+ ' + '3 • ' + a_entry + '² • ' + b_entry + ' + ' + '3 • ' + a_entry + ' • ' + b_entry + '² + ' + b_entry + '³'
        root.geometry('900x600')
    if p_m_entry == '-':
        dorivnyue_fsm_14 = a_entry + '³ ' + '- ' + '3 • ' + a_entry + '² • ' + b_entry + ' + ' '3 • ' + a_entry + ' • ' + b_entry + '³ ' ' - ' + b_entry + '³'
        root.geometry('900x600')
    dorivnyue_fsm_15 = Label(text = dorivnyue_fsm_14, font = 'Times 15 italic', fg = '#FF0000').place(x = 595, y = 385)

def droby_tabs():
    tab = Button(text = 'Властивості дробів', borderwidth = '4').place(x = 400, y = 1)
    tab2 = Button(text = 'Дії з дробами', borderwidth = '4', command = lambda: droby_oper()).place(x = 520, y = 1)

def droby_oper():
    #Number 1
    #Text`s
    dodavanya = Label(text = 'Додавання та віднімання дробів', font = 'Times 15 italic').place(x = 410, y = 55)
    a = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 109)
    ryska = Label(text = '—', font = 'Times 15 italic', fg = '#008000').place(x = 410, y = 129)
    b = Label(text = 'b', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 149)
    plus_minus = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000').place(x = 440, y = 129)
    c = Label(text = 'c', font = 'Times 15 italic', fg = '#008000').place(x = 480, y = 109)
    ryska = Label(text = '—', font = 'Times 15 italic', fg = '#008000').place(x = 475, y = 129)
    b = Label(text = 'b', font = 'Times 15 italic', fg = '#008000').place(x = 480, y = 149)
    dorivnyue = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 505, y = 129)
    a_ = Label(text = 'a +/- c', font = 'Times 15 italic', fg = '#008000').place(x = 535, y = 126.5)
    #Entry`s
    global a_1
    a_1 = Entry(width = '4')
    a_1.place(x = 415, y = 189)
    ryska_ = Label(text = '——', font = 'Times 15 italic').place(x = 410, y = 209)
    global b_1
    b_1 = Entry(width = '4')
    b_1.place(x = 415, y = 239)
    global plus_minus_
    plus_minus_ = Entry(width = '4')
    plus_minus_.place(x = 460, y = 214)
    global c_2
    c_2 = Entry(width = '4')
    c_2.place(x = 500, y = 189)
    ryska_ = Label(text = '——', font = 'Times 15 italic').place(x = 495, y = 209)
    global b_2
    b_2 = Entry(width = '4')
    b_2.place(x = 500, y = 239)
    dorivnyue_ = Label(text = '=', font = 'Times 15 italic').place(x = 550, y = 209)
    dorivnyue_1 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_8(rezult_8)).place(x = 450, y = 269)
    #Number 2
    #Text`s
    e = Label(text = r'\ e', font = 'Times 13 italic', fg = '#008000').place(x = 435, y = 324)
    a_2 = Label(text = 'a', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 329)
    ryska = Label(text = '———', font = 'Times 15 italic', fg = '#008000').place(x = 410, y = 349)
    b_3 = Label(text = 'b  •  c', font = 'Times 15 italic', fg = '#008000').place(x = 415, y = 369)
    plus_minus = Label(text = '+/-', font = 'Times 15 italic', fg = '#008000').place(x = 475, y = 349)
    d = Label(text = 'd', font = 'Times 15 italic', fg = '#008000').place(x = 525, y = 329)
    b_3 = Label(text = r'\ b', font = 'Times 13 italic', fg = '#008000').place(x = 545, y = 324)
    ryska = Label(text = '———', font = 'Times 15 italic', fg = '#008000').place(x = 520, y = 349)
    e_ = Label(text = 'e  •  c', font = 'Times 15 italic', fg = '#008000').place(x = 525, y = 369)
    dorivnyue_2 = Label(text = '=', font = 'Times 15 italic', fg = '#008000').place(x = 585, y = 349)
    dorivnyue_3 = Label(text = 'a • e +/- d • b', font = 'TImes 15 italic', fg = '#008000').place(x = 615, y = 329)
    ryska = Label(text = '——————', font = 'Times 15 italic', fg = '#008000').place(x = 610, y = 349)
    dorivnyue_4 = Label(text = 'b • c • e', font = 'Times 15 italic', fg = '#008000').place(x = 625, y = 369)
    #Entry`s
    global a_3
    a_3 = Entry(width = '4')
    a_3.place(x = 415, y = 429)
    ryska = Label(text = '———', font = 'Times 15 italic').place(x = 415, y = 449)
    global e_1
    e_1 = Entry(width = '1')
    e_1.place(x = 450, y = 424)
    global b_5
    b_5 = Entry(width = '4')
    b_5.place(x = 415, y = 469)
    global c_3
    c_3 = Entry(width = '4')
    c_3.place(x = 450, y = 469)
    global plus_minus_2
    plus_minus_2 = Entry(width = '4')
    plus_minus_2.place(x = 485, y = 449)
    global d_3
    d_3 = Entry(width = '4')
    d_3.place(x = 525, y = 429)
    ryska = Label(text = '———', font = 'Times 15 italic').place(x = 525, y = 449)
    global b_4
    b_4 = Entry(width = '1')
    b_4.place(x = 560, y = 424)
    global e_2
    e_2 = Entry(width = '4')
    e_2.place(x = 525, y = 469)
    global c_4
    c_4 = Entry(width = '4')
    c_4.place(x = 560, y = 469)
    dorivnyue_5 = Label(text = '=', font = 'Times 15 italic').place(x = 595, y = 449)
    dorivnyue_6 = Button(text = 'Розрахувати', font = 'Times 15 italic', command = lambda: perehod_9(rezult_9)).place(x = 450, y = 499)






def perehod_8(rezult_8):
    rezult_8()
def rezult_8():
    a_entry = a_1.get()
    b_entry = b_1.get()
    c_entry = c_2.get()
    p_m_entry = plus_minus_.get()
    dorivnyue = a_entry + ' ' + p_m_entry + ' ' + c_entry
    dorivnyue_ch_r = Label(text = b_entry, font = 'Times 15 italic', fg = '#FF0000').place(x = 605, y = 234)
    dorivnyue_ryska = Label(text = '———', font = 'Times 15 italic', fg = '#FF0000').place(x = 595, y = 209)
    dorivnyue_ = Label(text = dorivnyue, font = 'Times 15 italic', fg = '#FF0000').place(x = 600, y = 189)

def perehod_9(rezult_9):
    rezult_9()
def rezult_9():
    a_entry = a_3.get()
    b_entry = b_4.get()
    c_entry = c_3.get()
    d_entry = d_3.get()
    e_entry = e_2.get()
    p_m_entry = plus_minus_2.get()
    dorivnyue = a_entry + ' • ' + e_entry + ' ' + p_m_entry + ' ' + d_entry + ' • ' + b_entry
    dorivnyue_ch_r = Label(text = '—————', font = 'Times 15 italic', fg = '#FF0000').place(x = 640, y = 449)
    dorivnyue_1 = Label(text = dorivnyue, font = 'Times 15 italic', fg = '#FF0000').place(x = 640, y = 429)
    dorivnyue_2 = Label(text = 'b • c • e', font = 'TImes 15 italic', fg = '#FF0000').place(x = 640, y = 469) 

start()
root.mainloop()
