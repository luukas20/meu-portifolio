---
version: 1
slug: "templates-homepage-html"
primary_target: "templates/homepage.html"
related_targets: ["static/style.css","static/main.js"]
---

# Homepage do portfólio (Lucas Costa), versão limpa

**Escopo:** `templates/homepage.html`, `static/style.css`, `static/main.js`, rota `/`. Refaz o visual por completo (a "Torre de argila" foi descartada pelo Lucas por ser pesada e pouco séria). Code-led, sem comp (o ambiente não gera imagens). **Modo do visitante:** Experience, o conteúdo real lidera.

**Público e tarefa:** recrutadores (inclusive juniores) e a alta gerência de empresas, em geral pelo celular via LinkedIn, olhando rápido; colegas de dados em segundo plano. Ações: ver os projetos e falar com o Lucas. O currículo é secundário: um botão discreto no menu e na seção de contato.

**Pedido do Lucas (vale como direção fixada):** layout limpo, jovem e atual; fontes atuais e jovens sem perder legibilidade e seriedade; muito profissional; leve; sem emojis; usar a foto atual (`Foto Perfil`); menos destaque para o botão de currículo.

**Restrições:** pt-BR; nenhum texto do Lucas reescrito (só os emojis saem); conteúdo vindo de `conteudo.py`; contraste WCAG AA; `prefers-reduced-motion`; leve; cores só por variáveis CSS em `:root`; chatbot e backend não mudam.

**Momento de assinatura:** a curva normal (distribuição) em traço fino atrás da primeira tela, a marca de quem é estatístico; e o selo do cargo atual na foto.

**Em aberto:** hospedagem (muda o link dentro do PDF do currículo); sem recomendações do LinkedIn.

## Direction contract

THESIS: Um portfólio executivo e jovem: claro, limpo e arejado, em que o conteúdo real (nome, três frentes, trajetória, projetos com resultado) lidera e a interface recua. Recusa o visual temático e ornamental (a torre de argila saiu) e o "portfólio de dev" genérico: neon, degradês, cartões idênticos com ícone.

OWN-WORLD: Fundo claro neutro e frio, superfícies brancas, tinta azul-grafite e um único acento verde-azulado (teal) para ação, estado atual e dados. Títulos em Bricolage Grotesque (600 a 700, tracking apertado), texto em Onest. Filetes de 1px, cantos de 12 a 16px (maiores na foto), sombras suaves com deslocamento e desfoque, uma faixa escura só no contato. A curva normal em traço fino é a assinatura estatística. Ícones desenhados em traço único; sem emoji.

STORY: Em segundos o visitante entende quem é Lucas Costa, o que faz (estatística e ML, BI, análise para decisão) e onde trabalha hoje. Confia pela trajetória e pelos projetos com resultado. Age: ver projetos ou falar com ele; o currículo está à mão, sem disputar atenção.

FIRST VIEWPORT: Desktop 1440x900: cabeçalho com o nome, o menu e o botão "Currículo" em contorno; duas colunas. À esquerda: o nome (até 4.75rem), a frase de posicionamento, as três frentes em linhas separadas por filetes e dois botões ("Ver projetos" sólido, "Falar comigo" em contorno). À direita: a foto em retângulo arredondado com um selo "Analista de Transformação Sr., Iguá Saneamento" sobre o canto, e a curva normal sutil ao fundo. Celular 390x844: nome, posicionamento, frentes e botões; a foto vem logo abaixo.

FORM: Direção fixada pelo Lucas (limpa, jovem e profissional), executada como o padrão da categoria em fidelidade total, com tipografia atual e uma assinatura estatística; fora da minha lista própria de candidatos. seed:8dfea99e72645cc7

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
