def czyMiesciWZakresie(n,x,y):
    if n>=x and n<=y:
        odpowiedz=str(n)+f" mieści się w przedziale <{x},{y}>."
    elif n<=x and n>=y:
        odpowiedz=str(n)+f" mieści się w przedziale <{y},{x}>."
    else:
        odpowiedz=str(n)+f" nie mieści się w przedziale <{x},{y}>."
    return odpowiedz
print(czyMiesciWZakresie(5,1,26))