from tkinter import *
from tkinter import ttk #สไตล์กล่อง
from tkinter import messagebox
GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าโปรแกรมกว้าง x ยาว

L1 = Label(GUI , text = 'โปรแกรมบันทึกความรู้' , font = ('Angsana New',30),fg='green')
L1.place(x=30,y=20)
#B1 = ttk.Button (GUI,text = 'ยอดเงินที่มีอยู่')
#แสดง Block อยู่กลางหน้าจอ
#B1.pack(ipadx=20,ipady=20) # ขนาดปุ่ม

##โปรแกรม Command ใส่ใน Box
def Button2() : #ฟังก์ชั่น 
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo ('เงินในบัญชี' , text ) #ฟังก์ชั่น popup มี 3 แบบ
#showwarring #showinfo #showerror

#FB1 = Frame (GUI) #คล้ายกระดาน
FB1 = LabelFrame (GUI,text='Money')
FB1.place(x=80,y=80)
B2 = ttk.Button (FB1,text = 'ยอดเงินที่มีอยู่' , command = Button2)
#แสดงกำหนด Location กล่องปุ่ม
B2.pack(ipadx=20 , ipady=20 ,padx=30 , pady=30) #พิกัด 0,0 อยู่มุมซ้ายโปรแกรม
#ipad ขนาดกล่อง button , pad ขนาด Frame คุมหัวข้อ



GUI.mainloop()
