a=input("Introduceti primul cuvant: ")
b=input("Introduceti al doilea cuvant: ")
c=input("Introduceti al treilea cuvant: ")
d=input("Introduceti al patrulea cuvant: ")
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print("EROARE")
l1=a[:2]
l2=b[0]
l3=c[:3]
l4=d[:(len(d)//2)]

print("Cuvintele: ",a,b,c,d,sep="  ")
print("Cuvantul format este",l1+l2+l3+l4)
