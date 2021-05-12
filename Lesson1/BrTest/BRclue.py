import termcolor

from BRLogic import *

mustard = Symbol('ColMustard')
plum = Symbol('ProPlum')
scarlet = Symbol('MsScarlet')
characters = [mustard, plum, scarlet]

ballroom = Symbol('ballroom')
kitchen = Symbol('kitchen')
library = Symbol('library')
rooms = [ballroom, kitchen, library]

knife = Symbol('knife')
revolver = Symbol('revolver')
wrench = Symbol('wrench')
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: Yes", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))



check_knowledge(knowledge)