from classes import LatLon

# Design a store using OOP methodologies

class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return f'{self.name} costs ${self.price}'

class Department:
  # products with a list of tuples with signature (string, int)
  def __init__(self, name, products=[]):
    self.name = name
    self.products = products

  def __str__(self):
    return f'Welcome to the {self.name} department!'

  def add_product(self, product, price):
    self.products.append(Product(product, price))

  def print_products(self):
    for p in self.products:
      print(p)

# What does this store look like?
# What are the attributes we care about?
# name
# location
# categories of products

class Store:
  def __init__(self, name, lat, lon, departments):
    self.name = name
    self.location = LatLon(lat, lon)
    self.departments = [Department(d) for d in departments]
  
  def __str__(self):
    return f'Store {self.name}, {self.location}, {self.departments}'

  def print_products(self):
    for d in self.departments:
      d.print_products()

  def print_departments(self):
    for d in self.departments:
      print(d)

store = Store('LambdaStore', 44.13455, -121.123124, ['Clothing', 'Cookware', 'Books', 'Sporting Goods'])
# print(store)

products_and_departments = {
  "Clothing": [Product("Hurley Long-sleeve T-shirt", 25), Product("5-Pack Basic White Tees", 20)],
  "Cookware": [Product("Cast Iron Frying Pan", 30), Product("George Foreman Grill", 45), Product("Olive Wood Kitchen Spoons Set", 25)],
  "Books": [Product("Game of Thrones", 15), Product("Start With Why", 20), Product("Startup CEO", 18)],
  "Sporting Goods": [Product("Little League Baseball Bat", 25), Product("Boxing Gloves - Large", 45)]
}

# store.departments[1].add_product('George Foreman Grill', 45)
# store.departments[2].add_product('Start With Why', 20)

store.print_products()
store.print_departments()

# we want to add departments
# let's take input from the user and have them specify departments by index in the departments list

# wrap all this logic in a while loop so that we can keep giving selections
# instead of having to re-run the program every time

while True:
  selection = input('Select the number of a department or type "exit" to leave: ')

  if selection == 'exit':
    print('Thanks for shopping with us!')
    break

  # add error handling so that when a user inputs a department for a non-existent department,
  # we'll notify them that the department does not exist
  try:
    #casting might cause an error
    selection = int(selection)
    if selection >= len(store.departments):
      print("That's not a valid department")
    elif selection >= 0 and selection < len(store.departments):
      print(f'{store.departments[selection]}')
    else:
      print('Department numbers are positive')
  except ValueError:
    #the user didn't give us a value that could be cast to a number
    print('Please enter your choice as a number, or type "exit" to leave')

# when should we break out of this loop?
# let's let the user type "exit" into the selection to have them leave