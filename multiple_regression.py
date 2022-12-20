import pandas as pd
import tkinter
from tkinter import *
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('landprice1.csv')

X = dataset.iloc[0: ,0:3].values
Y = dataset.iloc[0: ,3].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

#x_train1 = np.reshape(x_train, (-1,1))
#y_train1 = np.reshape(y_train, (-1,1))

#x_test1 = np.reshape(x_test, (-1,1))
#y_test1 = np.reshape(y_test, (-1,1))

lin_regressor = LinearRegression()
lin_regressor.fit(x_train, y_train)

def model_pred():
    area1 = entry1.get()
    area = int(area1)

    distance1 = entry2.get()
    distance = int(distance1)

    crime1 = entry3.get()
    crime = int(crime1)

    trans_variable = np.array([[area, distance, crime ]])
    pred_price = lin_regressor.predict(trans_variable)
    pred_price = str(pred_price)

    label1 = Label(window, text=pred_price, fg='White', font=("Arial", 25))
    label1.pack()

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

window = Tk()
window.geometry("300x300")
window.title("Land Price")

label1 = Label(window, text = "Enter Land Area in Thousand Sq-feet", fg='lightgreen', font=("Arial", 15))
label1.pack()
area = StringVar()
area.set("")
entry1 = Entry(window, textvariable=area, fg="White", width=15, font=("Arial", 15))
entry1.pack()

label2 = Label(window, text = "Enter Land Distance from City centre", fg='lightgreen', font=("Arial", 15))
label2.pack()
distance = StringVar()
distance.set("")
entry2 = Entry(window, textvariable=distance, fg="White", width=15, font=("Arial", 15))
entry2.pack()

label3 = Label(window, text = "Enter Land Crime rate of this region", fg='lightgreen', font=("Arial", 15))
label3.pack()
crime = StringVar()
crime.set("")
entry3 = Entry(window, textvariable=crime, fg="White", width=15, font=("Arial", 15))
entry3.pack()

pred_button = Button(window, text="Predict", fg='green', command=model_pred, height=2, width = 15)
pred_button.pack()


mainloop()