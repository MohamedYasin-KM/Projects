from tkinter import *
from googletrans import Translator
from gtts import gTTS
def translate_language():
    n1 = entry.get()
    n2 = Translator()
    n3 = drop_down.get()

    if n3 == "ENGLISH":
        change = "en"
    elif n3 == "TAMIL":
        change = "ta"
    elif n3 == "HINDI":
        change = "hi"
    elif n3 == "FRENCH":
        change = "fr"

    text_trans = n2.translate(n1, dest=change)
    t=text_trans.text
    gTTS(text=t, slow=False, lang=change)
    twolabel.config(text=t)


Lang_option = [
        "ENGLISH",
        "TAMIL",
        "HINDI",
        "FRENCH",

    ]

tk_window = Tk()
tk_window.title("LANGUAGE TRANSLATOR")
tk_window.geometry('600x400')
tk_window.config(bg='sky blue')



entry = Entry(tk_window, bg='white', fg='black', font=("Arial",28,"bold"))
entry.place(x=60, y=80)
drop_down = StringVar()
drop_down.set("Select Language")

List_lang = OptionMenu(tk_window, drop_down, *Lang_option)
List_lang.configure(bg='yellow', fg='red', font=("Arial", 28, "bold"))
List_lang.place(x=500, y=80)
twolabel = Label(tk_window, text="\t\t\t\t", bg="white", fg="black", font=("Arial", 28, "bold"))
twolabel.place(x=0, y=150)
twolabel = Label(tk_window, text="Translated language", bg="violet", fg="pink", font=("Arial", 28, "bold"))
twolabel.place(x=220, y=150)
t_b = Button(tk_window, text="Translate!", bg="grey", fg="white", font=("Arial", 28, "bold"), command=translate_language)
t_b.place(x=220, y=220)
tk_window.mainloop()