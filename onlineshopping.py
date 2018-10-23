from easygui import *
import sys
while 1:
   msgbox("welcome to online shopping!")

   msg = "Which site would you prefer?"
   title = "online diwali shopping"
   choics = ["amazon","myntra","snapdeal","flipkart"]
   choice = choicebox(msg,title,choices)
   if choices=="amazon":
      msg1="what do you want on this diwali"
      title1="online diwali shopping"
      choices1=["electronics","fashion","sports","toys","clothes"]
      choice1=choicebox(msg1,title1,choices1)
   if choices1=="electronics":
      msg2="what do you want on this diwali"
      title2="online diwali shopping"
      choices2==["electronics","fashion","sports","toys","clothes"]

   msgbox("you chose: " + str(choice),"Survey Result")
   msg ="Do you want to continue?"
   title = "Please Confirm"
   if ccbox(msg, title):
      pass
   else:
      sys.exit(0)
