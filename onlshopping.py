from easygui import *
import sys
sum=0
list=[]
while 1:
     msgbox("welcome")
     msg="which site do you prefer?"
     title = "onlshopping"
     choices = ["amazon","snapdeal","myntra","flipkart"]
     choice = choicebox(msg, title, choices)

  #  note that we convert choice to string,in case
  #  the usr cancelled the choice, and we got none.
     if choice=="amazon":
        msg="what do you want to buy?"
        title="shop items"
        choices=["electronics","clothing"]
        choice = choicebox(msg, title, choices)
        if choice=="electronics":
              msg="what do you want to buy?"
              title="shop electronnics"
              choices=["dell","lenovo","apple"]
              choice=choicebox(msg, title, choices)
        elif choice=="clothing":
              msg="what do you want to buy?"
              title="shop clothing"
              choices=["forver 21","zara","UCB"]
              choice = choicebox(msg, title, choices)
        elif choice=="flipkart":
             msg="what do you want to buy?" 
             title="shop items" 
             choices=["electronics","clothing"]
             choice = choicebox(msg, title, choices)
        if choice=="electronics":
              msg="what do you want to buy?"
              title="shop electronnics"
              choices=["dell","lenovo","apple"]
              choice=choicebox(msg, title, choices)
        elif choice=="clothing":       
              msg="what do you want to buy?"
              title="shop clothing"
              choices=["forver 21","zara","UCB"]
              choice = choicebox(msg, title, choices)
        elif choice=="snapdeal":
         msg="what do you want to buy?"
        title="shop items"
        choices=["electronics","clothing"]
        choice = choicebox(msg, title, choices)
        if choice=="electronics":
              msg="what do you want to buy?"
              title="shop electronnics"
              choices=["dell","lenovo","apple"]
              choice=choicebox(msg, title, choices)
        elif choice=="clothing":
              msg="what do you want to buy?"
              title="shop clothing"
              choices=["forver 21","zara","UCB"]
              choice = choicebox(msg, title, choices)
        elif choice=="myntra":
         msg="what do you want to buy?"
        title="shop items"
        choices=["electronics","clothing"]
        choice = choicebox(msg, title, choices)
        if choice=="electronics":
              msg="what do you want to buy?"
              title="shop electronnics"
              choices=["dell","lenovo","apple"]
              choice=choicebox(msg, title, choices)
        elif choice=="clothing":
              msg="what do you want to buy?"
              title="shop clothing"
              choices=["forver 21","zara","UCB"]
              choice = choicebox(msg, title, choices)
        msg ="do you want to continue?"
        title = "please confirm"
        if ccbox(msg,title):
              pass
        else:
              sys.exit(0)
