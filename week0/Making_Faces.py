import re

emocao = input(str("emocao: "))

trocas = {
    "feliz": ":)",
    "triste": ":("
}

pattern = re.compile(r'\b(' + '|'.join(trocas.keys()) + r')\b')
resultado = pattern.sub(lambda m: trocas[m.group(0)], emocao)

print(resultado)
