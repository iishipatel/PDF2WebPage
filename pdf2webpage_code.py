from tkinter import *
from tkinter import messagebox
import PyPDF2
import webbrowser
window = Tk()
window.title("PDF TO HTML CONVERTER")
window.configure(background="PeachPuff")
lbl = Label(window, text="PDF TO HTML CONVERTER",font=('Times New Roman',15,'bold')).pack(side='top')
def clicked():
    new_window=Tk()
    new_window.configure(background='PeachPuff')
    new_window.title('INPUT FILE')
    lbl1=Label(new_window,text='ENTER PDF',font=('Times New Roman',15,'bold')).pack(side='top')
    txt = Entry(new_window,width=10).pack(side='left')
    btn2=Button(new_window,text='CONVERT',font=('Times New Roman',10,'bold'),bg='orange',command=convert).pack(side='right')
def convert():
    html_code='<html>\n<body>\n'
    pdfFileObj = open(str(txt), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range (pdfReader.numPages):
        page_code='<h1>PAGE NO. '+str(i)+'</h1>\n'
        pageObj = pdfReader.getPage(i)
        c= pageObj.extractText()
        page_code='<p>'+c+'</p>\n'
        html_code+=page_code
    html_code+='</body></html>'
    pdfFileObj.close()
    for i in range (len(str(txt))):
        if str(txt)[i]=='.':
            d=str(txt)[:i]
    f = open(d+'.html','w')
    message = html_code
    f.write(message)
    f.close()
    webbrowser.open_new_tab(d+'.html')
btn = Button(window, text="INPUT FILE",font=('Times New Roman',10,'bold'),bg='orange',command=clicked).pack(side='bottom')
messagebox.showwarning('REMINDER', 'PLEASE ENTER .pdf FILE ONLY')
window.mainloop()
