from tkinter import *
from PIL import Image,ImageTk
import random






#global points_player1
#global points_player2

def check():
	if i>k:
		y=Tk()
		y.geometry("300x250")
		y.configure(background="white")
		l=Label(y,text="winner chicken dinner",font="Arial 6")
		l.pack(pady=80)
		y.mainloop()
	elif i==k:
		y1=Tk()
		y1.geometry("300x250")
		l1=Label(y1,text="draw match",font="Arial 6")
		y1.configure(background="white")
		l1.pack(pady=80)
		y1.mainloop()
	elif i<k:
		y2=Tk()
		y2.geometry("300x250")
		y2.configure(background="white")
		l2=Label(y2,text="losser",font="Arial 6")
		l2.pack(pady=80)
		y2.mainloop()
	else:
		pass
	#elif i==10 and k==10:
#		y3=Tk()
#		y3.geometry("100x150")
#		l3=Label(y,text="draw match",font="Arial 6")
#		l3.pack()
#		y3.mainloop()
#	else:
#		pass





i=0 
k=0



	
		
	



def um2():
	
	global k
	
	
	if buttons[0]["text"]=="#" and buttons[1]["text"]=="#" and buttons[2]["text"]=="#":
			k=k+10
			
			
			buttons[0].configure(background="green")
			buttons[1].configure(background="green")
			
			buttons[2].configure(background="green")
	
			
			
			
			
	elif buttons[3]["text"]=="#" and buttons[4]["text"]=="#" and buttons[5]["text"]=="#":
			k=k+10
			
			
			
			buttons[3].configure(background="green")
			
			buttons[4].configure(background="green")
			
			buttons[5].configure(background="green")
	
	elif buttons[6]["text"]=="#" and buttons[7]["text"]=="#" and buttons[8]["text"]=="#":
			k=k+10
			
				
					
				
			
			
			
			buttons[6].configure(background="green")
			
			buttons[7].configure(background="green")
			
			buttons[8].configure(background="green")
	elif buttons[0]["text"]=="#" and buttons[3]["text"]=="#" and buttons[6]["text"]=="#":
			k=k+10
			
			
			
			buttons[0].configure(background="green")
			
			buttons[3].configure(background="green")
			
			buttons[6].configure(background="green")
	elif buttons[1]["text"]=="#" and buttons[4]["text"]=="#" and buttons[7]["text"]=="#":
			k=k+10
			
			
			
			buttons[1].configure(background="green")
			
			buttons[4].configure(background="green")
			
			buttons[7].configure(background="green")
	elif buttons[2]["text"]=="#" and buttons[5]["text"]=="#" and buttons[8]["text"]=="#":
			k=k+10
			
			
			
			buttons[3].configure(background="green")
			
			buttons[5].configure(background="green")
			
			buttons[8].configure(background="green")
	
	
	elif buttons[0]["text"]=="#" and buttons[4]["text"]=="#" and buttons[8]["text"]=="#":
			k=k+10
			
			
			
			buttons[0].configure(background="red")
			
			buttons[4].configure(background="green")
			
			buttons[8].configure(background="green")
	
	elif buttons[2]["text"]=="#" and buttons[4]["text"]=="#" and buttons[6]["text"]=="#":
			k=k+10
			
			
			
			buttons[2].configure(background="green")
			
			buttons[4].configure(background="green")
			
			buttons[6].configure(background="green")


def um1():
	global i
	if buttons[0]["text"]=="0" and buttons[1]["text"]=="0" and buttons[2]["text"]=="0":
			i=i+10
			
			buttons[0].configure(background="red")
			buttons[1].configure(background="red")
			buttons[2].configure(background="red")
			
			
			
			
	elif buttons[3]["text"]=="0" and buttons[4]["text"]=="0" and buttons[5]["text"]=="0":
			i=i+10
			
			
			
			buttons[3].configure(background="red")
			
			buttons[4].configure(background="red")
			
			buttons[5].configure(background="red")
	
	elif buttons[6]["text"]=="0" and buttons[7]["text"]=="0" and buttons[8]["text"]=="0":
			i=i+10
			
			
			
			buttons[6].configure(background="red")
			
			buttons[7].configure(background="red")
			
			buttons[8].configure(background="red")
	elif buttons[0]["text"]=="0" and buttons[3]["text"]=="0" and buttons[6]["text"]=="0":
			i=i+10
			
			
			
			buttons[0].configure(background="red")
			
			buttons[3].configure(background="red")
			
			buttons[6].configure(background="red")
	elif buttons[1]["text"]=="0" and buttons[4]["text"]=="0" and buttons[7]["text"]=="0":
			i=i+10
			
			
			buttons[1].configure(background="red")
			
			buttons[4].configure(background="red")
			
			buttons[7].configure(background="red")
	elif buttons[2]["text"]=="0" and buttons[5]["text"]=="0" and buttons[8]["text"]=="0":
			
			
			
			buttons[3].configure(background="red")
			
			buttons[5].configure(background="red")
			
			buttons[8].configure(background="red")
	
	
	elif buttons[0]["text"]=="0" and buttons[4]["text"]=="0" and buttons[8]["text"]=="0":
			i=i+10
			
			
			
			buttons[0].configure(background="red")
			
			buttons[4].configure(background="red")
			
			buttons[8].configure(background="red")
	
	elif buttons[2]["text"]=="0" and buttons[4]["text"]=="0" and buttons[6]["text"]=="0":
			i=i+10
			
			
			
			buttons[2].configure(background="red")
			
			buttons[4].configure(background="red")
			
			buttons[6].configure(background="red")

			
			
			
	
	


	
	
	
#global points_player1
#global points_player2

	
global name1
global name2	

name1="human:"
name2="Bot:"
	
	
	



succes=0
def bot():
	sel=random.choice(buttons)
	
	if sel["text"]==" ":
		sel["text"]="#"
		global succes
		succes=succes+1
		um2()
	
		
	elif sel["text"]=="0":
		bot()
	else:
		bot()
	if succes==4:
		check()
	


su=0
def res(b):
	
	
	if buttons[b]["text"]==" ":
		buttons[b]["text"]="0"
		global su
		su=su+1
		
		
		um1()
		bot()
	if su==5:
		check()
		
		
		
		
		
		
		
		
			
			
			
		
		
			
		
	
		
		
		
		
	
	
		

#/////////game//////////	
def game():
	root=Tk()
	root.geometry("490x330")
	root.resizable(0,0)
	x=IntVar()
	y=IntVar()	

	f4=Frame(root,bg="pink")
	f4.pack(expand=True,fill="both",side=RIGHT)
	f1=Frame(root)
	f1.pack(expand=True,fill="both")
	f2=Frame(root)
	f2.pack(expand=True,fill="both")
	f3=Frame(root)
	f3.pack(expand=True,fill="both")
	result=Label(f4,text="score",bg="pink")
	result.place(x=10,y=10)
	
	l=Label(f4,text=name1,font="Arial 5",bg="pink")
	l.place(x=0,y=80)
	l1=Label(f4,text=name2,font="Arial 5",bg="pink")
	l1.place(x=0,y=110)
	


	box=Entry(f4,font="Arial 5",width=2)
	box.place(x=65,y=80)
	box1=Entry(f4,font="Arial 5",width=2,bg="green")
	box1.place(x=65,y=110)
	mn=0
	x.set(mn)
	box.configure(background="red")
	
	#box3=Entry(f4,font="Arial 5",width=2)
#	box3.place(x=0,y=170)
#	
#	
#	
#	
#	box4=Entry(f4,font="Arial 5",width=2)
#	box4.place(x=40,y=170)
#	
#	
#	box5=Entry(f4,font="Arial 5",width=2)
#	box5.place(x=0,y=200)
#	
#	
#	box6=Entry(f4,font="Arial 5",width=2)
#	box6.place(x=40,y=200)
#	list=[box3,box4,box5,box6]
#	
	
	#box1=Entry(f4,font="Arial 5",width=2,textvariable=y)
#	box1.place(x=65,y=110)
#	box1=Entry(f4,font="Arial 5",width=2,textvariable=y)
#	box1.place(x=65,y=110)
#	
	
	
	
	
	b1=Button(f1,text=" ",width=3,height=2,relief="sunken",command=lambda:res(0),borderwidth=5)
#	b1.configure(command=lambda:botfather(b2))
	b1.grid(row=0,column=0)
	
	b2=Button(f1,text=" ",width=3,height=2,borderwidth=5,relief="sunken",command=lambda:res(1))
	b2.grid(row=0,column=1)
	
	b3=Button(f1,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(2))
	b3.grid(row=0,column=2)
	
	b4=Button(f2,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(3))
	b4.grid(row=1,column=0)
	
	b5=Button(f2,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(4))
	b5.grid(row=1,column=1)
	
	b6=Button(f2,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(5))
	b6.grid(row=1,column=2)
	
	b7=Button(f3,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(6))
	b7.grid(row=2,column=0)
	
	b8=Button(f3,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(7))
	b8.grid(row=2,column=1)
	
	b9=Button(f3,text=" ",width=3,height=2,relief="sunken",borderwidth=5,command=lambda:res(8)
		)
	b9.grid(row=2,column=2)
	global buttons
	buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
#	bot(b1,b2,b3,b4,b5,b6,b7,b8,b9)	
	

		
	root.mainloop()
	

	
#main screen/////)))))/////////////////////
scr1=Tk()
scr1.geometry("600x600")
scr1.resizable(0,0)

scr1.title("tic tac game")
scr1.configure(background="pink")
img=Image.open("ma.jpg")
load=ImageTk.PhotoImage(img)
l2=Label(scr1,image=load)

l2.place(x=0,y=0)
t=Label(scr1,text="tic tac game",relief="sunken",bg="pink")
t.pack(pady=150)

t2=Label(scr1,text="Devloper-Madhav",font="Arial 6",bg="pink")
#t2.pack(side=TOP,anchor="n")
t2.place(x=205,y=200)

b1=Button(scr1,text="start game",command=game,bg="white",width=5,height=1)
b1.place(x=220,y=260)




scr1.mainloop()





