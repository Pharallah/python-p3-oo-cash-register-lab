#!/usr/bin/env python3
import ipdb

class CashRegister:
  def __init__(self, discount=0, total=0, items=None, last_transaction_amount=0):
    self.discount = discount
    self.total = total
    
    if items is None:
      self.items = [] # If empty list
    else:
      self.items = items # Else, populate

    self.last_transaction_amount = last_transaction_amount

  def add_item(self, item, price, quantity=1):
    # Calculates total price
    self.total += price * quantity 
    current_items = []
    
    if quantity == 1:
      current_items.append(item)
    else:  
      if quantity > 1:
        i = 1
        while i <= quantity:
          current_items.append(item)
          i += 1

    self.items.extend(current_items)
    self.last_transaction_amount = price * quantity

    return self.items

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      percent_discount = float(self.discount / 100)
      discount_in_dollars = self.total * percent_discount
      int_total = int(self.total - discount_in_dollars)
      self.total = int_total
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if self.last_transaction_amount != 0:
      self.total -= self.last_transaction_amount
      self.last_transaction_amount = 0 # Reset LTA
      self.items.remove(self.items[-1]) # Removes last item
    else:
      print("No transaction to void")

    if len(self.items) == 0:
      return 0.0
    

new_register = CashRegister()
new_register.add_item("eggs", 1.99)

# ipdb.set_trace()


