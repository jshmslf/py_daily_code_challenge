from pyfiglet import Figlet
from clint.textui import colored
result = Figlet(font='slant')
print(colored.blue(result.renderText('THE NEWS!')))
print('Hallo Shamim Welcome to the News Site')
sources = ["Al-jazeera-english", "Cnn", "Football-italia", "BBc-news"]
items=1
for source in sources:
    print(str(items)+":" + source)
    items+=1