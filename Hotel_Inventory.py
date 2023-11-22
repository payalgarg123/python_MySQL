from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import ttk
import datetime
import mysql.connector

#mysql connector code
conn= mysql.connector.connect(host='localhost',
                        database='restaurant',
                        user='root',
                        password='7877766268')

cur=conn.cursor(buffered=True)


try:  
    dbs = cur.execute("create table menu( Name varchar(20) not null,address varchar(20) not null,phone_number int(20) not null ,no_of_days int(10) not null,total_amount int(20) not null)")  
    # dbs = cur.execute("show databases")  
except:  
    conn.rollback()

# design 
root = Tk()
root.geometry("1350x700")
root.title("Restaurant management system")
root.config(bg = "blue")

# #image for cart
menu_img = Image.open("C:/Users/panka/OneDrive/Desktop/hotel_management/purepng.com-shopping-cartshoppingcarttrolleycarriagebuggysupermarkets-14215265325036jrux.png")
resized = menu_img.resize((100, 100))
menu_img = ImageTk.PhotoImage(resized)



image = PhotoImage(file="C:/Users/panka/OneDrive/Desktop/hotel_management/purepng.com-shopping-cartshoppingcarttrolleycarriagebuggysupermarkets-14215265325036jrux.png")


custom_font = font.Font(family="Helvetica", size=30, weight="bold")

head_label = Label(root, text="Restaurant management system", image=image, compound="left",width=1500,bg = "blue",anchor="center",font=custom_font,fg ="white")
# head_label = Label(root,text="Inventory management system",bg="blue",fg="white",width=200,font=custom_font,anchor="w")
head_label.place(x = 0,y = 0)



def update_time():
    current_time=datetime.datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    head_label1.config(text="\tWelcome to Inventory management system\t\tDate: {} \t\ttime: {}".format((datetime.datetime.now()).strftime("%d/%m/%y"),current_time))
    root.after(1000, update_time)
head_label1 = Label(root,text="",width=200,bg = "grey",fg ="white",font=("arial",14,"bold"),anchor="w")
head_label1.place(x = 0,y = 100)
update_time()

left_menu = Frame(root,bd = 2,relief=RIDGE,width=159,height=555,bg="orange")
left_menu.place(x = 0,y=128)

menu_logo_label = Label(left_menu,image =menu_img,bg="orange",anchor="center",width=159,height=120)
menu_logo_label.place(x = 0,y=0)

menu_label = Label(left_menu,text="Menu",width = 10,bg="blue",font=("arial",20,"bold"),fg="white",anchor="center")
menu_label.place(x = 0,y=120)



next_image = Image.open("C:/Users/panka/OneDrive/Desktop/hotel_management/Restaurant-Logo-PNG-Download-Image.png")
resized = next_image.resize((28, 28))
next_image = ImageTk.PhotoImage(resized)





#code for design table no.
a=200
for i in range(1,6):
    label="tot_label"+str(i)
    label= Label(root,text="Table {}/n[0]".format(i),bg = "light blue",relief=RIDGE,bd = 5,font=("Arial",15,"bold"))
    label.place(x =a,y=200,width=200,height=100)
    a=a+200


prices = []
records = []
def pop_up(y):
    popup = Toplevel(root,width=400,height=400)  # Create a new popup window
    popup.title("Popup Window")
    popup_frame = Frame(popup, width=400, height=400,bg="light blue")
    popup_frame.place(x=200, y=200, anchor=CENTER)

    # Add widgets to the frame using place

    query = "SELECT name FROM "+y
    cur.execute(query)
    # records = cur.fetchall()

    for row in cur.fetchall():
        print(row[0])
        records.append(row[0])
    
    query = "SELECT price FROM "+y
    cur.execute(query)
    # records = cur.fetchall()

    for row in cur.fetchall():
        print(row[0])
        prices.append(row[0])
    
    print(prices)

    global breads_combo
    breads_combo = ttk.Combobox(popup_frame,values=records,font=("Arial",13,"bold"))
    breads_combo.place(x = 10,y = 120)
    breads_combo.set("select food item")


    label = Label(popup_frame, text="Select your "+y,font=("Arial",20,"bold"))
    label.place(x=80, y=50)

    Btn_sub = Button(popup_frame,text="-",command = sub_quant_bread,font=("Arial",11,"bold"))
    Btn_sub.place(x = 230,y = 113)

    global label_quant_bread
    label_quant_bread = Label(popup_frame,text=0,bg="white",width=5,font=("Arial",14,"bold"))
    label_quant_bread.place(x = 251,y = 113)

    Btn_sub = Button(popup_frame,text="+",command = add_quant_bread,font=("Arial",11,"bold"))
    Btn_sub.place(x = 320,y = 113)



    
    global table_combo
    tables = ["1","2","3","4"]
    table_combo = ttk.Combobox(popup_frame,values = tables,font=("Arial",13,"bold"))
    table_combo.place(x = 100,y = 163)
    table_combo.set("select table number")
    # btn_submit = Button(popup_frame,text = "SUBMIT",command=lambda: submit(table_combo.get()),font=("Arial",13,"bold"))
    # btn_submit.place(x = 170,y = 213)

    records.clear()    

def add_quant_bread():
    x = label_quant_bread['text']
    x+=1
    label_quant_bread['text'] = x
def sub_quant_bread():
    x = label_quant_bread['text']
    x-=1
    label_quant_bread['text'] = x

btn_breads = Button(left_menu,text="Breads",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("breads"))
btn_breads.place(x = 0,y=160)
btn_curries = Button(left_menu,text="Curries",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("curries"))
btn_curries.place(x = 0,y=200)
btn_sweetdish = Button(left_menu,text="Sweet dishes",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("Sweet dishes"))
btn_sweetdish.place(x = 0,y=240)
btn_beverage = Button(left_menu,text="Beverages",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("Beverages"))
btn_beverage.place(x = 0,y=280)
btn_starters = Button(left_menu,text="Starters",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("Starters"))
btn_starters.place(x = 0,y=320)
btn_soup = Button(left_menu,text="Soups",image = next_image,compound=LEFT,width = 145,font=("arial",14,"bold"),fg="black",anchor="w",bd=3,bg="yellow",command=lambda:pop_up("Soups"))
btn_soup.place(x = 0,y=360)


root.mainloop()