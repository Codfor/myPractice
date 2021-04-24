from tkinter import *
word_gui = Tk()

# create label
tile_label = Label(word_gui, text='word counter')
# adding the label to the centre gui screen
tile_label.pack()

tx_field_lable= Label(word_gui, text='entre you text here')
tx_out_label = Label(word_gui, text= 'counting results')

tx_field_lable.grid(row=0, column=0)
tx_out_label.grid(row=2, column=2)



# keeps the gui running
word_gui.mainloop()

