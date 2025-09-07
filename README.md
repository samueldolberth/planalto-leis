# Analisando o HTML do Planalto

O HTML do Planalto (como o da LGPD) geralmente não usa classes modernas. Ele segue um estilo antigo, com marcação semântica pobre e, muitas vezes, com tags de apresentação (`<font>`, `<b>`, `<u>`) ou apenas `<p>` para tudo.

---
## O que você vai encontrar nesse HTML

- Nenhuma classe ou id (em 99% dos casos).

- Estrutura baseada em:

    - `<p>` para cada artigo/linha.

    - `<b>` ou `<strong>` para títulos/capítulos.

    - `<center>` em alguns documentos.

    - `<br>` quebrando linhas em vez de usar `<h2>`, `<h3>`.

### Exemplo real de trecho:

''' <p style="text-align:center"><b>LEI Nº 13.709, DE 14 DE AGOSTO DE 2018</b></p>
<p>Dispõe sobre a proteção de dados pessoais...</p>
<p><b>CAPÍTULO I<br>DISPOSIÇÕES PRELIMINARES</b></p>
<p>Art. 1º Esta Lei dispõe sobre...</p> '''

O objetivo é envelopar o conteúdo original em blocos semânticos, sem mexer no texto da lei. Assim, criando ganchos CSS.

### Exemplo de reorganização:
'''
<body>
  <header>
    <h1>Lei nº 13.709, de 14 de agosto de 2018</h1>
    <p class="subtitulo">Lei Geral de Proteção de Dados Pessoais (LGPD)</p>
  </header>

  <main class="lei">
    <section class="capitulo">
      <h2>CAPÍTULO I — Disposições Preliminares</h2>
      <article class="artigo">
        <h3>Art. 1º</h3>
        <p>Esta Lei dispõe sobre...</p>
      </article>

      <article class="artigo">
        <h3>Art. 2º</h3>
        <p>São fundamentos da disciplina da proteção de dados pessoais: ...</p>
      </article>
    </section>

    <section class="capitulo">
      <h2>CAPÍTULO II — Do Tratamento de Dados Pessoais</h2>
      <!-- segue -->
    </section>
  </main>
</body>
'''

### criar um conjunto pequeno e semântico:
- .lei → container geral da lei.


- .capitulo → agrupa cada capítulo.


- .artigo → cada artigo.


- .subtitulo → descrição abaixo do título principal.


- .paragrafo → se quiser separar §§ de dentro dos artigos.


O desafio é que o HTML do Planalto é pouco semântico, então é preciso criar regras de parsing para detectar os elementos (Capítulo, Artigo, §, etc.) e aplicar classes/estruturas modernas.

## Padrões que aparecem no HTML do Planalto
Ao analisar leis como a LGPD, é encontrado sempre repetições previsíveis:

- Capítulos → quase sempre escritos como:
    - CAPÍTULO I, CAPÍTULO II, … seguidos do título em maiúsculas.


- Artigos → começam com Art. e um número (Art. 1º, Art. 2º, …).


- Parágrafos → começam com § 1º, § 2º, etc.


- Incisos → numerados com algarismos romanos (I -, II -, III - …).


- Alíneas → letras minúsculas seguidas de `)` → `a)`, `b)`, etc.


- Esses padrões podem ser detectados por regex.
