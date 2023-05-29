from tkinter import *
from currency_converter import CurrencyConverter

class CurrencyConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")

        self.input_currency_label = Label(master, text="From currency:")
        self.input_currency_label.pack()

        self.input_currency = Entry(master)
        self.input_currency.pack()

        self.input_amount_label = Label(master, text="Amount:")
        self.input_amount_label.pack()

        self.input_amount = Entry(master)
        self.input_amount.pack()

        self.output_currency_label = Label(master, text="To currency:")
        self.output_currency_label.pack()

        self.output_currency = Entry(master)
        self.output_currency.pack()

        self.output_amount_label = Label(master, text="Output:")
        self.output_amount_label.pack()

        self.output_amount = Label(master, text="")
        self.output_amount.pack()

        self.convert_button = Button(master, text="Convert", command=self.converter)
        self.convert_button.pack()

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.input_currency.get()
        output_currency = self.output_currency.get()
        input_amount = int(self.input_amount.get())
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.output_amount.config(text=str(output_amount))


root = Tk()
my_gui = CurrencyConverterGUI(root)
root.mainloop()