import os

try:
    import random
except:
    os.system('pip install random')

try:
    import pyfiglet
except:
    os.system('pip install pyfiglet==0.7')



res = pyfiglet.figlet_format("WIFI CARD GUESSER!", font="slant")
print(res)
print("### Developed by Youssef Alkhodary: https://userjoo9.github.io/youssefinfo/#main  ###\n")

def Guesser():
    try:

        print("\nNote!!: Card Start With Number?\nExcept '0' !!\n")
        approx = input("Card Start Number: ")

        print("\nNote!!: The Card Length Starts From 6 to 9 Maximum!!\n")
        length = int(input("The Length of Card: "))

        print("\nNote!!: The Amount Recommended is 60 to 100 !!!\n")
        amount = int(input("Amount of Cards You Need: "))

        if approx == "" or approx == " ":
            print("You Must Insert Minimum The First Number From Card to Guessing it")

        elif approx.isdecimal():
            if length == 6:
                start = str(approx) + "00000"
                end = str(approx) + "99999"
                table = random.sample(range(int(start), int(end)), amount)
                print(table)
            elif length == 7:
                start = str(approx) + "000000"
                end = str(approx) + "999999"
                table = random.sample(range(int(start), int(end)), amount)
                print(table)
            elif length == 8:
                start = str(approx) + "0000000"
                end = str(approx) + "9999999"
                table = random.sample(range(int(start), int(end)), amount)
                print(table)
            elif length == 9:
                start = str(approx) + "00000000"
                end = str(approx) + "99999999"
                table = random.sample(range(int(start), int(end)), amount)
                print(table)


        else:
            print("\nThis Card Guessing Values Not Available!")
        print("\nRun Again..?  (Y)es - (N)o")
        sw = input(">> ")
        if sw.lower() == 'y':
            Guesser()
        else:
            pass
    except:
        print("\nAn Error Accord, Must Insert Numeric Value Only!!\n")
        print("\nRun Again..?  (Y)es - (N)o")
        sw = input(">> ")
        if sw.lower() == 'y':
            Guesser()
        else:
            pass

Guesser()