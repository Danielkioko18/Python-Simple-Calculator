from tkinter import*
from tkinter import messagebox

def btnClick(numbers):
	global operator
	operator= operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")
def btnEqualInput():
   global operator
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=""

        
 
calc=Tk()
calc.title("MyCalculater")
calc.configure(background="white",borderwidth=5)
calc.resizable(0,0)
operator=""


text_Input=StringVar()
textDisplay =Entry(calc, font=('arial',15, 'bold'), textvariable=text_Input, bd=20,width=23, bg="powder blue", justify=RIGHT).grid(columnspan=4)
btn7=Button(calc, padx=20, pady=20, bd=8, text="7", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(7)).grid(column=0, row=1)
btn8=Button(calc, padx=20, pady=20, bd=8, text="8", fg="black", font=('arial', 15, 'bold'), bg="powder blue",command=lambda:btnClick(8)).grid(column=1,row=1)
btn9=Button(calc, padx=20, pady=20, bd=8, text="9", fg="black", font=('arial', 15, 'bold'), bg="powder blue",command=lambda:btnClick(9)).grid(column=2, row=1)
btn9=Button(calc, padx=20, pady=20, bd=8, text="+", fg="yellow", font=('arial', 14, 'bold'), bg="purple", command=lambda:btnClick("+")).grid(column=3, row=1)
btn4=Button(calc, padx=20, pady=20, bd=8, text="4", fg="black", font=('arial', 15, 'bold'), bg="powder blue",command=lambda:btnClick(4)).grid(column=0, row=2)
btn5=Button(calc, padx=20, pady=20, bd=8, text="5", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(5)).grid(column=1, row=2)
btn6=Button(calc, padx=20, pady=20, bd=8, text="6", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(6)).grid(column=2, row=2)
btn7=Button(calc, padx=20, pady=20, bd=8, text="-", fg="yellow", font=('arial', 16, 'bold'), bg="purple", command=lambda:btnClick("-")).grid(column=3, row=2)
btn1=Button(calc, padx=20, pady=20, bd=8, text="1", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(1)).grid(column=0, row=3)
btn2=Button(calc, padx=20, pady=20, bd=8, text="2", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(2)).grid(column=1, row=3)
btn3=Button(calc, padx=20, pady=20, bd=8, text="3", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(3)).grid(column=2, row=3)
btn7=Button(calc, padx=20, pady=20, bd=8, text="*", fg="yellow", font=('arial', 15, 'bold'), bg="purple", command=lambda:btnClick("*")).grid(column=3, row=3)
btn0=Button(calc, padx=20, pady=20, bd=8, text="0", fg="black", font=('arial', 15, 'bold'), bg="powder blue", command=lambda:btnClick(0)).grid(column=0, row=4)
btn7=Button(calc, padx=20, pady=20, bd=8, text="C", fg="red", font=('arial', 15, 'bold'), bg="green",command=btnClearDisplay).grid(column=1, row=4)
btn7=Button(calc, padx=20, pady=20, bd=8, text="=", fg="yellow", font=('arial', 15, 'bold'), bg="blue", command=btnEqualInput).grid(column=2, row=4)
btn7=Button(calc, padx=20, pady=20, bd=8, text="/", fg="yellow", font=('arial', 15, 'bold'), bg="purple", command=lambda:btnClick("/")).grid(column=3, row=4)

calc.mainloop()
