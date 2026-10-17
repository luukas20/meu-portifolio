---
name: Lucas Costa | Portfólio de Dados
description: Uma torre de argila em rolos vista em corte, onde cada bloco de conteúdo é uma fiada assentada sobre a outra.
colors:
  engobe: "#ece5da"
  engobe-sombra: "#d9cfbf"
  seca: "#bda98a"
  argila-crua: "#d78c5b"
  terracota: "#c65a3a"
  terracota-queimada: "#8f3f22"
  umber: "#7a4e34"
  argila-umida: "#3e2e28"
  argila-escura: "#2a1d18"
typography:
  display:
    fontFamily: "Holtwood One SC, Rockwell, Rockwell Extra Bold, serif"
    fontSize: "clamp(2.5rem, min(11vw, 12vh), 5.25rem)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Holtwood One SC, Rockwell, Rockwell Extra Bold, serif"
    fontSize: "clamp(1.9rem, 6vw, 3.25rem)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "normal"
  title:
    fontFamily: "Holtwood One SC, Rockwell, Rockwell Extra Bold, serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.03em"
  body:
    fontFamily: "Zilla Slab, Rockwell, Georgia, serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "Zilla Slab, Rockwell, Georgia, serif"
    fontSize: "0.85rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "normal"
rounded:
  rolo: "1.75rem"
  rolo-grande: "2rem"
  rolo-nome: "2.5rem"
  tijolo: "0.6rem"
  tag: "0.5rem"
  pilula: "999px"
spacing:
  fiada-gap: "0.5rem"
  faixa-x: "1.25rem"
  faixa-y: "clamp(3rem, 8vw, 6rem)"
  fiada-x: "1.75rem"
  largura-site: "76rem"
components:
  fiada-frente:
    backgroundColor: "{colors.terracota-queimada}"
    textColor: "{colors.engobe}"
    rounded: "{rounded.rolo}"
    padding: "0.75rem 1.25rem 0.85rem"
  fiada-nome:
    backgroundColor: "{colors.terracota}"
    textColor: "{colors.argila-escura}"
    typography: "{typography.display}"
    rounded: "{rounded.rolo-nome}"
    padding: "0.85rem 1.25rem 0.75rem"
  fiada-cargo:
    backgroundColor: "{colors.argila-umida}"
    textColor: "{colors.engobe}"
    rounded: "{rounded.rolo}"
  fiada-cargo-em-andamento:
    backgroundColor: "{colors.argila-escura}"
    textColor: "{colors.engobe}"
  fiada-cargo-base:
    backgroundColor: "{colors.seca}"
    textColor: "{colors.argila-escura}"
  fiada-projeto:
    backgroundColor: "{colors.terracota-queimada}"
    textColor: "{colors.engobe}"
    rounded: "{rounded.rolo-grande}"
    padding: "1.15rem 3.5rem 1.15rem 1.75rem"
  botao:
    backgroundColor: "{colors.terracota-queimada}"
    textColor: "{colors.engobe}"
    typography: "{typography.title}"
    rounded: "{rounded.pilula}"
    padding: "0.6rem 1.4rem"
    height: "2.9rem"
  botao-claro:
    backgroundColor: "{colors.engobe}"
    textColor: "{colors.argila-escura}"
    rounded: "{rounded.pilula}"
  junta-curriculo:
    backgroundColor: "{colors.engobe}"
    textColor: "{colors.argila-escura}"
    rounded: "{rounded.pilula}"
    padding: "0.7rem 1.25rem"
    height: "3.4rem"
  tag:
    backgroundColor: "{colors.argila-escura}"
    textColor: "{colors.engobe}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "0.2rem 0.65rem 0.2rem 0.45rem"
  tijolo:
    backgroundColor: "{colors.umber}"
    textColor: "{colors.engobe}"
    rounded: "{rounded.tijolo}"
    padding: "0.4rem 1rem"
  selo:
    backgroundColor: "{colors.argila-crua}"
    textColor: "{colors.argila-escura}"
    typography: "{typography.label}"
    rounded: "{rounded.pilula}"
    padding: "0.1rem 0.7rem"
  arco-botao:
    backgroundColor: "{colors.argila-escura}"
    textColor: "{colors.engobe}"
    width: "7.25rem"
    height: "8.5rem"
  chat-container:
    backgroundColor: "{colors.argila-escura}"
    textColor: "{colors.engobe}"
    width: "24rem"
  bot-message:
    backgroundColor: "{colors.engobe}"
    textColor: "{colors.argila-escura}"
    rounded: "1.1rem"
    padding: "0.65rem 1rem"
  user-message:
    backgroundColor: "{colors.terracota-queimada}"
    textColor: "{colors.engobe}"
    rounded: "1.1rem"
    padding: "0.65rem 1rem"
---

# Design System: Lucas Costa | Portfólio de Dados

## Overview

**Creative North Star: "A Torre de Argila em Rolos"**

A página é a torre vista em corte. Cada bloco de conteúdo é uma fiada de argila, um rolo assentado sobre o outro, e a carreira sobe da base (a formação, o TRE) até a fiada em andamento (Iguá). A cor não é verniz sobre uma página clara: terracota, umber e argila úmida ocupam faixas inteiras, em largura total, e o creme (engobe) aparece só como junta entre elas, como superfície de leitura clara e como texto. O mundo é quente, terroso, tátil e confiante, mais olaria que escritório.

A densidade é média e honesta. Há pouca coisa por tela, mas cada fiada é grande, de cantos arredondados, com grão de argila e um gradiente vertical (luz em cima, sombra embaixo) que dá volume de rolo. A hierarquia vem de largura e de cor da fiada, não de ícones ou ornamentos. Os títulos usam uma serifa grossa de caixa alta com falhas de tinta, como carimbo em tijolo; o texto corrido usa uma serifa de leitura calma.

O que o sistema recusa, por decisão do Lucas: o portfólio padrão (hero em duas colunas simétricas, cartões iguais em grade, barras de habilidade) e o fundo creme com acento terracota. A terra é o fundo.

**Key Characteristics:**
- Fiadas de argila como único módulo estrutural: faixas de largura total e blocos arredondados que afunilam para cima.
- Juntas de engobe (8px, com grão e marcas de polegar) separando as faixas.
- Uma única fiada em argila úmida escura com anel claro marca o que está em andamento.
- Volume por gradiente vertical e sombra com desfoque, nunca por contorno duro.
- Sem ícone decorativo; os únicos desenhos são o arco da torre (entrada do chat), a seta do currículo e os traços de abrir/fechar.
- Movimento só de assentar: as fiadas caem e se encaixam.

## Colors

Uma paleta de argila, da mais clara à mais escura, sem nenhum azul, verde ou cinza neutro frio. Todo valor nasce em `:root`.

### Primary
- **Terracota Queimada** (`terracota-queimada`, #8f3f22): a cor-base das fiadas e das faixas de trajetória e sobre; botões padrão, balão do usuário, filete do cabeçalho e do chat. Texto engobe sobre ela passa com folga.
- **Terracota** (`terracota`, #c65a3a): a cor viva. Aparece no bloco do nome, na seta/arco sobre fundo escuro e na cor do ícone do arco. Como é média, só leva texto escuro e só em tamanho de display.

### Secondary
- **Umber** (`umber`, #7a4e34): segunda cor de fundo: faixa de especialidades e contato, fiadas pares, tijolos de habilidade, bordas finas.
- **Argila Crua** (`argila-crua`, #d78c5b): o único realce pequeno: foco, seleção, marcadores de lista, sublinhado do link ativo, selo "em andamento", anel da fiada atual, cursor.

### Neutral
- **Engobe** (`engobe`, #ece5da): o creme de argila. Texto sobre as faixas escuras, juntas entre faixas, botões claros, balão do bot.
- **Engobe Sombra** (`engobe-sombra`, #d9cfbf): texto secundário (períodos) sobre fundo escuro.
- **Seca** (`seca`, #bda98a): argila seca; a fiada-base (formação) e o texto do rodapé.
- **Argila Úmida** (`argila-umida`, #3e2e28): fundo de página e das fiadas de cargo ímpares.
- **Argila Escura** (`argila-escura`, #2a1d18): cabeçalho, rodapé, chat, tags, texto sobre engobe e sobre terracota. O mais próximo de preto, e ainda é marrom.

### Named Rules
**The Terra Como Fundo Rule.** Terracota e umber são fundo de faixa inteira, em largura total. Nunca são reduzidos a acento sobre uma página creme.

**The Texto Claro Só Sobre Escuro Rule.** Texto engobe vai sobre terracota-queimada, umber, argila-umida ou argila-escura. Texto escuro (argila-escura) vai sobre engobe, seca ou terracota. Nunca claro sobre terracota média.

**The Uma Fiada Úmida Rule.** Só a fiada em andamento usa argila-escura com anel de argila-crua e brilho de umidade. Esse tratamento não se repete em nenhuma outra.

**The Cor Sai do Token Rule.** Cores novas entram em `:root` antes de serem usadas. Os poucos `rgb()` dentro dos gradientes de volume são luz e sombra, não paleta.

## Typography

**Display Font:** Holtwood One SC (com Rockwell, Rockwell Extra Bold, serif), hospedada em `static/fonts`.
**Body Font:** Zilla Slab 400, 400 itálico e 700 (com Rockwell, Georgia, serif), hospedada em `static/fonts`.

**Character:** Uma serifa egípcia pesada de caixa alta, com baixo contraste, que lê como carimbo em tijolo, contra uma serifa de laje calma para a leitura. As duas têm o mesmo gesto de barra grossa; uma grita, a outra conversa.

### Hierarchy
- **Display** (Holtwood 400, `clamp(2.5rem, min(11vw, 12vh), 5.25rem)`, 0.98): só o nome na primeira fiada, em caixa alta, com máscara de falha de tinta (`--falha`). A altura da janela (12vh) limita o tamanho para a primeira tela caber.
- **Headline** (Holtwood 400, `clamp(1.9rem, 6vw, 3.25rem)`, 1.08): títulos de faixa (`.titulo`), com a mesma máscara de falha e `text-wrap: balance`.
- **Title** (Holtwood 400, 1.1rem a 1.2rem, 1.3, espaçamento 0.02 a 0.04em): empresa do cargo, título de projeto, nome de especialidade, rótulo dos botões, nome do chat.
- **Body** (Zilla Slab 400, 1.125rem, 1.6): texto corrido; descrições em 1.075rem, sobre em 1.2rem. Limites de linha: 52ch a 62ch.
- **Label** (Zilla Slab 700, 0.85rem a 1rem): tags, selo, nome do cargo, períodos, tijolos de habilidade, links de redes.

### Named Rules
**The Carimbo Só no Título Rule.** Holtwood é para nome, títulos de faixa, de fiada e de botão. Parágrafo, lista e mensagem de chat nunca saem em Holtwood.

**The Falha de Tinta Rule.** A máscara `--falha` é aplicada só ao nome e aos títulos de faixa (os maiores). Em corpo pequeno ela prejudicaria a leitura.

## Layout

O modelo espacial é vertical: faixas de largura total empilhadas, cada uma com um miolo centrado de no máximo 76rem (`largura-site`); faixas de texto (sobre, contato) caem para 46rem. Dentro do miolo, a unidade é a fiada, um bloco de largura variável, centralizada, empilhada com 0.5rem de intervalo (`fiada-gap`). A largura que muda é o desenho: no desktop as fiadas de cargo alargam de 78% (a atual, no topo) a 97% (a mais antiga), e a base da formação fecha em 100%; as três frentes da primeira tela vão de 100% a 88%, formando o perfil da torre.

Primeira tela: duas colunas no desktop (1.55fr de fiadas, 1fr de foto) a partir de 64rem; coluna única abaixo. Nome, tagline fina, três frentes e a junta do currículo cabem sem rolar em 390x844 e em 1440x900, com ajustes de padding para telas baixas (menos de 720px de altura no celular, menos de 820px no desktop). Faixas têm padding vertical `clamp(3rem, 8vw, 6rem)` e lateral de 1.25rem.

Há três degraus de resposta: base (celular), `min-width: 40rem` (resumos em grade de colunas, projeto em duas colunas, chat vira janela de 24rem) e `min-width: 64rem` (menu horizontal, duas colunas na primeira tela, cargos em três colunas). Abaixo de 26rem as frentes deixam de afunilar para ganhar largura de texto. Alvos de toque têm no mínimo 2.9rem de altura.

## Elevation & Depth

O sistema é híbrido: profundidade por camada tonal (cada fiada tem cor própria sobre o fundo `argila-umida`) mais volume de rolo por gradiente, e só então sombra. O volume vem de `--rolo`, uma luz clara no alto e sombra escura embaixo da própria fiada; as superfícies claras de engobe usam `--rolo-claro`, e as fiadas finas `--rolo-suave`. O grão (`--grao`, `--grao-leve`) cobre tudo que é argila.

As sombras são sempre deslocadas para baixo, longas e desfocadas, com raio negativo para não vazar nos lados. Não existe sombra dura nem contorno de caixa como profundidade.

### Shadow Vocabulary
- **Fiada** (`box-shadow: 0 14px 24px -14px var(--sombra)`): fiadas em repouso, com junta de engobe de 2px embaixo (`--junta`).
- **Botão** (`box-shadow: 0 8px 16px -8px var(--sombra)`): botões; no hover sobem 2px e a sombra vai a `0 14px 22px -8px`.
- **Retrato** (`box-shadow: 0 24px 36px -20px var(--sombra)`): a foto e a janela do chat (`0 24px 40px -16px`).
- **Arco** (`box-shadow: 0 16px 26px -12px var(--sombra)`): o arco e o botão flutuante do chat.

### Named Rules
**The Junta Rule.** Entre faixas, uma junta de engobe de 8px com grão e a emenda (`--emenda`, marcas de polegar a 115 graus); entre fiadas, 2px de `--junta`. Faixa sem junta de engobe no topo não existe.

**The Sombra Mole Rule.** Sombra sempre com deslocamento vertical e desfoque, raio negativo e cor `--sombra` (marrom translúcido). Nenhuma sombra preta, nenhuma sombra dura deslocada na diagonal.

## Shapes

Forma de rolo: cantos muito arredondados, nunca quadrados. Fiadas usam 1.75rem (`raio-rolo`), projetos 2rem, o bloco do nome 2.5rem, a fiada fina e os botões são pílulas (999px). Tags e tijolos são mais enxutos (0.5 e 0.6rem), como tijolos pequenos sobre os rolos.

A silhueta de assinatura é o arco: um semicírculo em cima e cantos de 1rem embaixo (`999px 999px 1rem 1rem`), usado na foto do retrato (com borda de 6px em terracota-queimada), no botão do chat na primeira tela e no botão flutuante. A janela do chat repete a ideia com `3rem 3rem 1.25rem 1.25rem`. Bordas são grossas (2px a 6px) e de argila, nunca finas e cinzas.

## Components

### Fiada (módulo base)
Um bloco de argila: cor por `--cor`, grão e rolo como fundo, cantos de `raio-rolo`, texto engobe e filete de junta embaixo. Todas as variações são o mesmo componente com outra cor e outra largura.
- **Nome:** terracota, texto argila-escura, display, cantos de 2.5rem.
- **Fina (tagline):** umber, itálico, pílula a 96% de largura.
- **Frente:** terracota-queimada / umber / terracota-queimada, a 100%, 96% e 92% no celular, e 100%, 94% e 88% a partir de 40rem.
- **Cargo:** argila-umida e umber alternadas; abre com `details`; indicador de mais/menos de 1.1rem desenhado em CSS, no canto direito. Em andamento: argila-escura com anel de 3px argila-crua e brilho de umidade; vem aberta. Base (formação): seca com texto escuro, sem abrir.
- **Projeto:** cantos de 2rem; terracota-queimada e umber alternadas; só um abre por vez (acordeão nomeado); corpo em duas colunas com captura de tela em 16/10 com borda de 3px em argila-escura.
- **Especialidade:** terracota-queimada e argila-umida alternadas; título à esquerda, descrição e tags à direita.
- **Hover (só com hover real):** o brilho (`--brilho`) acende sobre o resumo.

### Buttons
- **Shape:** pílula (999px), altura mínima de 2.9rem (3.4rem no grande).
- **Padrão:** terracota-queimada com grão e rolo, texto engobe em Holtwood 0.9rem, sombra de botão.
- **Claro:** engobe com grão leve e `--rolo-claro`, texto argila-escura. Usado para o currículo no cabeçalho, "Abrir o projeto" e ações secundárias.
- **Hover / Active:** sobe 2px no hover (só em dispositivos com hover); desce 1px ao pressionar. Transição de 0.2s com `--ease`.
- **Foco:** anel de 3px em argila-crua com 3px de distância, em todo elemento.

### Junta do currículo
A ação primária da página: uma pílula de engobe de 3.4rem, em largura total da coluna, com a seta de download (máscara SVG em `currentColor`) à esquerda do texto "Baixar currículo (PDF)" em Holtwood. Fecha a pilha de fiadas da primeira tela.

### Tags e tijolos
- **Tag:** 0.5rem de raio, fundo argila-escura, texto engobe em bold 0.85rem.
- **Tijolo (habilidade):** 0.6rem de raio, fundo umber com grão e rolo, bold 1rem, em linha com quebra.
- **Selo:** pílula de argila-crua com texto argila-escura; só em "em andamento".

### Navigation
Cabeçalho fixo em argila-escura com filete de 3px em terracota-queimada. Marca (favicon e nome em Holtwood 0.95rem) à esquerda, botão claro de currículo à direita. No celular, um botão de menu de 2.9rem com três barras que viram X abre uma lista de links com divisor de umber; no desktop (64rem), os links ficam em linha, bold. O link da seção atual é sublinhado em argila-crua (3px).

### Arco da torre (entrada do chat)
Assinatura do sistema: a porta da torre é o convite para a Puxa Saco. Na primeira tela é o botão de 7.25rem por 8.5rem encaixado no canto da foto, com rótulo "Pergunte à Puxa Saco"; depois que se rola, o mesmo arco aparece menor (3.9rem por 4.6rem) como botão flutuante no canto da tela. O desenho é um arco de terracota com linhas de engobe e porta de argila-escura, sobre fundo argila-escura e borda de 3px engobe. A janela do chat abre com translação curta e esmaecimento; mensagens do bot em engobe, do usuário em terracota-queimada, campo de texto em pílula engobe, envio redondo.

### Movimento
O único gesto é assentar: a fiada cai 22px com leve estreitamento e se encaixa (0.6s, `--ease`, atraso de 60ms por fiada). A torre pode ser reconstruída fiada por fiada somente se o visitante clicar no botão da trajetória (`--duracao` 0.7s, 130ms por fiada). Com `prefers-reduced-motion: reduce` tudo para e o botão de reconstruir some.

## Do's and Don'ts

### Do:
- **Do** usar terracota-queimada, umber, argila-umida e argila-escura como fundos de faixa e fiada em largura total, e engobe como junta, leitura clara e texto.
- **Do** dar a cada fiada seu grão (`--grao` ou `--grao-leve`) e seu gradiente de rolo (`--rolo`, `--rolo-claro` ou `--rolo-suave`) sobre a cor de base.
- **Do** variar a largura das fiadas (de 78% a 100%) para desenhar o perfil da torre; a fiada atual, no topo, é a mais estreita e a base da formação a mais larga.
- **Do** usar Holtwood One SC em caixa alta só para nome, títulos e rótulos de botão, e Zilla Slab para todo texto corrido, com 52ch a 62ch de linha.
- **Do** reservar argila-crua para o realce pequeno: foco, seleção, marcadores, selo e o anel da fiada em andamento.
- **Do** desenhar o arco (`999px 999px r r`) para tudo que é porta de entrada: a foto, o chat, a janela.
- **Do** declarar uma cor nova como token em `:root` antes de usá-la, e conferir contraste AA em cada par texto/fundo.

### Don't:
- **Don't** fazer o portfólio padrão: hero em duas colunas simétricas, cartões iguais em grade, barras de habilidade.
- **Don't** pôr texto engobe sobre terracota média (#c65a3a); nela só entra argila-escura, e só em tamanho de display.
- **Don't** reduzir terracota e umber a acento sobre fundo creme; a terra é o fundo.
- **Don't** repetir o tratamento de argila úmida com anel claro fora da fiada em andamento.
- **Don't** usar sombra dura, sombra preta pura ou contorno fino cinza como profundidade; só a sombra mole marrom e a borda grossa de argila.
- **Don't** pôr ícone decorativo, ilustração ou emoji de enfeite no layout; os únicos desenhos são o arco, a seta do currículo e os traços de abrir/fechar.
- **Don't** aplicar a máscara de falha de tinta a texto pequeno nem usar Holtwood em parágrafos.
- **Don't** animar nada além de assentar, sombra e elevação de hover; sem rolagem parallax, sem hover grudado no celular.
