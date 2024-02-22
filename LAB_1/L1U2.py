#printar alla delar av receptet.
def recept(antal):
    print("\nSockerkaka recept för", antal, "personer:")
    print("-", int(round(antal*0.75, 0)), "st ägg")
    print("-", round(antal*0.75, 1), "dl strösocker")
    print("-", round(antal*0.50, 1), "tsk vaniljsocker")
    print("-", round(antal*0.50, 1), "tsk bakpulver")
    print("-", round(antal*0.75, 1), "dl vetemjöl")
    print("-", int(round(antal*18.75, 1)), "g smör")
    print("-", round(antal*0.25, 1), "dl vatten")

#för tidsberäkning.
def tidblanda(antal):
    tidBlanda = int(10+antal)
    return tidBlanda

#för tidsberäkning.
def tidgradda(antal):
    tidGradda = int(30+(3*antal))
    return tidGradda

#main funktion.
def sockerkaka(antal):
    recept(antal)
    tidTotal = tidblanda(antal) + tidgradda(antal)
    print("\nAtt baka kakan tar sammanlangt", tidTotal, "minuter.\n")

#min "script"? Jag har ju redan gjort allt i funktionerna.
sockerkaka(4)
sockerkaka(7)

#om man vill skriva själv antal personer.
#antal = int(input("\nAntalet personer som kakan ska ätas av: "))