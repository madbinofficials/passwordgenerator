#password gamertaor and creator.


import random

data="abcdefghujklmnoqrstuvwxyzABCDEFGHUJKLMNIOQRSTUVWVXYZ1234567890"
def gen():
	
	print("how many digit of password you want🔐\n")
	k=int(input())
	password=''.join(random.					sample(data,k))
	print(password)
	response=input("Do you want set this as your password📑\n")
	if response=="yes":
		print("which account you want for it🔁\n")

		id=input()
		print("\t\n\n\n\n\n\n😇😇thank you for using our apps\n developer madhav bag🙏🙏")
		userdata=id+"👉"+password+"\n"
		with open('password.txt','a') as user:
			user.write(str(userdata))
		
			 
			 	 
			 	 	 
			 	 	 	 
def output():
	with open('password.txt','r') as user:
		
	    real_text=user.read()
	rm_text="{}''"
	outtext="".join(i for i in real_text if not i in rm_text)
	
	print(outtext)		 
		


print("\t🖥password generrator🖥")
print("\t🛠-------------------🛠")
print("")
print("\t🇮🇳DEVELOPER:-Madhav Bag✅\n")
choice=int(input("\twhat do you want to do:-\n\t  1:👉new password \n\t  2:👉see passwords\n"))


#try:
if choice==1:
	gen()
else:
	print("enter the master key ro view it 🧐\n")
	key=input()
	if key=="madhav":
		output()
	else:
		print("Go Back To Home😡😡")

		
   	
		
	

#except:
#	print("plz input right options")
	
