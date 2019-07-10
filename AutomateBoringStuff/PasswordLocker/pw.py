#! python 3
# pw.py - An insecure password locker program

PASSWORDS = {
    'yahoo': 'CarlCox1',
    'gmail': 'Elfingham1',
    'facebook': 'Elfingham7',
    'google': 'Elfingham8'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage: python pw.py[account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account)
