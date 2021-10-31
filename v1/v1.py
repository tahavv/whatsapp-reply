from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import chromedriver_binary
from tkinter import *
from tkinter import ttk

#function
def send():
    name=number_entry.get()
    msg=msg_entry.get()
    count=count_entry.get()
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver , 600)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        button.click()
    


#mainscreen
root = Tk()
root.geometry('400x400')
root.columnconfigure(0,weight=1)
root.resizable(0,0)
root.title("Whatsapp message bomber")

#labels
num=StringVar()
msg=StringVar()
count=StringVar()

Label(root,text='Whatsapp message bomber',font=("jost",20),fg='gold2').grid()
Label(root,text="Type name or number to send:",font=("jost",15),fg='green').grid()

number_entry=Entry(root ,width=50, textvariable=num)
number_entry.grid()

Label(root,text="Type your message here:",font=("jost",15),fg='green').grid()
msg_entry=Entry(root ,width=50,textvariable=msg)
msg_entry.grid()

Label(root,text="Type number of messages here:",font=("jost",15),fg='green').grid()
count_entry=Entry(root ,width=50,textvariable=count)
count_entry.grid()

btn1=Button(root,text='START',font ="jost" ,bg ='green',fg='white',padx=50, command=send)
btn1.grid()

Label(root,text="You should open your whatsapp account by scanning QR code",font=("jost",10)).grid()
Label(root,text='and start sending .',font=("josh",10)).grid()


root.mainloop()
