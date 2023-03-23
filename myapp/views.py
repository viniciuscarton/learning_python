from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os

def index(request):
    return render(request, 'index.html')

def basic_view(request):
    context = {'heading': 'basic'}
    return render(request, 'level.html', context)

def intermediate_view(request):
    context = {'heading': 'intermediate'}
    return render(request, 'level.html', context)

def advanced_view(request):
    context = {'heading': 'advanced'}
    return render(request, 'level.html', context)

def script_list(request):
    image_dict = {
      'bandnamegenerator': 'Generate a band name.',
      'blackjack': 'Blackjack!',
      'bmi': 'Calculate your BMI.',
      'caesarcypher': 'Encrypt and decrypt a message.',
      'calculator': 'Just a calculator.',
      'coffeemachine': 'A simple coffee machine system.',
      'daysinamonth': 'Find out how many days a month has (even in leap years).',
      'guessthenumber': 'Guess a random number.',
      'hangman': 'Hangman!',
      'higherorlower': 'Guess which personality has a higher number of followers.',
      'lifeleft': 'Calculate how much you have left.',
      'lovecalculator': 'Find out if you and are partner are a good match.',
      'oddoreven': 'Is it odd or even?',
      'paperrockscissors': 'Paper! Rock! Scissors!',
      'passwordgenerator': 'Generate a passaword.',
      'primenumberchecker': 'Is it a prime number?',
      'secretauction': 'Make a bid with your friends and it will tell you the winner!',
      'tipcalculator': 'Calculate your tip.',
      'treasureislandgame': 'Make your moves and find the treasure.'
    }
    context = {
        'image_dict': image_dict
    }
    return render(request, 'script_list.html', context)

script_dict = {
    'basic-utility': ['myapp/static/script/basic/utility/bandnamegenerator.py', 'myapp/static/script/basic/utility/bmi.py', 'myapp/static/script/basic/utility/calculator.py', 'myapp/static/script/basic/utility/daysinamonth.py', 'myapp/static/script/basic/utility/lifeleft.py', 'myapp/static/script/basic/utility/oddoreven.py', 'myapp/static/script/basic/utility/primenumberchecker.py', 'myapp/static/script/basic/utility/tipcalculator.py'],
    'intermediate-utility': ['myapp/static/script/intermediate/utility/caesarcypher.py', 'myapp/static/script/intermediate/utility/coffeemachine.py', 'myapp/static/script/intermediate/utility/guessthenumber.py', 'myapp/static/script/intermediate/utility/passwordgenerator.py'],
    'advanced-utility': [],
    'basic-fun': ['myapp/static/script/basic/fun/lovecalculator.py', 'myapp/static/script/basic/fun/treasureislandgame.py'],
    'intermediate-fun': ['myapp/static/script/intermediate/fun/blackjack.py', 'myapp/static/script/intermediate/fun/hangman.py', 'myapp/static/script/intermediate/fun/higherorlower.py', 'myapp/static/script/intermediate/fun/paperrockscissors.py', 'myapp/static/script/intermediate/fun/secretauction.py'],
    'advanced-fun': []
}

def file_view_fun(request, heading):
    script_entry = heading + '-fun'
    script_list = script_dict[f'{heading}-fun']
    descriptions = {
      'bandnamegenerator': 'Generate a band name.',
      'blackjack': 'Blackjack!',
      'bmi': 'Calculate your BMI.',
      'caesarcypher': 'Encrypt and decrypt a message.',
      'calculator': 'Just a calculator.',
      'coffeemachine': 'A simple coffee machine system.',
      'daysinamonth': 'Find out how many days a month has (even in leap years).',
      'guessthenumber': 'Guess a random number.',
      'hangman': 'Hangman!',
      'higherorlower': 'Guess which personality has a higher number of followers.',
      'lifeleft': 'Calculate how much time you have left.',
      'lovecalculator': 'Find out if you and your partner are a good match.',
      'oddoreven': 'Is it odd or even?',
      'paperrockscissors': 'Paper! Rock! Scissors!',
      'passwordgenerator': 'Generate a password.',
      'primenumberchecker': 'Is it a prime number?',
      'secretauction': 'Make a bid with your friends and it will tell you the winner!',
      'tipcalculator': 'Calculate your tip.',
      'treasureislandgame': 'Make your moves and find the treasure.'
    }
    context = {'heading': heading + '/fun','script_list': script_list, 'descriptions': descriptions}
    return render(request, 'file.html', context)

def file_view_utility(request, heading):
    script_entry = heading + '-utility'
    script_list = script_dict[f'{heading}-utility']
    descriptions = {
      'bandnamegenerator': 'Generate a band name.',
      'blackjack': 'Blackjack!',
      'bmi': 'Calculate your BMI.',
      'caesarcypher': 'Encrypt and decrypt a message.',
      'calculator': 'Just a calculator.',
      'coffeemachine': 'A simple coffee machine system.',
      'daysinamonth': 'Find out how many days a month has (even in leap years).',
      'guessthenumber': 'Guess a random number.',
      'hangman': 'Hangman!',
      'higherorlower': 'Guess which personality has a higher number of followers.',
      'lifeleft': 'Calculate how much time you have left.',
      'lovecalculator': 'Find out if you and your partner are a good match.',
      'oddoreven': 'Is it odd or even?',
      'paperrockscissors': 'Paper! Rock! Scissors!',
      'passwordgenerator': 'Generate a password.',
      'primenumberchecker': 'Is it a prime number?',
      'secretauction': 'Make a bid with your friends and it will tell you the winner!',
      'tipcalculator': 'Calculate your tip.',
      'treasureislandgame': 'Make your moves and find the treasure.'
    }
    context = {'heading': heading + '/utility','script_list': script_list, 'descriptions': descriptions}
    return render(request, 'file.html', context)

