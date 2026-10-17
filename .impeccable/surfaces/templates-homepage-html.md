---
version: 1
slug: "templates-homepage-html"
primary_target: "templates/homepage.html"
related_targets: ["static/style.css","static/main.js"]
---

# Homepage do portfólio (Lucas Costa)

**Escopo:** `templates/homepage.html`, `static/style.css`, `static/main.js`, rota `/`. Redesign completo em código (code-led, sem comp: o ambiente não gera imagens). **Modo do visitante:** Experience, a obra lidera.

**Público e tarefa:** recrutadores e gestores (celular, via LinkedIn, olhar rápido) e colegas de dados. Ação principal: baixar o currículo. Prova real: 6 projetos, trajetória (Iguá, Cencosud, Hospital Primavera, TRE-SE), currículo atualizado, chatbot Puxa Saco.

**Restrições:** pt-BR; nenhum texto do Lucas é reescrito; conteúdo vem de `conteudo.py`; contraste WCAG AA; `prefers-reduced-motion`; páginas leves (imagens enxutas, sem JS pesado); conhecimento e API do chatbot não mudam.

**Direção escolhida pelo Lucas:** Torre de argila em rolos (catálogo `clay-ceramics-fracture-coiled-earth-tower`), adotada mesmo tendo sido marcada como recusada. Decisões do Lucas: terracota e umber como fundo de verdade (não creme); chatbot como o arco de entrada da torre; foto original a ser tratada para o portfólio.

**Momento de assinatura:** a fiada em andamento (Iguá, "atualmente") é a única em argila úmida escura; a torre pode ser "construída" fiada por fiada somente se o visitante pedir.

**Em aberto:** foto original (aguarda o arquivo do Lucas); hospedagem (muda o link dentro do PDF do currículo); sem recomendações do LinkedIn; a citação do H. G. Wells fica, em lugar a definir na construção.

## Direction contract

THESIS: A página é a própria torre vista em corte: fiadas de argila assentadas uma sobre a outra, cada bloco de conteúdo uma fiada, a carreira subindo da base (TRE, 2022) até a fiada em andamento (Iguá). Recusa o portfólio padrão: hero em duas colunas, cartões iguais e barras de habilidade.

OWN-WORLD: Terracota e umber ocupam faixas inteiras, em largura total; juntas de engobe claro separam as fiadas; um único anel de argila úmida escura marca o que está em andamento. Maiúsculas de serifa grossa e baixo contraste, como carimbo em tijolo, para títulos; serifa de leitura para o texto corrido, sobre faixas escuras ou claras, nunca claro sobre terracota média. Grão leve de argila, cantos de rolo arredondados, sombras com deslocamento e desfoque. Sem ícone decorativo.

STORY: Em segundos o visitante entende quem é Lucas Costa e suas três frentes (estatística e ML, BI, análise para decisão). Acredita pela trajetória em fiadas e pelos projetos que abrem mostrando método e resultado. Age: baixa o currículo; depois contata ou conversa com a Puxa Saco pelo arco da torre.

FIRST VIEWPORT: Desktop 1440x900: faixas terracota em largura total; à esquerda "LUCAS COSTA" em caixa alta grossa (até 6rem) numa fiada; abaixo, três fiadas com as frentes, cada linha com a largura da sua fiada; uma junta clara com "Baixar currículo (PDF)" como ação primária; à direita a foto recortada encaixada na torre e o arco de entrada do chat no flanco. Celular 390x844: nome, três fiadas e o botão do currículo cabem sem rolar.

FORM: Torre de argila em rolos (catálogo `clay-ceramics-fracture-coiled-earth-tower`), escolhida pelo Lucas entre os desafiantes; fora da minha lista própria de candidatos. seed:8dfea99e72645cc7

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
