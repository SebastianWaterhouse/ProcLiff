import webbrowser, sys

class stuff(Object):
  name = "null"
  def poke_return():
    pass
  def watch_return():
    pass
  def microscope_return():
    pass
  def inspect_return():
    pass
  def timelapse_return():
    pass
  def checkwaste_return():
    pass
  def dnamap_return():
    pass
  

class tree(stuff):
  name = "tree"
  def poke_return():
    print("It's a tree. Nothing happens.")
  def watch_return():
    webbrowser.open("https://www.youtube.com/watch?v=C1_uez5WX1o")
  def microscope_return():
    print("Yep. The tree has cells all right.")
  def inspect_return():
    print("By using pollen, trees reproduce sexually. They can also reproduce asexually through human intervention.")
  def timelapse_return():
    print("Over many years, this tree grew from a random seed stuck in the ground to a great, majestic, 30-foot tall behemoth of the natural world.")
  def checkwaste_return():
    print("When too much of it is built up, trees release excess oxygen.")
  def dnamap_return():
    print("That's definitely dna.")

class porcup(stuff):
  name = "porcupine"
  def poke_return():
    print("It looks disgruntled, gets up, and sits down.")
  def watch_return():
    print("As you watch, the porcupine eats an apple.")
  def microscope_return():
    print("Just as you suspected, the porcupine has cells. Simply amazing.")
  def inspect_return():
    print("Looks like it reproduces sexually. It dawns on you that you really didn't need to do that.")
  def timelapse_return():
    print("Daw! It was so cute as a baby! Now it kind of scares you.")
  def checkwaste_return():
    print("Poor little guy is shivering.")
  def dnamap_return():
    print("That's definitely dna.")

class myster(stuff):
  name = "thing"
  def poke_return():
    print("It eats your finger. You die.")
    sys.exit()
  def watch_return():
    print("As you watch, the weird thing eats an entire bear.")
  def microscope_return():
    print("You think those are cells, but it's a good question.")
  def inspect_return():
    print("This appears to split apart to reproduce.")
  def timelapse_return():
    print("You don't need to run a timelapse. It grows before your eyes.")
  def checkwaste_return():
    print("It excretes a strange green liquid. Best not touch it.")
  def dnamap_return():
    print("These dna strands, they're constantly changing.")

class rock(stuff):
  name = "rock"
  def poke_return():
    print("It's a rock. It doesn't do anything.")
  def watch_return():
    print("It's a rock. It doesn't do anything.")
  def microscope_return():
    print("Looks really bumpy.")
  def timelapse_return():
    print("It's a rock. It doesn't do anything.")
  def checkwaste_return():
    print("It's a rock. It doesn't do anything.")
  def dnamap_return():
    print("It's a rock. It doesn't have dna.")

nouns = {"porcupine":porcup, "tree":tree, "thing":myster, "rock":rock]

class commands(Object):
  name = "null"
  point = "null"
  allows_articles = 0
  def MainFunc(inputs):
    pass

class poke(commands):
  name = "poke"
  point = "Movement"
  def MainFunc(target):
    a = getattr(nouns[target], "poke_return")
    a()
class watch(commands):
  name = "watch"
  point = "Intake"
  def MainFunc(target):
    a = getattr(nouns[target], "watch_return")
    a()
class microscope(commands):
  name = "microscope"
  point = "Cells"
  def MainFunc(target):
    a = getattr(nouns[target], "microscope_return")
    a()
class timelapse(commands):
  name = "timelapse"
  point = "Growth"
  def MainFunc(target):
    a = getattr(nouns[target], "timelapse_return")
    a()
class checkwaste(commands):
  name = "check"
  point = "Homeostasis"
  def MainFunc(target):
    a = getattr(nouns[target], "checkwaste_return")
    a()
class dnamap(commands):
  name = "map"
  point = "DNA"
  def MainFunc(target):
    a = getattr(nouns[target], "dnamap_return"_
    a()
class exit(commands):
  name = "exit"
  point = "exit"
  def MainFunc(target):
    sys.exit()

commands = {"poke":poke, "watch":watch, "microscope":microscope, "timelapse":timelapse, "check":checkwaste, "map":dnamap, "exit":exit

print ("There is a porcupine, a tree, a rock, and some weird thing.")
print(" ")
print("You can do these commands: ")
print ("Poke:Movement")
print("Watch:Intake")
print("Microscope:Cells")
print("Timelapse:Growth")
print("Check:Homeostasis")
print("Map:DNA")
print("Exit:Exit")
print(" ")
print("Use these commands by typing '[command] [target]'"
print(" ")

while 1:
  command = input("Type a command: ")
  command = command.split()
  try:
    commands[command[0]].MainFunc(command[1])
  except:
    print("Invalid command/target. Please try again.")
  
  
