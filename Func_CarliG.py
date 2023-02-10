# definizione della funzione
def saluto():
    run=True
    c=0
    stop=10
    while run== True:
        print("Buongiorno, questo è il contributo di  Carli Gianmarco  ")
        c += 1
        if c > stop:
            print("Direi che ora posso smetterla di salutarla :)")
            break
        
# chiamata della funzione
saluto()
