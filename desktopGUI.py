from tkinter import *
import fileinput
import aiml
bot=aiml.Kernel()
bot.learn("nikjoke.aiml")
WindowTitle = 'SKF-CHATBOT'

def ClickAction():
    EntryText = EntryBox.get("0.0",END)
    ChatLog.config(state=NORMAL)
    log = open('name.txt', 'r')
    user=log.read()
    log.close()
    ChatLog.insert(END, "\n\n"+user+": "+EntryText)
    temp = bot.respond(EntryText)
    if temp!="":
        ChatLog.insert(END, "\nSKF: "+temp)
        EntryBox.delete("0.0",END)
    else:
        ChatLog.insert(END, " Sorry unable to find, but you can add your answer in other textbox ")
        EntryBox1.config(state=NORMAL)
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    
def ClickAction1():
    temp2 = EntryBox1.get("0.0",END)
    if temp2!="\n":
        EntryText = EntryBox.get("0.0",END)
        aimltext='<category> <pattern>'+EntryText.upper()+'</pattern> <template>'+temp2+'</template> </category></aiml>'
        for line in fileinput.FileInput("nikjoke.aiml",inplace=1):
            line = line.replace("</aiml>",aimltext.replace('\n', ''))
            print (line)
        EntryBox1.delete("0.0",END)
        EntryBox1.config(state=DISABLED)
        bot.learn("nikjoke.aiml")
    EntryBox.delete("0.0",END)
    
def PressAction(event):
    EntryBox.config(state=NORMAL)
    ClickAction()
def DisableEntry(event):
    EntryBox.config(state=DISABLED)
def DisableEntry1(event):
    EntryBox.config(state=DISABLED)
def PressAction1(event):
    EntryBox1.config(state=DISABLED)
    ClickAction1()
    
base = Tk()
base.title(WindowTitle)
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.insert(END, "Welcome to chat bot...Say hii..\n")
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=30, text="Send", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)




EntryBox1 = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox1.bind("<Return>", DisableEntry1)
EntryBox1.bind("<KeyRelease-Return>", PressAction1)
EntryBox1.config(state=DISABLED)

SendButton1 = Button(base, font=30, text="Add\nAnswer", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction1)

scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=6, y=401, height=45, width=265)
SendButton.place(x=277, y=401, height=45)

EntryBox1.place(x=6, y=451, height=45, width=265)
SendButton1.place(x=277, y=451, height=45)
base.mainloop()