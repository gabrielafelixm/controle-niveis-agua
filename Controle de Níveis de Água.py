from colorama import Fore, Style, init

init()

# Lista com os níveis já escritos
lista = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]

# Função que retorna a cor conforme o nível
def cor_do_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Exibindo cada nível com sua cor
for indice, mensagem in enumerate(lista):
    nivel = indice + 1
    cor = cor_do_nivel(nivel)
    print(cor + mensagem + Style.RESET_ALL)
