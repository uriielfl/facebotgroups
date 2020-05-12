from tkinter.ttk import Frame 
from tkinter.ttk import Entry
from tkinter.ttk import Label
#from tkinter.ttk import Button
from ttkthemes import themed_tk as Tk
from ttkthemes import ThemedStyle
from tkinter import Button
from tkinter.ttk import Separator
from tkinter.ttk import LabelFrame
from tkinter import Text
from tkinter.ttk import Treeview
import tkinter.font as tkFont





lgn_Screen = Tk.ThemedTk()
lgn_Screen.title("Facebook Bot")
lgn_Screen.resizable(0,0)
style = ThemedStyle(lgn_Screen)
style.set_theme("arc")

class main():
    def __init__(self, tk):

        self.frame_lgn = Frame(lgn_Screen, width = 450, height = 750)
        self.frame_lgn.pack()
      
        #Separator
        self.pane_W = LabelFrame(lgn_Screen,text = 'Your Credentials' ,width = 300,height =200 )
        self.pane_W.place(x=1,y=10)

        #Login Entry
        self.usr_label = Label(lgn_Screen, text="Usuário:")
        self.usr_label.place(x=22,y=53)
        self.usr_entry = Entry(lgn_Screen, width = 25)
        self.usr_entry.place(x=72,y=50)
        #Passowrd Entry
        self.pw_label = Label(lgn_Screen, text="Senha:")
        self.pw_label.place(x=30,y=103)
        self.pw_entry = Entry(lgn_Screen, show="*", width = 25)
        self.pw_entry.place(x=72,y=100)
        
        def validate():
            usr = str(self.usr_entry.get())
            pw = str(self.pw_entry.get())

            print(usr)
            print(pw)

       

        #Separator message
        self.pane_W_Text= LabelFrame(lgn_Screen,text = 'Your Message:' ,width = 300,height =200 )
        self.pane_W_Text.place(x=1,y=210)
        #textbox 
        self.tb = Text(lgn_Screen, width = 35, height = 8, borderwidth = 0)
        self.tb.place(x=7,y=225)

        #Separator data
        self.pane_groups= LabelFrame(lgn_Screen,text = 'Seus Grupos aparecerão aqui:' ,width = 300,height =200 )
        self.pane_groups.place(x=1,y=410)
        
        self.tvGroups = Treeview(lgn_Screen)
        self.tvGroups.place(x=7, y=425,width = 287, height = 130)

        #Aviso de Botão
        fontStyle = tkFont.Font(size = 8)
        self.advcLbl  = Label(lgn_Screen, text = "* Aviso: o botão para confirmar o grupo será \nliberado em breve!", font = fontStyle)
        self.advcLbl.place(x=7,y=610)
        def conf_Message():
            msg = str(self.tb.get('1.0', 'end-1c'))
            print(msg)
            from selenium import webdriver
            from time import sleep 
            from selenium.webdriver.common.keys import Keys
            
            url = "https://facebook.com/"
            d = webdriver.Chrome()
            d.get(url)


            sleep(2)

            target_user = d.find_element_by_xpath('//*[@id="email"]')
            target_pw = d.find_element_by_xpath('//*[@id="pass"]')
            target_user.click()
            sleep(2)
            target_user.send_keys(str(self.usr_entry.get()))
            sleep(2)
            target_pw.send_keys(str(self.pw_entry.get()))
            sleep(6)
            log_in = d.find_element_by_xpath('//*[@id="u_0_b"]')
            sleep(1)
            log_in.click()
            sleep(3)
            webdriver.ActionChains(d).send_keys(Keys.ESCAPE).perform()
            sleep(4)
            explore_Group = d.find_element_by_xpath('//*[@id="navItem_1434659290104689"]/a/div')
            explore_Group.click()
            sleep(3)
            webdriver.ActionChains(d).send_keys(Keys.ESCAPE).perform()
            sleep(1)
            try:
                while True:
                    see_more = d.find_element_by_xpath("//*[contains(text(), 'Ver mais')]")
                    see_more.click()
                    sleep(2)
            except:
                pass
            sleep(3)
            groups = d.find_elements_by_class_name('_2yaa')
            l_groups = []
            for g_names in groups:
                l_groups.append(str(g_names.text))
            
            
            print(l_groups)
            group_index = []
            counter = 0
            for j in l_groups[:-1]:
                if str(j) == 'Descobrir':
                    continue
                print(str(counter)+" - "+str(j))
                counter += 1
                self.tvGroups.insert('', 'end', text = j)
            
            
            #selected_Group = ""
            def confirmGroup():
                self.cur = self.tvGroups.focus()
                self.selectedItem = str(self.tvGroups.item(self.cur)['text'])
                print(self.selectedItem)


                openGroup = d.find_element_by_xpath("//*[contains(text(), '"+ self.selectedItem +"')]")
                openGroup.click()
                sleep(6)
                postit = d.find_element_by_xpath("//*[@name='xhpc_message_text']")
                postit.send_keys(str(self.tb.get('1.0', 'end-1c')))
                sleep(5)
                publish = d.find_element_by_class_name('_332r')
                publish.click()
            self.selgroup = Button(lgn_Screen, text = "Confirmar", width = 10, font = 'Verdana 8', borderwidth = 0, bg = '#FFFFFF', fg = '#363636', command = confirmGroup )
            self.selgroup.place(x=175,y=570)
            
            
        self.cnf_Msg = Button(lgn_Screen, text = "Confirmar", width = 10, font = 'Verdana 8', borderwidth = 0, bg = '#FFFFFF', fg = '#363636', command = conf_Message)        
        self.cnf_Msg.place(x=175,y=370, height = 20)
        
        #Separator data
        


windows_WIDTH = lgn_Screen.winfo_reqwidth()
windows_HEIGHT = lgn_Screen.winfo_reqheight()
positionHORIZONTAL = int(lgn_Screen.winfo_screenwidth()/2 - windows_WIDTH/2)
positionVERTICAL = int(lgn_Screen.winfo_screenheight()/2 - windows_HEIGHT/2)
lgn_Screen.geometry("303x643+{}+{}".format(positionVERTICAL + 650,positionHORIZONTAL-750))
main(lgn_Screen)
lgn_Screen.mainloop()
