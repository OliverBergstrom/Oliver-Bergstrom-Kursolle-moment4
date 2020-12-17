# uppgift 5

start = 0 # detta gör så att koden kan köras om ifall värdet fortfarande blir 0
lenlim = 0 # lenlim kollar så att längden blir ett giltigt tal
while start == 0:
    while lenlim == 0: # den kommer att stanna på 0 tills Längd blir ett giltigt tal
        Längd = int(input("Ange längd")) # längd värdet sparas i variabeln Längd vilket användaren väljer
        lenlim+=1
        if isinstance(Längd, str):
            lenlim = 0
    Bredd = int(input("Ange bredd")) # bredd värdet sparas i variabeln Bredd vilket användaren väljer
    Höjd = int(input("Ange höjd")) # höjd värdet sparas i variabeln Höjd
    if Höjd < 0: # detta gör så att höjdens värde aldrig kan bli mindre än 0 och mer än 10
        Höjd = 1
    elif Höjd > 10:
        Höjd = 10

    def area(Längd, Bredd):
        return (Längd*Bredd) # areans värde sparas i variabeln Area och är summan på Längd gånger Bredd

    Area = area(Längd,Bredd)

    if Längd == Bredd: # ifall längden och breddens värde är detsamma då är det en kvadrat
        print(f"Arean är {Area} och den är en kvadrat")
    else:
        print(f"Arean är {Area} och den är en rektangel")

    for Höjd in range(1,Höjd+1): # höjdens värde är hur många gånger den ska räkna ut volymen
        Volym = Höjd*Area
        print(f"Volymen för höjden {Höjd} är {Volym}")
        
    start+=1 # värdet ändras till 1 för att koden ska stanna

    if input("Vill du starta om? Y/yes N/no").lower() != 'y': # kollar ifall användaren vill starta om koden
        break                             
    else:
        start = 0 # ifall användaren skrev Y eller y så ändras startvärdet till 0