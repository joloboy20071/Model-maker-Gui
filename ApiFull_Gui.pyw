
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from tkinter.ttk import *

import easygui
import os
import threading
import webbrowser
import threading

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

import os as yourmother
import sys
from asyncio.windows_events import NULL
from distutils.log import error
from xml.dom.minidom import Element
from bs4 import BeautifulSoup
from lxml import etree
import requests


# File Frame
def fileframe():
# Frames
    global fiframe
    global filist_frame
    global fibutton_frame
# Lebels
    global fipassword_lable
    global fisalt_lable
    global fi_selectfile_label
# boxes
    global fipasswordbox
    global fisaltbox
    global filistbox
# knoppen
    global browsefi
    global file_enc_button
    global file_dec_button

# Input Box + knop
    fiframe = tk.LabelFrame(root, text='   Models maker  ',font='Raleway 19 bold',padx=10,pady=10)
    fiframe.grid(row=0,column=0,padx=40,pady=20)



# Lijst + Scroll Bar
    filist_frame = tk.Frame(fiframe)
    filist_frame.grid(row=3, columnspan=2)

    fiscroll = tk.Scrollbar(filist_frame, orient='vertical')
    fiscroll.grid(row=3,column=2, sticky='NSW')

    filistbox = tk.Listbox(filist_frame, width=50,height=10,font='Raleway 13')
    filistbox.grid(row=3,columnspan=2, pady=10)

    filistbox.config(yscrollcommand=fiscroll.set)
    fiscroll.config(command=filistbox.yview)


# knop
    fibutton_frame = tk.Frame(fiframe)
    fibutton_frame.grid(row=4, columnspan=2)
    
    browsefi = tk.Button(fiframe, text='Browse', font='Raleway 15 bold', width=20, command=file, borderwidth=3)
    browsefi.grid(row=2,column=1,padx=5, pady=5)


    file_enc_button = tk.Button(fibutton_frame, text='start',font='Raleway 15 bold', width=15,command=threadingst, borderwidth=3)
    file_enc_button.grid(row=4,column=0,padx=30,pady=15)


# kleur verandering
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='white', bg='black'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='white', bg='#575757'))



# Folder Frame
def folderframe():

    global foframe
    global folist_frame
    global fobutton_frame

    global fo_selectfolder_label

    global folistbox

    global browsefo
    global fold_enc_button
    global fold_dec_button

# Input Box + knop









# Progress Bar
def progbar():
    global pb_lable
    global percent
    global pbar
    global percentlabel
    global darkmodebtn
    global pbar_frame

    pb_lable = tk.Label(root, text=' |      Progress      | ', bg="#B0FF84", font = "Raleway 13 bold")
    pb_lable.grid(row=4, columnspan=2, sticky='w', padx=35)

    darkmodebtn = tk.Button(root, text='Turn Off Darkmode', bg='#B0FF84', font='Raleway 13 bold', borderwidth=1, relief="solid",width=20, command=switch)
    darkmodebtn.grid(row=4, columnspan=2, sticky='e', padx=35)

    pbar_frame = tk.Frame(root)
    pbar_frame.grid(row=6, columnspan=2)

    pbar = Progressbar(pbar_frame,orient='horizontal',length=675,mode='determinate')
    pbar.grid(row=6,column=0, pady=(0,20))

    percent = tk.StringVar()

    percentlabel = tk.Label(root, textvariable=percent, font='Raleway 15')
    percentlabel.grid(row=4,columnspan=2,pady=10, padx=200, sticky='w')





# DarkMode Function
global is_on
is_on = True
def switch():
    global is_on
    if is_on:
        darkmodeon()
        darkmodebtn.config(text='Turn Off Darkmode')
        is_on = False
    else:
        darkmodebtn.config(text='Turn On Darkmode')
        darkmodeoff()
        is_on = True

def darkmodeon():

    browsefi['bg']='#575757'
    browsefi['fg']="white"

    filistbox['bg']='#575757'
    filistbox['fg']='white'

    file_enc_button['bg']='#575757'
    file_enc_button['fg']='white'


    pb_lable['fg']='black'
    percentlabel['bg']='black'
    percentlabel['fg']='white'
    pbar_frame['bg']='black'

    root['bg']='black'
    fiframe['bg']='black'
    fiframe['fg']='white'
    filist_frame['bg']='black'
    fibutton_frame['bg']='black'


   

 
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='white', bg='black'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='white', bg='#575757'))





def darkmodeoff():
    
    browsefi['bg']='#F0F0F0'
    browsefi['fg']='black'

    filistbox['bg']='white'
    filistbox['fg']='black'

    file_enc_button['bg']='#F0F0F0'
    file_enc_button['fg']='black'




    pb_lable['fg']='black'
    percentlabel['bg']='#F0F0F0'
    percentlabel['fg']='black'
    pbar_frame['bg']='#F0F0F0'

    root['bg']='#F0F0F0'
    fiframe['bg']='#F0F0F0'
    fiframe['fg']='black'
    filist_frame['bg']='#F0F0F0'
    fibutton_frame['bg']='#F0F0F0'

 
    
    file_enc_button.bind("<Enter>", lambda e: file_enc_button.config(fg='black', bg='#D0D0D0'))
    file_enc_button.bind("<Leave>", lambda e: file_enc_button.config(fg='black', bg='#F0F0F0'))






#

    

def fidecdone1():
    
    pbar['value']=25
    percent.set('25%')
    

def fidecdone2():
    pbar['value']=50
    percent.set('50%')
    


def fidecdone():
    pbar['value']=100
    percent.set('100%')
    file_enc_button['state']='active'
    tk.messagebox.showinfo('Klaar','Alle files zijn gemaakt')
def buttoninactive():
    file_enc_button['state']='disabled'

rice_array2 = ["test-series \n"]
price_array = []


def file():
    txt = easygui.fileopenbox()
    text = open(txt).read()
    url = text.replace("+", "").replace("5G", " ").replace(" ", "-").replace("--","").replace("Fan-Edition", "fe").replace("4G", "").replace("Lite","").split("\n")

    for i in url:
        price_array.append(f"https://www.telefoonmaken.nl/{i}-reparatie/")
        

print("")
def scherm():
    
    x = 0
    while x < 100:
        try:
            HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                        'Accept-Language': 'en-US, en;q=0.5'})

            webpage = requests.get(price_array[x], headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            dom = etree.HTML(str(soup))
            element = dom.xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[2]/div/div[1]/div/div[7]/div/table/tbody/tr[1]/td[2]/strong')[0].text
            splitted = element.split(" ")
            price = splitted[1]

            price_string = str(price)

            file = open("AA Pending/price_scherm.txt", "a")
            file.write("€"+price_string+"\n")
            filistbox.insert('end',(price+price_array[x]))
            x+=1
        except:
            file = open("AA Pending/price_scherm.txt", "a")
            file.write("Op Aanvraag "+"\n")
            x +=1
            filistbox.insert('end',IndexError)
            

def batt():
    y = 0
    while y < 100:
        try:
            HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                        'Accept-Language': 'en-US, en;q=0.5'})

            webpage = requests.get(price_array[y], headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            dom = etree.HTML(str(soup))
            element = dom.xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[2]/div/div[1]/div/div[7]/div/table/tbody/tr[2]/td[2]/strong')[0].text
            splitted = element.split(" ")
            price = splitted[1]

            price_string = str(price)

            file = open("AA Pending/price_batterij.txt", "a")
            file.write("€"+price_string+"\n")
            filistbox.insert('end',(price+price_array[y]))
            y+=1
        except:
            file = open("AA Pending/price_batterij.txt", "a")
            file.write("Op Aanvraag "+"\n")
            y +=1
            filistbox.insert('end',IndexError)
            

def pricemake():
    schermt = open("schermen.html","r")
    schermtemplate = schermt.read()
    batterijt = open("batterij.html","r")
    batterijtemplate = batterijt.read()
    waterschadet = open("waterschade.html","r")
    waterschadetemplate = waterschadet.read()
    overiget= open("overige.html","r")
    overigetemplate = overiget.read()

    m = open("AA Pending/modellen.txt","r").read()
    models = str(m).split("\n")

    sline = 0
    bline = 0
    for currentmodel in models:
        sfile = open("AA Pending/price_scherm.txt","r")
        scherm_all_lines = sfile.readlines()

        newschermdata = str(schermtemplate).replace("EDITMODEL",str(currentmodel)).replace("LINKMODEL",(currentmodel.lower().replace(" ","-"))).replace("PLACEHOLDER", str(scherm_all_lines[sline]))
        newschermfile = open("Schermen/"+str(currentmodel)+".html","w")
        newschermfile.write(str(newschermdata))


        bfile = open("AA Pending/price_batterij.txt","r")
        batterij_all_lines = bfile.readlines()

        newbatterijdata = str(batterijtemplate).replace("EDITMODEL",str(currentmodel)).replace("LINKMODEL",(currentmodel.lower().replace(" ","-"))).replace("PLACEHOLDER", str(batterij_all_lines[sline]))
        newbatterijfile = open("Batterijen/"+str(currentmodel)+".html","w")
        newbatterijfile.write(str(newbatterijdata))
        filistbox.insert('end',currentmodel)


        newwaterschadedata = str(waterschadetemplate).replace("EDITMODEL",str(currentmodel)).replace("LINKMODEL",(currentmodel.lower().replace(" ","-")))
        newwaterschadefile = open("Waterschade/"+str(currentmodel)+".html","w")
        newwaterschadefile.write(str(newwaterschadedata))

        newoverigedata = str(overigetemplate).replace("EDITMODEL",str(currentmodel)).replace("LINKMODEL",(currentmodel.lower().replace(" ","-")))
        newoverigefile = open("Overige/"+str(currentmodel)+".html","w")
        newoverigefile.write(str(newoverigedata))
        sline = sline + 1
        bline = bline + 1

def modelmake():
    buttoninactive()
    filistbox.insert('end',"Modelen worden gemaakt")
    scherm()
    fidecdone1()
    batt()
    fidecdone2()
    pricemake()
    fidecdone()

def threadingst():
        trd=threading.Thread(target=modelmake)
        trd.start()



root = tk.Tk()

root.resizable(False,False)
root.title('Model maker')
fileframe()
folderframe()
progbar()
percent.set('0%')
darkmodeon()



root.mainloop()
