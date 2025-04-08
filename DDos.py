import pyfiglet
import termcolor 


print(termcolor.colored(pyfiglet.figlet_format("DDos"),color="red"))

print(termcolor.colored("1: Ddos Samp Ddos number is : 1",color="red"))
print(termcolor.colored("2: Ddos Https number is : 2",color="red"))
print(termcolor.colored("3: Ddos Network number is : 3",color="red"))
print(termcolor.colored("4: Ddos Ip number is : 4",color="red"))

enter = int(input("Enter Number of Ddos :"))

ddos1 = 1
ddos2 = 2
ddos3 = 3
ddos4 = 4

v = 0
o = 0



if enter == ddos1:
    print("DDos Samp Done ")
    ddos = input("Enter Ip Of surver :")
    while ddos != ",":
        print(f"Attack Sent {ddos}")
        if v < 10000:
            v += 1 
    else:
        print("Surver Down")
elif enter == ddos2:

    print("DDos Https Done ")
    ddosh = input("Enter Https Of WebSite :")
    
elif enter == ddos3:

    print("DDos Network Done ")
    net = input("Enter Ip Of Network :")
    while net != ",":
        print(f"Attack Sent {net}")
        if v < 10000:
            v += 1 
    else:
        print("Surver Down")

elif enter == ddos4:
    print("DDos Ip Done ")
    ph = input("Enter Ip Of Phone :")

    while ph != ",":
        print(f"Attack Sent {ph}")
        if v < 10000:
            v += 1 
    else:
        print("Surver Down")
else:
    print("Not Foned")

while ddosh != "":
    print(f"Attack Sent {ddosh}")
    if o < 100000:
        o += 1
else:
    print("Surver Down")

