import time 

antwoord_A = ["A", "a"]
antwoord_B = ["B", "b"]
antwoord_C = ["C", "c"]
antwoord_d = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

speedboat = 0
grenade = 0

required = ("\nAlleen A, B, of C gebruiken\n") 

def intro():
  print ("Bruddas… my name is Osas… Let me tell you about back home.. When I was young.. at the age of 4 years old... I had just finished.. my ak-47 preliminary target practice.. I had just come out the shower.. I was a happy boy! Full of potential! Until…… the Wataumbu clan attacked. I witnessed the CEO of Wataumbu.. take my parents.. my BRUDDAS. Into the dark… and I never saw them again… after that day. I have dedicated myself. I will build infrastructure. In the Netherlands. To find my family. And bring justice to Wataumbu.:")
  time.sleep(1)
  print ("The first step is to escape africa.. I am located in Wakanda. How do i escape this land?:")
  time.sleep(1)
  print ("""  A. Grab the boat, and sail away.
  B. run through the guards.
  C. dig a hole.
  D. try to sneak out""")
  choice = input(">>> ") 
  if choice in antwoord_A:
    option_boat()
  elif choice in antwoord_B:
    print ("\nThat was a STUPID idea... "
    "\n\nyou have been killed.")
  elif choice in antwoord_C:
    print ("\nThat was a STUPID idea... "
    "\n\nyou have been killed.")
  elif choice in antwoord_d:
    option_sneak()
  else:
    print (required)
    intro()

def option_boat(): 
  print ("\nYou have grabbed the boat and sailed away as fast as you can.. however.. the Wataumbu clan has spotted you. They are trying to destroy your boat with canonballs... What do we do?:")
  time.sleep(1)
  print ("""  A. jump out the boat and swim
  B. sail harder
  C. look around for assistance.""")
  choice = input(">>> ")
  if choice in antwoord_A:
    option_hole()
  elif choice in antwoord_B:
    print ("\nyou tried to sail harder.. but you weren't fast enough to escape Wataumbu. \n\nyou have been killed by the canon ball.")
  elif choice in antwoord_C:
    option_assistance()
  else:
    print (required)
    option_boat()

def option_assistance():
  print ("\nyou look around for assistance.. you spot a speedboat! do you board it? Y/N")
  choice = input(">>> ")
  if choice in yes:
    speedboat = 1 
  else:
    speedboat = 0
  print ("\nwhat do you do now?")
  time.sleep(1)
  print ("""  A. nothing
  B. throw the sailor off
  C. swim away """)
  choice = input(">>> ")
  if choice in antwoord_A:
    print ("\nyou do... nothing..? That's kinda dumb lol \n\nYou have died so hard cuz Wataumbu")
  elif choice in antwoord_B:
   if speedboat > 0:
    print ("\nyou threw the sailor off and you are now captain of the boat.\n\nYou survive as you sail to freedom")
   else: 
     print ("\nyou did not get on the speedboat so you could not throw him off! \n\nWataumbu has ended you.")
  elif choice in antwoord_C:
    print ("swimming away was not an option.")
  else:
    print (required)
    option_assistance()

def option_hole():
  print ("\nyou remember you have special wakandan powers and can breathe under water! What are you goin got do?:")
  time.sleep(1)
  print ("""  A. nothing
  B. try to fight against Wataumbu's special forces
  C. dive underwater""")
  choice = input(">>> ")
  if choice in antwoord_A:
    print ("that was dumb lol. "
    "\n\nWataumbu has killed you really hard")
  elif choice in antwoord_B:
    print ("\nYou were no match for Wataumbu as you have no weapons or even a flat surface to stand on. "
    "\n\nYou have been killed by Wataumbu")
  elif choice in antwoord_C:
    option_dive()
  else:
    print (required)
    option_hole()
    
def option_dive():
  print ("\nyou dive very deep under water and encounter a shipwreck full of treasure! One of the treasures just so happens to be a grenade launcher. Do you take it? Y/N")
  choice = input(">>> ")
  if choice in yes:
    grenade = 1 
  else:
    grenade = 0
  print ("Wataumbu is getting closer.")
  time.sleep(1)
  if grenade > 0:
    print ("\nYou shoot the grenade launcher right in Wataumbu's faces. Luckily their ships survived the several explosions."
    "\n\nYou take their fully enhanced ship and sail to freedom!")
  else: 
     print ("\nMaybe you should've taken the grenade launcher my brudda "
     "\n\nWataumbu has obliterated you.")

def option_sneak():
  print ("You see the guards guarding the entrance to Wakanda. You try to sneak past them, but they spot you! what do you do?:")
  time.sleep(1)
  print ("""  A. Grab the nearest rock and throw it.
  B. run away.
  C. act like you belong.""")
  choice = input(">>> ") 
  if choice in antwoord_A:
    option_rock()
  elif choice in antwoord_B:
    option_run()
  elif choice in antwoord_C:
    option_act()
  else:
    print (required)
    option_sneak()

def option_rock():
  print ("You throw an epic rock.. but it had no effect... what now? :")
  time.sleep(1)
  print ("""  A. run away.
  B. throw another rock
  C. act like you belong.""")
  choice = input(">>> ") 
  if choice in antwoord_A:
    option_run()
  elif choice in antwoord_B:
    print ("\nwhy would you do that... you knew the first rock already had no effect... "
    "\n\nyou have been killed.")
  elif choice in antwoord_C:
    option_act()
  else:
    print (required)
    option_rock()

def option_run():
  print ("You run away so hard and notice someone left their truck open with key already in the ignition. What do you do? :")
  time.sleep(1)
  print ("""  A. steal the car.
  B. ignore the car and run other way """)
  choice = input(">>> ") 
  if choice in antwoord_A:
    option_runn()
  elif choice in antwoord_B:
    print ("\nyou tried running away.. however........ the guards were faster than you and caught you "
    "\n\nthey later killed you.")
  else:
    print (required)
    option_run()

def option_act():
  print ("You act and say you belong here. They asked why. What do you say? :")
  time.sleep(1)
  print ("""  A. \"i was startled\"
  B. \"i belong here because...\"
  C. \"i'm a guest\"""")
  choice = input(">>> ") 
  if choice in antwoord_A:
    option_startled()
  elif choice in antwoord_B:
    print ("\nyou say you belong here because... you couldnt think of anything so they shot you because they knew you were lying"
    "\n\nyou have been killed.")
  elif choice in antwoord_C:
    print ("\nthey shot you because they know they cant bring guests lol"
    "\n\nyou have been killed.")
  else:
    print (required)
    option_act()

def option_runn():
  print ("As you run you see an unlocked truck in the distance. You get in and drive off. But where to? :")
  time.sleep(1)
  print ("""  A. cameroon
  B. Benin
  C. Chad""")
  choice = input(">>> ") 
  if choice in antwoord_A:
    print ("\nYou arrive in the country Cameroon. However.. you did not know Cameroon is Wataumbu's homeland."
    "\n\nthey spot you and kill you on the spot")
  elif choice in antwoord_B:
    print ("\nyou arrive in the country Benin. however.... it was the wrong way. And it is too risky to go back. Now you are stranded."
    "\n\nyou die of starvation")
  elif choice in antwoord_C:
    print ("\nYou drive through the country known as Chad. This was a good choice. As it is closest to the Netherlands"
    "\n\nsurprisingly no accidents happen on your way to the Netherlands and you arrive safely. Time to build infrastructure!")
  else:
    print (required)
    option_runn()

def option_startled():
  print ("You say you were startled and that is why you threw the rock. They are still suspicious of you and decide to ask you a question only the guards would know. The question is: What is 9 + 10? :")
  time.sleep(1)
  print ("""  A. 19
  B. 21
  C. you tell them it is a trick question""")
  choice = input(">>> ") 
  if choice in antwoord_A:
     print ("\nyou got the question wrong"
    "\n\nand have been killed...")
  elif choice in antwoord_B:
    print ("\nno way you got the question right! They now think you are one of them and give you access to everything there"
    "\n\nyou take their truck and drive off safely.. to freedom...")
  elif choice in antwoord_C:
    print ("\nthey shoot you because it is not a trick question."
    "\n\nyou have been killed.")
  else:
    print (required)
    option_startled()

intro()

        