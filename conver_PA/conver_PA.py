import tkinter as tk

def convert_to_fahrenheit():
    celsius = float(tbCelsius.get())
    fahrenheit1 = (celsius * 9 / 5) + 32
    tbFarenheint.delete(0, tk.END)
    tbFarenheint.insert(0, str(fahrenheit1))

def convert_to_celsius():
    fahrenheit2 = float(tbFarenheint.get())   
    celsius2 = (fahrenheit2 - 32) * 5.0 / 9.0
    tbCelsius.delete(0, tk.END)
    tbCelsius.insert(0, str(celsius2))

ventana = tk.Tk()
ventana.title('Conversor de temperatura')



lbFarenheint = tk.Label(ventana, text="Fahrenheit")
lbFarenheint.grid(row=0, column=0)
tbFarenheint = tk.Entry(ventana)
tbFarenheint.grid(row=0, column=1)
btnFarenheint = tk.Button(ventana, text="F a C", command=convert_to_celsius)
btnFarenheint.grid(row=0, column=2)

lbCelsius = tk.Label(ventana, text="Celsius")
lbCelsius.grid(row=1, column=0)
tbCelsius = tk.Entry(ventana)
tbCelsius.grid(row=1, column=1)
btnCelsius = tk.Button(ventana, text="C a F", command=convert_to_fahrenheit)
btnCelsius.grid(row=1, column=2)

ventana.mainloop()

