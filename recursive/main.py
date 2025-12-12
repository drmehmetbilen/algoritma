
def faktoriyel(n):
    if n<=1:
        return 1

    return n * faktoriyel(n-1)

def fibo(x):
    if x<=2:
        return 1
    
    return fibo(x-1)+fibo(x-2)


def liste_toplami(L):
    if len(L)==0:
        return 0
    return L[0]+ liste_toplami(L[1:])

# L = [1,4,62,3,234,23,34,44,100,2,5]
# liste_toplami(L)
        


# sayi = int(input("Lütfen fibonacci değerini hesaplamak istediğiniz sayıyı giriniz."))
# hesaplanan_deger = fibo(sayi)
# print(f"Girmiş olduğunuz {sayi} sayısının hesaplanan fibonacci değeri {hesaplanan_deger} 'dır. ")