#main funktion.
def kostnad(P, r, a):
    k = P + (a+1)*P*r/2
    print("Den totala kostnaden efter", a, "år är", int(k), "kr.")

#min "script".
kostnad(50000, 0.03, 10)