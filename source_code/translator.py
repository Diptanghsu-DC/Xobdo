#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


# In[2]:


root=Tk()
root.geometry('1100x320')
root.resizable(0,0)
#root.iconbitmap('logo.simpli.co')
root['bg']='purple'
root.title('Language Translator by Mind Mavericks')
Label(root, text="Language Translator", font="Arial 20 bold").pack()


# In[3]:


Label(root, text="Enter Text", font="arial 13 bold", bg="white smoke").place(x=165, y=90)


# In[4]:


Input_text=Entry(root, width=60) #sets the dimension
Input_text.place(x=30, y=130) #sets the coordinates/location
Input_text.get()


# In[5]:


Label(root, text="Output", font="arial 13 bold", bg="white smoke").place(x=780,y=90)


# In[6]:


Output_text=Text(root, font="arial 10", height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600,y=130)
#root.mainloop()


# In[7]:


langauge=list(LANGUAGES.values())
dest_lang=ttk.Combobox(root, values=langauge, width=22)
dest_lang.place(x=130, y=160)
dest_lang.set("Choose Language")


# In[ ]:


def Translate():
    translator=Translator()
    translated=translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0,END)
    Output_text.insert(END, translated.text)
    
trans_button=Button(root, text="Translate", font="arial 12 bold", pady=5, command=Translate, bg='orange', activebackground='green')
trans_button.place(x=445, y=180)
root.mainloop()


# In[ ]:




