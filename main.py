from cgi import print_form
from lib2to3.pgen2 import driver
from pprint import pprint
from tkinter import RADIOBUTTON
from tokenize import Name
from unicodedata import name
from account import Account
from car import Car
from driver import Driver
from payment import payment
from route import Route
from user import User


if _name_ == "main":
   print ("Hola mundo")
   
   carro = Car()
   carro.id             =5
   carro.brand          ="toyota"
   carro.driver         ="Diego"
   carro.passanggers    = 5
   carro.printAll(carro)
   
   pprint(vars(carro))        
   
   carro                = Car()
   carro.id             =2
   carro.brand          ="Fiat"
   carro.driver         ="alexandra"
   carro.passanggers    = 5
   
   print(vars(carro))
   print(vars(carro2))
   
   print(vars(User))
   User.id       =5
   User.name     ="Anuel aa"
   User.dociment ="karol"
   User.email    ="example@gmail.com"
   User.password ="123"
   
   print(vars(Route))
   Route.id       =5
   Route.start    ="mansion"
   Route.end      ="terreno" 
   
   print(vars(driver)) 
   Driver.id          =5
   Driver.name        ="Rodrigo"
   Driver.document    ="1752584662"
   Driver.email       ="ejample@gmail.com"
   Driver.password    ="159"