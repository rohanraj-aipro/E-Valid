import colorama
from colorama import Fore, Back, Style
from validate_email import validate_email

print(Fore.MAGENTA, Back.BLACK +        '########         ##     ##    ###    ##       #### ########  ')
print(Fore.LIGHTBLUE_EX, Back.BLACK +   '##               ##     ##   ## ##   ##        ##  ##     ## ')
print(Fore.LIGHTYELLOW_EX, Back.BLACK + '##               ##     ##  ##   ##  ##        ##  ##     ## ')
print(Fore.RED, Back.BLACK +            '######   ####### ##     ## ##     ## ##        ##  ##     ## ')
print(Fore.GREEN, Back.BLACK +          '##                ##   ##  ######### ##        ##  ##     ## ')
print(Fore.LIGHTCYAN_EX, Back.BLACK +   '##                 ## ##   ##     ## ##        ##  ##     ## ')
print(Fore.LIGHTRED_EX, Back.BLACK +    '########            ###    ##     ## ######## #### ########  ')

print(Fore.YELLOW, Back.BLACK + '       An OSINT Tool To Check Whether if an email or domain is Valid or Not')

print(Fore.GREEN + """

                             /^\/^\\
                             \----|
                         _---'---~~~~-_
                          ~~~|~~L~|~~~~
                             (/_  /~~--
                           \~ \  /  /~
                         __~\  ~ /   ~~----,
                         \    | |       /  \\  SHERLOCK-HOLMES OSINT TOOL
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \\---'
                      //_- |  |          \\
                     //   |____|\______\__\\
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\\


""", end ="")
print(Fore.LIGHTRED_EX, Back.BLACK + 'Made By Hacker--Rohan Raj\n')

yourmail = input(Fore.CYAN + "Please Enter an Email to Check if it is Valid or Not:-\n")

is_valid = validate_email(yourmail)
print(is_valid)
