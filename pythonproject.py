#rashmi landge,33
#sneha kapure,26
#karnal raut,27
#mahesh nawale,43
#atharva nagarkar,42
#manas limkar,35

print("welcome to VIT BANK ATM")
restart="Y"
chances=3
balance=15000
while chances>=0:
 pin=int(input("please enter your 4 digit pin-"))
 if pin==(1234):
   print("/n you have entered the correct pin")
while(restart not in('n','No','no,N')):
print("/n please press 1 for your bank balance/n")
print("please press 2 to make a withdrawal/n")
print("please press 3 to deposited/n")
print("please press 4 to exit/n")
option=int(input("enter your option:"))
if option==1:
 print("your balance is",balance)
 restart=input("/n would you like to go back to the menu ?")
if restart in('n','No','no,N'):
 print("thank you")
 chances=-1
 break
elif option==2:
option2=('y')
withdrawal=float(input("how much would you like to withdrawal?/n available notes-100 200 500 2000/n"))
if(withdrawal%2000==0 or withdrawal%500==0 or withdrawal%200==0 or withdrawal%100==0):
 balance=balance-withdrawal
 print("your balance in account is",balance)
 restart=input("/n would you like to go back to the menu?")
 if restart in('n',NO',no,N'):
  print("thank you")
  chances=-1
  break
else:
 print("invalid amount!4,please retry")
 restart='Y'
elif option==3:
 deposite=float(input("how much would you like to deposite?"))
 balance=balance+deposite
 print("your balance is now",balance)
 restart=input(/n would you like to go back to the menu?")
 if restart in('n','No','no,N'):
  print("thank you")
  chances=-1
  break
elif option==4:
 print("thank you for using our ATM/n")
 chances=-1
 break
else:
 print("please enter a correct no./n")
elif pin!=(1234):
 print("incorrect password")
if chances==2:
 print("last try")
chances=chances-1
if chances==0:
 print("NO more tries!")
break