import pandas as pd
import tkinter
from tkinter import *
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('landprice.csv')

X = dataset.iloc[0: ,0].values
Y = dataset.iloc[0: ,-1].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

x_train1 = np.reshape(x_train, (-1,1))
y_train1 = np.reshape(y_train, (-1,1))

x_test1 = np.reshape(x_test, (-1,1))
y_test1 = np.reshape(y_test, (-1,1))

lin_regressor = LinearRegression()
lin_regressor.fit(x_train1, y_train1)

def model_pred():
    area1 = entry.get()
    area = int(area1)

    trans_area = np.array([[ area ]])
    pred_price = lin_regressor.predict(trans_area)
    pred_price = str(pred_price)

    label1 = Label(window, text=pred_price, fg='White', font=("Arial", 25))
    label1.pack()

window = Tk()
window.geometry("300x300")
window.title("Land Price")
label = Label(window, text = "Enter Land Area in Thousand Sq-feet", fg='lightgreen', font=("Arial", 15))
label.pack()

area = StringVar()
area.set("")

entry = Entry(window, textvariable=area, fg="White", width=15, font=("Arial", 15))
entry.pack()

pred_button = Button(window, text="Predict", fg='green', command=model_pred, height=2, width = 15)
pred_button.pack()


mainloop()