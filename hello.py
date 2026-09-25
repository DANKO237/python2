#nombre = int(input("entrer un nombre"))
#if (nombre % 2 == 0):
#    print("le nombre est paire")
#else:
#    print("le nombre est impair")

#sigle = input(cmr)
#if(sigle == cmr):
    #print("la nationalité est camerounaise")
#elif(sigle == gb):
    #print("la nationalité est: Gabonaise")
#else :
    #print("il n'a pas de nationalmité")  


#for i in range(13):
 #   print(f"{5 * i} = {5 * i}")   
#mot_pass = "1234"
#user_pass = ""
#while(mot_pass != mot_pass):
   # print(f"mot de pass incorrect")
#mot_pass = input("entrer un mot de pass") 
# 1)
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
# 2)
nombre1 = int(input("entré un nombre: "))
nombre2 = int(input("entré un nombre: "))
operateur = input("entré un operateur: ")
def operation(nombre1,nombre2):
    if(operateur == "+"):
        print(f"{nombre1} + {nombre2} ={add(nombre1, nombre2)}")
    elif (operateur == "-"):     
        print(f"{nombre1} - {nombre2} = {subtract(nombre1, nombre2)}")
    elif(operateur == "*"):    
        print(f"{nombre1} * {nombre2} = {multiply(nombre1, nombre2)}")
    elif(operateur == "/"):    
        print(f"{nombre1} / {nombre2} = {divide(nombre1, nombre2)}")
    else:    
        print(f"entrer un operateur valide")
operation(nombre1, nombre2)        
# 3)
def grade(score):
    return score
score = float(input("entrer votre score: "))
if(grade(score)>= 10):
    print(f"votre resultat est: Reussi")
else:
    print(f"votre resultat est: echec") 
# 4)
if(grade(score)< 10):
    print(f"votre grade est: F")
elif(grade(score)< 12):
    print(f"votre grade est: D")
elif(grade(score)< 14):
    print(f"votre grade est: C")
elif(grade(score)<18):
    print(f"votre grade est: B")
else:
    print(f"votre grade est: A")     
# 5)
def grade(score=50):
    if(score>=50):
      print(f"{grade}={reussi}")
      return True
    else:
        print(f"{grade}={echec}")
        return False  
    
                         