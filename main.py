from tkinter import *
from tkinter import messagebox
from Pack import Pack
from Pack import Dog

pack = Pack()


def addToPackClick():
   dog = Dog(wieght.get(),height.get(),calassific.get(),sound.get(),food.get(),name.get(),age.get())
   pack.addNewDog(dog)
   messagebox.showinfo("Message", 'new dog added')

def deleteFromPack():
    pack.removeLastDog()
    messagebox.showinfo("Message", 'last god geleted')

def showPack():
    pack.showPack()

def sortPack():

    type=sortType.get()
    paramter = ""

    if type == 1:
        paramter = 'weight'
    if type == 2:
        paramter = 'height'
    if type == 3:
        paramter = 'classification'
    if type == 4:
        paramter = 'name'
    if type == 5:
        paramter = 'sound'
    if type == 6:
        paramter = 'food'
    if type == 7:
        paramter = 'age'

    pack.sortPack(paramter)
    print ('sorted by '+paramter)


def inputIntoFile():
    f=open('test.txt','a')
    f.writelines(wieght.get()+';'+height.get()+';'+calassific.get()+';'+sound.get()+';'+food.get()+';'+name.get()+';'+age.get()+'\n')
    f.close()
    messagebox.showinfo("Message", 'inserted into file')

def getFromFile():
    f = open('test.txt', 'r')
    for line in f:
        dog = Dog(line.split(';')[0], line.split(';')[1], line.split(';')[2], line.split(';')[3], line.split(';')[4], line.split(';')[5], line.split(';')[6])
        pack.addNewDog(dog)
    f.close()
    messagebox.showinfo("Message", 'Data got')

def clearFile():
    f = open('test.txt', 'w')
    f.write('')
    f.close()
    messagebox.showinfo("Message", 'file have been cleaned')

if __name__ == '__main__':
    root = Tk()

    sortType = IntVar()
    sortType.set(1)

    #RADIO BUTTONS
    weightSort = Radiobutton(text="Вес", value=1, variable=sortType)
    heightSort = Radiobutton(text="Рост", value=2, variable=sortType)
    calassificSort = Radiobutton(text="Класс", value=3, variable=sortType)
    soundSort = Radiobutton(text="Звук издаёт", value=4, variable=sortType)
    foodSort = Radiobutton(text="Корм", value=5, variable=sortType)
    nameSort = Radiobutton(text="Кличка", value=6, variable=sortType)
    ageSort = Radiobutton(text="Возраст", value=7, variable=sortType)

    weightSort.grid(row=0,column=3)
    heightSort.grid(row=1,column=3)
    calassificSort.grid(row=2,column=3)
    soundSort.grid(row=3,column=3)
    foodSort.grid(row=4,column=3)
    nameSort.grid(row=5,column=3)
    ageSort.grid(row=6,column=3)

    #ENTRIES
    wieght = Entry()
    height = Entry()
    calassific = Entry()
    sound = Entry()
    food = Entry()
    name = Entry()
    age = Entry()

    wieght.grid(row=0, column=1)
    height.grid(row=1, column=1)
    calassific.grid(row=2, column=1)
    sound.grid(row=3, column=1)
    food.grid(row=4, column=1)
    name.grid(row=5, column=1)
    age.grid(row=6, column=1)

    #LABELS
    wieghtLabel = Label(text='Рост: ')
    heightLabel = Label(text='Вес: ')
    calassificLabel = Label(text='Класс: ')
    soundLabel =Label(text='Звук издаёт: ')
    foodLabel = Label(text='Корм: ')
    nameLabel = Label(text='Кличка: ')
    ageLabel = Label(text='Возраст: ')

    wieghtLabel.grid(row=0,column=0)
    heightLabel.grid(row=1, column=0)
    calassificLabel.grid(row=2, column=0)
    soundLabel.grid(row=3, column=0)
    foodLabel.grid(row=4, column=0)
    nameLabel.grid(row=5, column=0)
    ageLabel.grid(row=6, column=0)



    #BUTTONS
    btn = Button(text="Добавить",  command=addToPackClick)
    btn2 = Button(text="Удалить", command=deleteFromPack)
    btn3 = Button(text="Просмотр", command=showPack)
    btn4 = Button(text="Сортировка", command=sortPack)
    btn5 = Button(text="Добавить в файл", command=inputIntoFile)
    btn6 = Button(text="Получить данные из файла", command=getFromFile)
    btn7 = Button(text="Очистить файл", command=clearFile)

    btn.grid(row=7, column=0,columnspan=3 )
    btn2.grid(row=8, column=0,columnspan=3)
    btn3.grid(row=9, column=0,columnspan=3)
    btn4.grid(row=10, column=0, columnspan=3)
    btn5.grid(row=11, column=0, columnspan=3)
    btn6.grid(row=12, column=0, columnspan=3)
    btn7.grid(row=13, column=0, columnspan=3)

    root.mainloop()
