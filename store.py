# Python Store Inventory by bennyman123abc
#
# This was built as a simple coding project yet, I hope someone will find
# some use out of it. Even if that use is just reading the source code to
# learn Python.

import os
import sys
from textuilib3 import menu, menuItem, setHeader, getHeader, clear
import textuilib3 as ui
#import PyCrypto as pycrypto (This will be implemented with the admin and user system)

# Inventory Class
# - This class implements a basic inventory for multiple inventory stores
class Inventory:
  def __init__(self, name): # For now, all we are going to require is a name for inventory initialization
    if isinstance(name, str): # We need to make sure that the name is a string so we don't crash later
      self.name = name # This will set the internal variable 'name' to the value of our provided string
      
    self.itemList = [] # This sets the item list to an empty array (List) so we can add items to it later
    
  def addItem(self, item): # This will add a provided item to self.itemList
    canAdd = True
    if isinstance(item, Item): # This makes sure that the provided item is actually an Item object
      for it in self.itemList: # This checks every item in the array (List), self.itemList to make sure we aren't trying to add a duplicate.
        if it == item:
          canAdd = False # This tells the function that the item can't be added.
      if canAdd == True:
        self.itemList.append(item) # This adds the item to the end of the list. It does not matter because the list can be sorted when being displayed to the user.

  def removeItem(self, item): 
# Item Class
# - This class implements the main item that will be used to store items in an inventory
