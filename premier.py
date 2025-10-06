

n=int(input("entrer un nombre:"))
premier=True
for diviseur in range (2,n):
    reste=n% diviseur
    if reste==0:
        print(n,"n'est pas premier car divisible par",diviseur) 
        premier=False
        
print(n,"est premier !")

#YO