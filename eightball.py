from random import choice
import cmd
from json5 import load, dump


class Console(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.positive_answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definately',
                                 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes',
                                 'Signs point to yes', 'Wtf, why not', 'Something like that, yeah', 'More or less',
                                 'Fuck yeaaah!', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ']
        self.medium_answers = ['Reply hazy, try again', 'Ask again later', 'Better not tell you now',
                               'Cannot predict now', 'Concentrate and ask again', '¯\_(°°)_/¯',
                               'How the fuck should I know']
        self.negative_answers = ['Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful',
                                 'oop', 'Fuck no', 'Hell naw',
                                 '''....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...''']

        self.all_answers = [self.positive_answers, self.medium_answers, self.negative_answers]

        self.chaos_answers = ['How the fuck should I know', 'No, and fuck you for asking', '...Are you on drugs?',
                              '._. Really? No.', 'LMAO, dumbass.', 'Please, just shut the fuck up and leave',
                              'I swear, one more question like that and-', 'Your question takes dumbfuck to a new level.',
                              '*yawn* Wait, are you still talking?']

        self.thoughts = ['Hmm...', 'Let me think about it...', 'How should I put it...']

        self.qrefalias = {'exit': 'quit', 'close': 'quit'}

        try:
            with open('resources/settings.json', 'r') as file:
                self.settings = load(file)

        except Exception as e:
            print(e)
            self.settings = {'ChaosMode': False}

    intro = '''
 /$$      /$$                     /$$          
| $$$    /$$$                    |__/          
| $$$$  /$$$$  /$$$$$$   /$$$$$$  /$$  /$$$$$$$
| $$ $$/$$ $$ |____  $$ /$$__  $$| $$ /$$_____/
| $$  $$$| $$  /$$$$$$$| $$  \ $$| $$| $$      
| $$\  $ | $$ /$$__  $$| $$  | $$| $$| $$      
| $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$
|__/     |__/ \_______/ \____  $$|__/ \_______/
                        /$$  \ $$              
                       |  $$$$$$/              
                        \______/               
  /$$$$$$          /$$$$$$$            /$$ /$$ 
 /$$__  $$        | $$__  $$          | $$| $$ 
| $$  \ $$        | $$  \ $$  /$$$$$$ | $$| $$ 
|  $$$$$$/ /$$$$$$| $$$$$$$  |____  $$| $$| $$ 
 >$$__  $$|______/| $$__  $$  /$$$$$$$| $$| $$ 
| $$  \ $$        | $$  \ $$ /$$__  $$| $$| $$ 
|  $$$$$$/        | $$$$$$$/|  $$$$$$$| $$| $$ 
 \______/         |_______/  \_______/|__/|__/ 
 
 Use "/" before a word to turn it into a command
 ex: "/help"
 '''

    prompt = '\n°~~~~~~~~~~~~~~~~~~~~°\nWhat is your question?\n\n>>'

    def precmd(self, line: str) -> str:
        sline = line.split(' ')
        try:
            if line[0] == '/':
                try:
                    for alias in self.qrefalias.keys():
                        if alias == line[1:len(sline[0])]:
                            return self.qrefalias[alias] + line[len(sline[0]) + 1:]
                    return line[1:]
                except KeyError:
                    print('Command not found')
            else:
                return 'nuthin'
        except IndexError:
            return ''

    # COMMANDS

    def do_quit(self, args: str):
        """Exits the app
        Params: None
        Aliases: exit, close"""
        exit(0)

    def default(self, line: str) -> None:
        try:
            if self.settings['ChaosMode']:
                print(choice(self.chaos_answers))
            else:
                raise IndexError
        except IndexError:
            print('\n' + choice(self.thoughts))
            print(choice(choice(self.all_answers)))
        print()


c = Console()
c.cmdloop()
