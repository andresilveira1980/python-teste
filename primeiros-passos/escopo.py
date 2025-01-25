print('-----------------------Programa de escopo ----------------------')
print()

def mostrar():
    profissao = 'rei do rock'
    nome = 'Élvis Présley'
    return f"O sr.{nome} tem como profissão {profissao}."

idade = 42
print (mostrar())
mostrar()
# print(profissao) fora do escopo que é a função já fica indicando erro

print(idade)