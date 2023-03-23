import os
from django import template
register = template.Library()

@register.filter
def basename(value):
    return os.path.basename(value)

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]

@register.filter(name='script_title')
def format_script_basename(script_basename):
    formats = {
      'bandnamegenerator': 'Band name generator',
      'blackjack': 'Blackjack',
      'bmi': 'BMI',
      'caesarcypher': 'Caesar Cypher',
      'calculator': 'Calculator',
      'coffeemachine': 'Coffee Machine',
      'daysinamonth': 'Days in a Month',
      'guessthenumber': 'Guess the Number',
      'hangman': 'Hangman',
      'higherorlower': 'Higher or Lower',
      'lifeleft': 'Life Left',
      'lovecalculator': 'Love Calculator',
      'oddoreven': 'Odd or Even',
      'paperrockscissors': 'Paper, Rock, Scissors',
      'passwordgenerator': 'Generate a Passaword',
      'primenumberchecker': 'Prime Number Checker',
      'secretauction': 'Secret Auction',
      'tipcalculator': 'Tip Calculator',
      'treasureislandgame': 'Treasure Island Game'
    }
    if script_basename in formats:
        return formats[script_basename]
    else:
        return ' '.join([word.capitalize() for word in script_basename.split('_')])



