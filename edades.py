pro_m=0
pro_t=0
pro_n=0
for x in range(5):
    edad=int(input("INGRESE EDAD DEL TURNO MAÑANA: "))
    pro_m+=edad
for x in range(6):
    edad=int(input("INGRESE EDAD DEL TURNO TARDE: "))
    pro_t+=edad
for x in range(11):
    edad=int(input("INGRESE EDAD DEL TURNO NOCHE: "))
    pro_n+=edad
pm=pro_m/5
pt=pro_t/6
pn=pro_n/11
print("EL PROMEDIO DEL TURNO MAÑANA ES: ",pm)
print("EL PROMEDIO DEL TURNO TARDE ES: ",pt)
print("EL PROMEDIO DEL TURNO NOCHE ES: ",pn)
if pm>pt and pm>pn:
    print("El promedio mayor es del turno mañana")
elif pm<pt and pt>pn:
    print("El promedio mayor es del turno tarde")
else:
    print("El promedio mayor es del turno noche")
