while True:
    n=input("Enter an integer between 1 to 10 : ")
    try:
      n = int(n)
      if n>10:
          raise IndexError
      reciprocal=1/n
      print (" The reciprocal  of your number is",reciprocal)
      break

    except TypeError:
      print("You did not enter an integer!!!\n please try again.")
    except ValueError:
      print("You did not enter an integer!!!\n please try again.")
    except IndexError:
        print("You did not enter a number between 1 to 10!!! \n Please,try again.")

    except ZeroDivisionError:
      print("Oops, you entered zero. ")

