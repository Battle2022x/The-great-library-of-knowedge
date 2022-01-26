# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "is Taiwan a country"
answer = "no"
username = "Conner"
password = "chingchong"
my_auth.set_authorization(username,password)
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
