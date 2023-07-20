import string
import random


def mainmenu():
  print(" ")

  print("WELCOME TO PASSWORD MANAGER")
  print("MAIN MENU:")

  print(" ")

  print("Enter \"New\" to enter a new password.")
  print("Enter \"read\" to know the saved password.")
  print(" ")

  user_input = input("Please enter option from the above given menu: ")

  if user_input == "New":
    add_newpasswd()
  elif user_input == "read":
    readPasswords()
  else:
    print("ERROR: The option you have chosen is incorrect")
    print("Please choose the option from the given menu!!!")
    print(" ")


def add_newpasswd():
  if True:
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter passward length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    global p
    print("your passwars is: ")
    p = "".join(s[0:plen])

    print("".join(s[0:plen]))
    q = input("Enter \"yes\" or \"No\" Do you want to save the passward? ")
    if q == "Yes":
      store()
    else:
      print("thank you your Password is saved")


def store():
  file = open("info.txt", 'a')
  userName = input("Please enter the user name: ")
  usrnm = "UserName: " + userName
  pwd = " Password: " + p + "\n"
  file.write(usrnm)
  file.write(pwd)
  file.close


def readPasswords():
  username = input("Enter the user name: ")
  file = open('info.txt', 'r')
  s = ' '
  while s:
    s = file.readline()
    if s[0] == "username":
      print("your password is: ", s)
  file.close()


mainmenu()
