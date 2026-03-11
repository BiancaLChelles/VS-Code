

# Condições com if, else e elif em Python



  # Exemplo 2
nota1 = 10
nota2 = 6
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
        print("Aprovada! - NOTA: ", round(media, 2))
elif media >= 5:
        print("Recuperação! - NOTA: ", round(media, 2))    
else:
        print("Reprovada! - NOTA: ", round(media, 2))   

# Exemplo 1
idade = 60
e_membro = True

if idade >= 60:
     if e_membro:
        print("Desconto para idosos membros: 30%")
     else:
        print("Desconto para idosos não membros: 20%")

elif idade>=50:
     if e_membro:
        print("Vale compra com cashe baks de 20% para pessoas entre 50 e 59 anos membros")
     else:
        print("Desconto para pessoas entre 50 e 59 anos não membros: 10%")        
else:
    print("Sem desconto para menores de 60 anos.")        

