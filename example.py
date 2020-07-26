from tkinter import Tk
import argui

# Syntax: argui.Argui(tkinter.Tk, target=None, filename=None) where target is the executable and filename is the file output is piped to
app = argui.Argui(Tk())

# Put app.addField() calls below
# Example calls included below
# Syntax: argui.Argui.addField(argname, style='default', width=28, insert_name=False, regex=None)
# The style parameter adds input filtering (includes 'require', 'integer', 'double'/'float', 'string' as well as aliases, use a space to seperate each style, example: 'require integer')
# The regex parameter needs a argui.Regex object, usage: argui.Regex(expression, description)
app.addField('Basic')                                                                   # Basic field
app.addField('--insert-name', insert_name=True)                                         # Insert the name of the argument before the argument
app.addField('Custom Width', width=48)                                                  # Extra wide text entry box
app.addField('Required', style='require')                                               # Required Input
app.addField('Integer', style='integer')                                                # Input must be an integer
app.addField('Double', style='double')                                                  # Input must be a double (no decimal required)
app.addField('Float', style='float')                                                    # Input must have 1 decimal point and no more than one
app.addField('String', style='string')                                                  # Equivalent to the 'default' filter; Serves no purpose except for reference
app.addField('Regex', regex=argui.Regex('^[a-zA-z0-9_]+$','Alphanumeric Input Only'))   # Regexes need to match the entire string, so this might be an automatic 'require' style depending on your regex.

app.finishSetup()
app.mainloop()
