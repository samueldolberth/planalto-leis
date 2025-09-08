import re
from bs4 import BeautifulSoup

html = "L13709.html"

# Lendo o arquivo HTML
with open(html, "r", encoding="latin-1") as file:
    soup = BeautifulSoup(file, "html.parser")

# Cabeçalho novo (você já tinha feito)
novo_html = [
    "<!DOCTYPE html>",
    "<html lang='pt-BR'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <title>Lei nº 13.709/2018 - LGPD</title>",
    "  <link rel='stylesheet' href='style.css'>",
    "</head>",
    "<body>",
    "  <main class='lei'>"
]

# Regras de regex
regex_capitulo = re.compile(r"^CAP[IÍ]TULO", re.IGNORECASE)
regex_artigo = re.compile(r"^Art\.\s*\d+", re.IGNORECASE)
regex_paragrafo = re.compile(r"^§\s*\d+")
regex_inciso = re.compile(r"^[IVXLCDM]+\s*-")  # números romanos
regex_alinea = re.compile(r"^[a-z]\)")

# Controle para fechar blocos
aberto_capitulo = False
aberto_artigo = False

# Pegando todos os links
for p in soup.find_all("p"):
    texto = p.get_text(strip=True)

    if not texto:
        continue # pula vazio

    if regex_capitulo.match(texto):
        if aberto_artigo:
            novo_html.append("      </article>")
            aberto_artigo = False
        if aberto_capitulo:
            novo_html.append("    </section>")
        novo_html.append(f"    <section class='capitulo'><h2>{texto}</h2>")
        aberto_capitulo = True

    elif regex_artigo.match(texto):
        if aberto_artigo:
            novo_html.append("      </article>")
        novo_html.append(f"      <article class='artigo'><h3>{texto}</h3>")
        aberto_artigo = True

    elif regex_paragrafo.match(texto):
        novo_html.append(f"        <p class='paragrafo'>{texto}</p>")

    elif regex_inciso.match(texto):
        novo_html.append(f"        <p class='inciso'>{texto}</p>")

    elif regex_alinea.match(texto):
        novo_html.append(f"        <p class='alinea'>{texto}</p>")

    else:
        novo_html.append(f"        <p>{texto}</p>")



# Fechar últimos blocos
if aberto_artigo:
    novo_html.append("      </article>")
if aberto_capitulo:
    novo_html.append("    </section>")

# Fechar tags principais
novo_html.extend([
    "  </main>",
    "</body>",
    "</html>"
])

# salva o resultado
with open("lei_estruturada.html", "w", encoding="utf-8") as f:
    f.write("\n".join(novo_html))


print("Lei estruturada salva em lei_estruturada.html")