# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Principal:** recrutadores (inclusive juniores) e a alta gerência de empresas, avaliando a contratação do Lucas (dados, BI, análise). Chegam por LinkedIn, currículo ou indicação, olham rápido e decidem se entram em contato.
- **Secundário:** colegas e comunidade de dados. Querem ver o método, o código e os estudos por trás de cada projeto.

## Product Purpose

Portfólio pessoal de **Lucas Costa**, Estatístico (UFS, 2019/2024), hoje Analista de Transformação Sr. na Iguá Saneamento. Mostra projetos e trajetória em Machine Learning, BI e análise para decisão. Sucesso = o visitante entra em contato (WhatsApp, LinkedIn, e-mail), baixa o currículo ou tira dúvidas no chatbot "Puxa Saco".

## Positioning

Três frentes, nas palavras do Lucas (no site, em out/2026, ganharam frases de impacto escritas com os fatos do currículo e dos projetos dele, mais as ferramentas em etiquetas):

1. **Estatística e Machine Learning:** desenvolve bons modelos de Machine Learning.
2. **BI:** forte conhecimento em ferramentas de BI (Power BI, SQL, Pentaho).
3. **Análise para decisão:** muita experiência em análise de dados para decisão rápida e precisa, trabalhando com Python, R e ferramentas de IA como o Claude.

Diferencial do site: um assistente de IA ("Puxa Saco") que responde sobre o perfil dele, com personalidade. Risco de crédito (PD, LGD, EAD, CMN 4966/21) é experiência de domínio da Cencosud e aparece em um projeto, mas **não** foi escolhido como a chamada principal.

## Operating Context

- Visitante vem de links (LinkedIn, currículo, GitHub) e abre no celular ou no computador.
- Idioma: português do Brasil. Versão em inglês não é desejada por enquanto.
- Contato por WhatsApp, LinkedIn e e-mail. Os projetos apontam para fora (Power BI público, Streamlit, GitHub).

## Capabilities and Constraints

- Site de página única em Flask (Jinja, CSS e JS próprios, sem build). Conteúdo da página em `conteudo.py`; conhecimento do chatbot em `prompts/conhecimento.md`.
- Chatbot via API do Gemini, sem histórico entre mensagens, com limite de uso por IP.
- Todo texto profissional é do Lucas: nada é reescrito sem aprovação.
- **Decisões em aberto:**
  - Hospedagem (hoje no Render gratuito, que "dorme" e demora no primeiro acesso; aberto a trocar).
  - Destino dos cards "Perda Esperada" e "Controle de Gastos" (hoje sem link).
  - Quando a hospedagem mudar, atualizar o link do site dentro do PDF do currículo (hoje aponta para o endereço no Render).
- **Decididas pelo Lucas:** rodapé com o nome completo ("Lucas da Silva Costa"); manter a citação do H. G. Wells; renomear "portifolio" para "portfólio" (feito); sem domínio próprio por enquanto (usa o endereço da hospedagem).

## Brand Commitments

- Nome: Lucas Costa.
- O assistente se chama **Puxa Saco** e tem voz amigável, engraçada, um pouco bajuladora, porém profissional e precisa. Só afirma o que está na base de conhecimento.
- Pedido do Lucas para o visual (out/2026): limpo, jovem e atual, com fontes atuais e legíveis, **muito profissional e leve**, para servir tanto a recrutadores juniores quanto à alta gerência; **sem emojis**; usar a foto atual (`Foto Perfil`); o botão de currículo com **pouco destaque** (um botão no menu e outro na seção "Vamos conversar").
- Uma tentativa anterior ("Torre de argila", terracota e umber) foi descartada por ser pesada e pouco séria; fica só no histórico do git.

## Evidence on Hand

- Seis projetos publicados (imagens em `static/images/`, descrições em `conteudo.py`): Perda Esperada, Visão Computacional (Gatos vs. Cachorros), Faturamento vs Meta, Previsão BOVA11, Controle de Gastos Pessoais, Previsão Ações Streamlit.
- **Pode mostrar métricas da Cencosud**, como o Índice de Cobertura de 115% do projeto de Perda Esperada.
- Cat vs Dog: repositório público em `github.com/luukas20/cnn-cat-vs-dog` (notebooks lidos; conclusões aguardam confirmação do Lucas antes de irem para o site ou o chatbot).
- Experiência: Iguá Saneamento, Cencosud, Hospital Primavera, TRE-SE. Formação e cursos em `prompts/conhecimento.md`.
- **Tem recomendações no LinkedIn**, mas o LinkedIn bloqueia leitura automatizada e os textos não foram fornecidos. Sem recomendações no site até o Lucas colar os textos: não inventar nem parafrasear depoimentos.
- Currículo em PDF baixável no site (`static/docs/`), na versão atualizada em out/2026: Iguá como emprego atual, subtítulo "Analista de Dados". O Word de origem fica no computador do Lucas, fora do repositório. O PDF tem e-mail e telefone, sem CPF ou endereço.
- **Ausências que não podem ser inventadas:** textos das recomendações, link de destino dos cards sem link.

## Product Principles

1. **Prova antes de promessa:** projetos reais, métricas autorizadas e recomendações com as palavras de quem as escreveu.
2. **As três frentes ditas com clareza** logo no começo: estatística/ML, BI e análise para decisão.
3. **Caminho curto até os projetos e o contato** para quem só passa o olho; o currículo está à mão, sem disputar atenção.
4. **Profundidade para quem quer ver o método:** cada projeto leva ao código, ao painel ou ao estudo, quando existir.
5. **O chatbot é parte do produto:** tem personalidade, só diz o que está na base e a base acompanha a página.

## Accessibility & Inclusion

Sem requisito específico informado pelo Lucas. Proposta para confirmar: contraste mínimo WCAG 2.2 AA, uso completo pelo teclado e respeito a `prefers-reduced-motion`.
