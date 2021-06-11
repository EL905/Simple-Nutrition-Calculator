# Program to calculate total nutrition vlaue of your meal
# Select item from list and enter amount in grams, then add
# The program will add and display all nutritions
# Author: Damian Wlodarczyk
# Date: 20/09/2020

from tkinter import *

root = Tk()
root.title("Nutrition calculator")
root.geometry("400x500")

caloriesTotal = 0
fatTotal = 0
carbsTotal = 0
proteinTotal = 0

class Item:
    def __init__(self,name,calories,fat,carbs,protein): 
          self.name = name
          self.calories = calories
          self.fat = fat
          self.carbs = carbs
          self.protein = protein

def selected_item():
    global caloriesTotal
    global fatTotal
    global carbsTotal
    global proteinTotal

    for item in list.curselection():
        caloriesTotal   += (y[item].calories * (float(amountField.get()) / 100))
        fatTotal        += (y[item].fat * (float(amountField.get()) / 100))
        carbsTotal      += (y[item].carbs * (float(amountField.get()) / 100))
        proteinTotal    += (y[item].protein * (float(amountField.get()) / 100))
        
    label.config(text = "Total Calories: " + str("%.2f"%caloriesTotal) + "\n"
        + "Total Fat: " + str("%.2f"%fatTotal) + "\n"
        + "Total Carbs: " + str("%.2f"%carbsTotal) + "\n"
        + "Total Protein: " + str("%.2f"%proteinTotal))

    amountField.delete(0,"end")

def reset():
    global caloriesTotal
    global fatTotal
    global carbsTotal
    global proteinTotal

    caloriesTotal *= 0
    fatTotal *= 0
    carbsTotal *= 0
    proteinTotal *= 0

    label.config(text = "Total Calories: " + str(caloriesTotal) + "\n"
        + "Total Fat: " + str(fatTotal) + "\n"
        + "Total Carbs: " + str(carbsTotal) + "\n"
        + "Total Protein: " + str(proteinTotal))

# Choosing selectmode as multiple 
# for selecting multiple options
list = Listbox(root)
label = Label(root, text="")
amountField = Entry(root, )
addButton = Button(root, text="Add", command=selected_item)
resetButton = Button(root, text="Reset", command=reset)

# Widget expands horizontally and
# vertically by assigning both to 
# fill option
list.pack(expand = YES, fill = "both")
label.pack()
amountField.pack()
addButton.pack()
resetButton.pack()


rosół = Item("Rosół",36,1.2,3.53,2.52)
chocolate90percent = Item("Chocolate 90%",592,55,14,10)
chocolate85percent = Item("Chocolate 85%",564,41,33,11)
broccoli = Item("Broccoli",33,0.4,7,2.8)
scalions = Item("Scalions",32,0.2,7,1.8)
onion = Item("Onion",39,0.1,9,1.1)
egg = Item("Egg",155,11,1.1,13)
strawberry = Item("Strawberry",32,0.3,8,0.7)
blueberry = Item("Blueberry",57,0.3,14,0.7)
blackberry = Item("Blackberry",43,0.5,10,1.4)
mushroom = Item("Mushroom",22,0.3,3.3,3.1)
raspberry = Item("Raspberry",52,0.7,12,1.2)
chicken = Item("Chicken",239,14,0,27)
pork = Item("Pork",242,14,0,27)
beef = Item("Beef",250,15,0,26)
walnut = Item("Walnut",654,65,14,15)
sunflowerSeeds = Item("Sunflower seeds",584,51,20,21)
tomato = Item("Tomato",17,0.2,3.9,0.9)
cucumber = Item("Cucumber",15,0.1,3.6,0.7)
pickle = Item("Pickle",10,0.2,2.3,0.3)
mayonnaise = Item("Mayonnaise (ml)",681,74,3.7,0.8)
frankfurter = Item("Frankfurter",266,22,4.5,13)
pepperoniMild = Item("Pepperioni - Mild",498,47,2,17)
cheeseMaasdam = Item("Cheese - Maasdam",372,30,0.5,24)
rashersUnsmoked = Item("Rashers (unsmoked)",289,26,0.5,13)
porkSausageIrish = Item("Pork Sausage (Irish)",279,23,2.2,16)
cheeseCheddar = Item("Cheese - Cheddar",390,32,0.5,26)
spinach = Item("Spinach",17,0.5,0.5,2.2)
kabanos = Item("Kabanos",496,44,3,24)
frenchBrie = Item("French Brie",352,31,0.5,17)
mayonnaiseKielecki = Item("Mayonnaise Kielecki",631,68,2.3,1.9)
oliveOilExtraVirgin = Item("Olive Oil Extra Virgin(ml)",828,92,0.5,0.5)
watermelon = Item("Watermelon",30,0.2,8,0.6)
sourCream = Item("Sour Cream(ml)",264,26,4.7,2.9)
lard = Item("Lard",900,100,0,0)
porkMince = Item("Pork Mince",169,10,0.5,19)
garlic = Item("Garlic",90,0.6,16.3,7.9)
pepper = Item("Pepper",31,0.3,6,1)
pierogiGesina = Item("Pierogi z gęsiną",212,8.1,24,8.9)
irishHoneyHam = Item("Irish Honey Ham",127,2.4,1,24.9)
tomatoPassta = Item("Tomato Passta",31,0.1,4.8,1.7)
smokedPorkSausage = Item("Smoked Pork Sausage",487,35,0.9,29.5)
smokedMacrel = Item("Smoked Macrel",272,21,0,21)


x = [rosół.name, chocolate90percent.name, chocolate85percent.name, broccoli.name, scalions.name, onion.name,
     egg.name, strawberry.name, blueberry.name, blackberry.name, mushroom.name, raspberry.name, 
     chicken.name, pork.name, beef.name, walnut.name, sunflowerSeeds.name, tomato.name, cucumber.name,
     pickle.name, mayonnaise.name, frankfurter.name, pepperoniMild.name, cheeseMaasdam.name,
     rashersUnsmoked.name, porkSausageIrish.name, cheeseCheddar.name, spinach.name, kabanos.name, frenchBrie.name,
     mayonnaiseKielecki.name, oliveOilExtraVirgin.name, watermelon.name, sourCream.name, lard.name,
     porkMince.name, garlic.name, pepper.name, pierogiGesina.name, irishHoneyHam.name, tomatoPassta.name,
     smokedPorkSausage.name, smokedMacrel.name]

y = [rosół, chocolate90percent, chocolate85percent, broccoli, scalions, onion,
     egg, strawberry, blueberry, blackberry, mushroom, raspberry, 
     chicken, pork, beef, walnut, sunflowerSeeds, tomato, cucumber,
     pickle, mayonnaise, frankfurter, pepperoniMild, cheeseMaasdam,
     rashersUnsmoked, porkSausageIrish, cheeseCheddar, spinach, kabanos, frenchBrie,
     mayonnaiseKielecki, oliveOilExtraVirgin, watermelon, sourCream, lard,
     porkMince, garlic, pepper, pierogiGesina, irishHoneyHam, tomatoPassta,
     smokedPorkSausage, smokedMacrel]
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])

root.mainloop()