print("Vize ve final notunu gir..!!!!")
X = input()
X = int(X)

Y = int(input())

print("Devamsızlık hafta sayınızı giriniz.!!!!")
D = int(input())

if D<5:
    Z=X*0.4+Y*0.6
    print("Ortalamanız : ",Z)
    if Z>=50:
        print("GEÇTİ")
    else:
        print("KALDI")
else:
    print("KALDI")
        
    

