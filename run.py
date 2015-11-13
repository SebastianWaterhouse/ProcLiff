import webbrowser, sys

class stuff(Object):
  name = "null"
  def poke_return():
    "pass
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
    print("By using pollen, trees reproduce sexually. They can also reproduce asexually through human intervention."
  def timelapse_return():
    print("Over many years, this tree grew from a random seed stuck in the ground to a great, majestic, 30-foot tall behemoth of the natural world.
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

class rock(stuff):
  name = "rock"

nouns = {"porcupine":porcup, "tree":tree, "thing":myster, "rock":rock]
articles = ["the"]

class commands(Object):
  name = "null"
  acceptable_nouns = ["null"]
  allows_articles = 0
  def MainFunc(inputs):
    pass

class poke(commands):
  name = "poke"
  acceptable_nouns = ["porcupine", "tree", "thing"]
  allows_articles = 1
  def MainFunc(target):
    a = getattr(nouns[target], "poke_return")
    a()
