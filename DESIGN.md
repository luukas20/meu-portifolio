---
name: Lucas Costa | Portfólio de Dados
description: Portfólio claro, limpo e profissional de um estatístico: fundo frio, tinta azul-grafite, um único acento verde-azulado e uma curva normal discreta como assinatura.
colors:
  fundo: "#f7f8fa"
  superficie: "#ffffff"
  superficie-suave: "#f1f4f8"
  linha: "#e2e6ec"
  linha-forte: "#cbd2dc"
  tinta: "#0e1726"
  tinta-suave: "#475569"
  tinta-fraca: "#64748b"
  acento: "#0b7a75"
  acento-forte: "#075e5a"
  acento-suave: "#e3f3f2"
  escuro: "#0e1726"
  texto-escuro: "#f7f8fa"
  texto-escuro-suave: "#a9b4c6"
  acento-no-escuro: "#3dd6c8"
  erro: "#b42318"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(2.75rem, 7vw, 4.75rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Bricolage Grotesque, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 3.6vw, 2.6rem)"
    fontWeight: 650
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Bricolage Grotesque, Segoe UI, system-ui, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 650
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  lead:
    fontFamily: "Onest, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.15rem, 2.2vw, 1.45rem)"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "Onest, Segoe UI, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Onest, Segoe UI, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.4
rounded:
  raio: "12px"
  raio-grande: "22px"
  pilula: "999px"
spacing:
  gutter: "clamp(1.25rem, 4vw, 2rem)"
  largura-site: "72rem"
  secao: "clamp(3.5rem, 8vw, 6rem)"
components:
  button-primary:
    backgroundColor: "{colors.acento}"
    textColor: "{colors.superficie}"
    rounded: "{rounded.raio}"
    padding: "0.65rem 1.25rem"
    height: "2.9rem"
  button-primary-hover:
    backgroundColor: "{colors.acento-forte}"
  button-outline:
    backgroundColor: "{colors.superficie}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.raio}"
    padding: "0.65rem 1.25rem"
    height: "2.9rem"
  button-light:
    backgroundColor: "{colors.texto-escuro}"
    textColor: "{colors.escuro}"
    rounded: "{rounded.raio}"
    padding: "0.8rem 1.5rem"
    height: "3.25rem"
  button-outline-light:
    backgroundColor: "transparent"
    textColor: "{colors.texto-escuro}"
    rounded: "{rounded.raio}"
    padding: "0.8rem 1.5rem"
    height: "3.25rem"
  card-projeto:
    backgroundColor: "{colors.superficie}"
    rounded: "{rounded.raio-grande}"
    padding: "1.4rem 1.5rem 1.5rem"
  tag:
    backgroundColor: "{colors.superficie}"
    textColor: "{colors.tinta-suave}"
    rounded: "{rounded.pilula}"
    typography: "{typography.label}"
    padding: "0.2rem 0.65rem 0.2rem 0.5rem"
  chip:
    backgroundColor: "{colors.superficie}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.pilula}"
    padding: "0.4rem 0.9rem"
  selo-cargo:
    backgroundColor: "{colors.superficie}"
    textColor: "{colors.tinta}"
    rounded: "14px"
    padding: "0.7rem 1rem"
  selo-atual:
    backgroundColor: "{colors.acento-suave}"
    textColor: "{colors.acento-forte}"
    rounded: "{rounded.pilula}"
    padding: "0.05rem 0.55rem"
  chat-bolha-usuario:
    backgroundColor: "{colors.acento}"
    textColor: "{colors.superficie}"
    rounded: "16px"
    padding: "0.65rem 0.95rem"
  chat-bolha-bot:
    backgroundColor: "{colors.superficie}"
    textColor: "{colors.tinta}"
    rounded: "16px"
    padding: "0.65rem 0.95rem"
---

# Design System: Lucas Costa | Portfólio de Dados

## Overview

**Creative North Star: "O Relatório Claro"**

O site se comporta como um bom relatório executivo: fundo frio e arejado, superfícies brancas, tinta azul-grafite e um único acento verde-azulado que marca ação, estado atual e dados. O conteúdo real (nome, três frentes, trajetória, projetos) lidera; a interface recua. Foi feito para ser lido rápido, em geral no celular, por recrutadores e gestores.

A personalidade vem da tipografia (Bricolage Grotesque nos títulos, com tracking apertado, e Onest no texto), de filetes de 1px no lugar de molduras pesadas e de sombras suaves, de baixo contraste e com deslocamento vertical. A única assinatura é estatística: uma curva normal em traço fino no pé da primeira tela, mais o selo do cargo atual sobre a foto no desktop. Currículo é propositalmente discreto: botão de contorno no menu e botão secundário na faixa de contato.

Recusado de forma confirmada: o visual temático e ornamental da versão anterior (descartada pelo Lucas) e o "portfólio de dev" genérico com neon, degradês e cartões idênticos com ícone. Sem emojis.

**Key Characteristics:**
- Fundo frio (`fundo`), superfícies brancas (`superficie`), faixa escura (`escuro`) apenas em "Vamos conversar" e no rodapé.
- Um único acento (`acento`); `acento-no-escuro` existe só para a faixa escura.
- Títulos em Bricolage Grotesque 650 a 700, texto em Onest, ambas hospedadas em `public/static/fonts`.
- Filetes (`linha`, `linha-forte`) estruturam; sombras são suaves e raras.
- Cantos de 12px em controles, 22px em cartões e foto.
- Movimento curto: entrada da primeira tela com `surgir` e easing `cubic-bezier(0.16, 1, 0.3, 1)`; respeita `prefers-reduced-motion`.

## Colors

Paleta fria e contida: neutros azulados, uma cor de ação verde-azulada e uma faixa escura da mesma tinta do texto.

### Primary
- **Verde-azulado de ação** (`acento`, #0b7a75): botão primário, link com seta, item atual do menu, marcador do cargo atual na trajetória, bolha do usuário, botão do chat, filete curto sobre cada especialidade, traço e área da curva normal (em opacidade baixa), caret e `accent-color`. Contraste sobre branco acima de AA.
- **Verde-azulado profundo** (`acento-forte`, #075e5a): hover de botão e link, texto do selo "Atual".
- **Névoa verde-azulada** (`acento-suave`, #e3f3f2): fundo do selo "Atual", área da curva, seleção de texto.
- **Verde-azulado luminoso** (`acento-no-escuro`, #3dd6c8): somente sobre `escuro`: foco e hover de redes sociais.

### Neutral
- **Fundo frio** (`fundo`, #f7f8fa): fundo da página e da caixa de mensagens do chat.
- **Superfície branca** (`superficie`, #ffffff): cabeçalho, cartões, chips, tags, selo, janela do chat.
- **Superfície suave** (`superficie-suave`, #f1f4f8): faixas alternadas de seção (Meu portfólio, Sobre), moldura de imagem, bloco da fórmula.
- **Filete** (`linha`, #e2e6ec) e **filete forte** (`linha-forte`, #cbd2dc): divisórias e bordas; o forte abre listas e contorna botões e o botão de menu.
- **Tinta** (`tinta`, #0e1726): títulos e texto principal.
- **Tinta suave** (`tinta-suave`, #475569): parágrafos, descrições e rótulos secundários.
- **Tinta fraca** (`tinta-fraca`, #64748b): legendas, subtítulo do chat, placeholder, autor da citação.
- **Faixa escura** (`escuro`, #0e1726) com `texto-escuro` (#f7f8fa) e `texto-escuro-suave` (#a9b4c6): contato e rodapé. Filetes sobre ela usam `linha-escuro` (rgb(247 248 250 / 0.24)).
- **Erro** (`erro`, #b42318): contorno da mensagem de erro do chat, único uso.

### Named Rules
**The One Teal Rule.** O verde-azulado é a única cor de croma alto e só significa ação, estado atual ou dado. Nada decorativo recebe `acento`.

**The Dark Band Rule.** `escuro` aparece apenas em "Vamos conversar" e no rodapé, como fecho. Nenhuma outra seção vira escura.

## Typography

**Display Font:** Bricolage Grotesque (com Segoe UI, system-ui, sans-serif), variável 200 a 800.
**Body Font:** Onest (com Segoe UI, system-ui, sans-serif), variável 100 a 900.

**Character:** Bricolage dá ao título um tom atual e jovem sem perder seriedade; Onest mantém o texto neutro e legível. Títulos usam `text-wrap: balance`.

### Hierarchy
- **Display** (700, `clamp(2.75rem, 7vw, 4.75rem)`, 1.02, -0.03em): o nome na primeira tela. Em desktop baixo (altura até 820px) escala por `7vh`, até 4.25rem.
- **Headline** (650, `clamp(1.75rem, 3.6vw, 2.6rem)`, 1.1, -0.02em): títulos de seção.
- **Title** (650, 1.2rem, 1.25, -0.015em): cartões de projeto, especialidades, empresas da trajetória (1.3rem), frentes (1.05rem).
- **Lead** (Onest 400, `clamp(1.15rem, 2.2vw, 1.45rem)`, 1.4, máx. 30ch): frase de posicionamento.
- **Body** (Onest 400, 1.0625rem, 1.65): texto corrido; parágrafos longos ficam entre 52ch e 62ch.
- **Label** (Onest 500, 0.8125rem a 0.95rem): tags, chips, períodos. Sem caixa alta e sem espaçamento largo.

### Named Rules
**The Tight Display Rule.** Só Bricolage Grotesque recebe tracking negativo (-0.01em a -0.03em); Onest nunca é apertada.

## Layout

Coluna única centrada, `largura-site` de 72rem, com `gutter` fluido (1.25rem a 2rem) como respiro lateral. Seções têm padding vertical `clamp(3.5rem, 8vw, 6rem)` e alternam `fundo` com `superficie-suave` (com filetes acima e abaixo). Mobile primeiro, com quatro pontos de quebra: 40rem (chat mais largo, cursos em duas colunas), 48rem (curva aparece, cartões e especialidades em grade, trajetória em duas colunas, selo se desloca), 64rem (menu horizontal, primeira tela em duas colunas 1.1fr/0.9fr, selo do cargo sobre a foto, sobre em duas colunas) e desktop baixo (`min-width: 64rem` e `max-height: 820px`, que compacta a primeira tela para caber inteira).

Primeira tela: no celular a ordem é nome, posicionamento, cargo atual em linha com marcador, botões, frentes (frase + etiquetas), foto; no desktop a linha do cargo some (o selo a substitui) e a ordem é a mesma, sem a linha do cargo: nome, posicionamento, botões, frentes. Cada frente tem o título, uma frase de impacto em tinta forte e as ferramentas e temas em etiquetas pequenas (`.frente-itens`). A trajetória é uma linha do tempo vertical de 2px com marcos circulares. Projetos: 1 coluna, 2 a partir de 48rem. Especialidades: 3 colunas a partir de 48rem. O rodapé reserva 5.5rem embaixo para o botão flutuante do chat.

## Elevation & Depth

Híbrido, mas majoritariamente plano: a estrutura vem de filetes e do contraste entre `fundo`, `superficie` e `superficie-suave`. Sombras existem só em objetos que flutuam ou se destacam, sempre suaves, azuladas (base `#0e1726`) e com deslocamento vertical e blur amplo.

### Shadow Vocabulary
- **Repouso do cartão** (`box-shadow: 0 1px 2px var(--sombra-suave)`): cartões de projeto.
- **Foto e citação** (`0 30px 50px -28px var(--sombra-media)` na foto; `0 24px 40px -28px var(--sombra-media)` na citação): peso para os dois elementos de destaque.
- **Selo e botão primário** (`0 16px 28px -14px var(--sombra-media)` no selo; `0 6px 14px -8px var(--sombra-media)` no botão primário).
- **Flutuantes** (menu aberto `0 24px 30px -24px`; janela do chat `0 30px 60px -20px`; botão do chat `0 16px 28px -10px` mais `0 2px 6px var(--sombra-suave)`).

### Named Rules
**The Soft Lift Rule.** Sombra sempre com deslocamento vertical, blur amplo e valores negativos de spread, em `sombra-suave` (0.08) ou `sombra-media` (0.18). Sem sombra dura, sem contorno deslocado.

## Shapes

Cantos arredondados moderados: `raio` (12px) em botões, botão de menu e marca; `raio-grande` (22px) em cartões de projeto, citação e foto; 14px no selo do cargo; 16px nas bolhas do chat (canto inferior do lado do falante em 5px) e 20px na janela; pílula (999px) em tags, chips, selo "Atual", campo e botão do chat. A foto é um retângulo 4:5 com borda `linha`. Bordas são sempre de 1px em `linha` ou `linha-forte`; a única exceção é a linha do tempo (2px) e o filete de acento de 3px sobre cada especialidade. Ícones de interface são desenhados em traço único (24x24, traço 1.9, pontas arredondadas, `currentColor`); logotipos de ferramentas nas tags são imagens WebP recoloridas no acento.

## Components

### Buttons
- **Shape:** cantos de 12px (`raio`), altura mínima 2.9rem (pequeno 2.4rem, grande 3.25rem), texto Onest 600.
- **Primary** (`botao-primario`): fundo `acento`, texto branco, sombra suave; hover para `acento-forte`. Usado em "Ver projetos".
- **Outline** (`botao-contorno`): fundo branco, borda `linha-forte`, hover com borda `tinta`. Usado em "Falar comigo" e no "Currículo" do menu (pequeno): é o tratamento discreto do currículo.
- **Sobre faixa escura:** `botao-claro` (fundo `texto-escuro`, texto `escuro`) para o WhatsApp e `botao-contorno-claro` (transparente, borda `linha-escuro`) para o currículo.
- **Estados:** `:active` desloca 1px; hover só em dispositivos com hover; foco é um contorno de 3px em `acento` com 3px de afastamento (`acento-no-escuro` na faixa escura).
- **Link com seta** (`link-seta`): texto `acento` 600, sem sublinhado; hover escurece e sublinha.

### Cards / Containers
- **Cartão de projeto:** fundo branco, borda `linha`, canto 22px, imagem 16:10 no topo com filete embaixo, corpo com padding 1.4rem 1.5rem 1.5rem, título, tags, descrição e link com seta empurrado para o fim. Sombra de repouso mínima; sem elevação no hover. Todos os cartões têm o mesmo tamanho e peso; o projeto mais recente vai primeiro, sem variante de destaque.
- **Especialidade:** sem caixa; filete superior de `linha-forte` com um traço de acento de 2.75rem por 3px.
- **Citação:** cartão branco, canto 22px, texto de título em Bricolage 500.

### Chips e tags
- **Tag** (projetos e especialidades): pílula branca com borda `linha`, texto `tinta-suave` 0.8125rem e logotipo de 14px à esquerda.
- **Chip** (habilidades técnicas): pílula branca com borda `linha`, texto `tinta` 0.95rem, sem logotipo.
- **Selo "Atual":** pílula `acento-suave` com texto `acento-forte`, ao lado do período.

### Navigation
Cabeçalho fixo (sticky) branco com filete inferior. Marca (favicon e "Lucas Costa", Bricolage 700) à esquerda. Em desktop, links horizontais em `tinta-suave` e o item da seção visível marcado com `aria-current` em `acento` (nenhum marcado na primeira tela). Abaixo de 64rem, botão de três barras de 2.75rem que vira X e abre um painel de largura total com itens de 3rem separados por filetes e o botão "Currículo" em largura total.

### Selo do cargo (assinatura)
Cartão branco de 14px com borda e sombra, sobre o canto inferior esquerdo da foto (sai 1.25rem para fora a partir de 48rem), mostrando cargo em negrito e empresa em `tinta-fraca`. Visível só a partir de 64rem; no celular o cargo vira a linha com marcador de acento sob a frase de posicionamento.

### Curva normal (assinatura)
SVG de 7.5rem de altura no pé da primeira tela, visível a partir de 48rem: área `acento-suave` e traço de `acento` a 40% de opacidade, com máscara que dissolve para baixo. Decorativo, `aria-hidden`.

### Linha do tempo
Filete vertical de 2px (`linha`) com marcos circulares de 12px; o marco atual é preenchido em `acento`. Os dois primeiros cargos mostram tópicos com marcador de 6px em `acento` a 70%; os demais ficam num `details` ("Ver atividades (n)").

### Chatbot "Puxa Saco"
Botão flutuante em pílula `acento` (só ícone no celular, ícone e texto a partir de 40rem). Janela branca de 20px de canto, cabeçalho com filete, área de mensagens em `fundo`, bolhas de 16px: bot branca com borda, usuário em `acento`. Campo em pílula com borda `tinta-fraca` e botão de envio circular. A janela entra com opacidade e `translateY(12px) scale(0.98)`, e `visibility` a remove do foco quando fechada.

## Do's and Don'ts

### Do:
- **Do** usar `acento` apenas para ação, estado atual e dados; o resto é neutro azulado.
- **Do** escrever toda cor por variável de `:root`; nada de hex solto nos componentes.
- **Do** separar com filetes de 1px (`linha`, `linha-forte`) antes de pensar em sombra.
- **Do** manter `escuro` restrito a "Vamos conversar" e ao rodapé, com `acento-no-escuro` para foco e hover ali.
- **Do** manter o currículo discreto: contorno no menu, contorno claro na faixa escura; o primário sólido é de "Ver projetos".
- **Do** usar títulos em Bricolage com tracking negativo e texto em Onest; alvos de toque com no mínimo 2.75rem.
- **Do** envolver animações de entrada em `prefers-reduced-motion: no-preference` e limitar hover a `(hover: hover)`.

### Don't:
- **Don't** usar emojis, ícones por glifo ou ícones de fonte; ícones de interface são SVG de traço único.
- **Don't** usar neon, degradês decorativos ou cartões idênticos com ícone no estilo "portfólio de dev".
- **Don't** usar sombras duras ou deslocadas sem blur.
- **Don't** introduzir um segundo acento nem tingir seções inteiras de `acento`.
- **Don't** apertar o tracking da Onest nem usar caixa alta com espaçamento largo como rótulo de seção.
- **Don't** repetir o tema ornamental e pesado da versão descartada (terracota, texturas, molduras grossas).

## Limitações conhecidas

- A foto da primeira tela (`lucas.webp`) tem 720 px de largura e fica mole em telas 2x.
- A frase da meta description ainda aguarda aprovação do Lucas.
