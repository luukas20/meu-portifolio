# CLAUDE.md

Portfólio pessoal de **Lucas Costa** (Estatístico; Ciência de Dados, BI e Risco de Crédito). Site de página única em Flask + HTML/CSS/JS puros (visual limpo, claro e moderno; ver `DESIGN.md`), com um chatbot ("Puxa Saco") que responde sobre o Lucas usando a API do Gemini.
Repositório: `github.com/luukas20/meu-portifolio` (branch `main`). Todo o conteúdo, UI e commits são em **pt-BR**.

## Stack

- Python 3.12, Flask 3.1, `google-genai` (modelo padrão `gemini-3.8-flash` com reserva `gemini-3.5-flash-lite`; trocáveis por `GEMINI_MODEL` e `GEMINI_MODEL_RESERVA`), `Flask-Limiter`, `python-dotenv`, `gunicorn` (produção)
- Front: templates Jinja2, `public/static/style.css` (CSS puro), `public/static/main.js` (JS vanilla). **Sem CDN nem script de terceiros**: fontes hospedadas em `public/static/fonts/` (Bricolage Grotesque para títulos, Onest para texto) e a fórmula da Perda Esperada em MathML nativo
- Sem banco de dados, sem build/bundler, sem CI/CD no repositório. Testes em `tests/` (pytest): chatbot e conteúdo/estrutura da página

## Comandos (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt   # requirements.txt = produção; requirements-dev.txt = + pytest e Pillow
python tools/otimizar_imagens.py     # gera os WebP leves em public/static/images/ a partir de imagens-originais/

flask --app main run --debug     # dev em http://127.0.0.1:5000 (python main.py também funciona)
gunicorn main:app                # produção
pytest                           # testes (Gemini simulado, não gasta cota)
```

- Variáveis de ambiente em `.env` (gitignorado): `GEMINI_API_KEY` e, opcionalmente, `GEMINI_MODEL` / `GEMINI_MODEL_RESERVA`. **Nunca ler, imprimir ou commitar o conteúdo do `.env`.**
- Não há linter: para o resto, validar mudanças subindo o servidor e conferindo no navegador (desktop e celular). O servidor sem `--debug` **não recarrega templates** (só o CSS/JS estáticos): reinicie ao mexer em `templates/`. Capturas sem navegador aberto: Chrome `--headless=new --screenshot` (a janela headless não desce de ~500 px; para celular use um iframe de 390 px).
- Modelos do Gemini saem do ar com frequência (`gemini-2.0-flash` e `2.5-flash` retornam 404 para esta chave). Antes de trocar o padrão, conferir a [página de depreciações](https://ai.google.dev/gemini-api/docs/deprecations) e testar com uma chamada real. Na chave gratuita (out/2026) o `3.8-flash` aceita só **20 requisições por dia** (429 com "free_tier_requests"; a cota volta em horas) e responde em 4 a 23 s; o `flash-lite` respondeu em 2 a 4 s sem bater em limite. Com a chave gratuita o modelo de reserva acaba atendendo quase tudo: para um site público, ativar o faturamento no AI Studio ou definir `GEMINI_MODEL` com o `flash-lite` (sem mexer no código). Se o principal falhar com 402/404/429/500/503, o back-end tenta o modelo de reserva.
- Node.js LTS (24.x) instalado via winget só para rodar ferramentas `npx` (skills); o app em si não usa Node. Em terminais já abertos o PATH só atualiza após reiniciar.
- **Hospedagem**: produção na **Vercel (Hobby)** em `https://lucas-costa-estatistico.vercel.app` (projeto `lucas-costa-estatistico`, time `lucas-9b0f`, função Python em São Paulo/`gru1`). O Render (plano gratuito que "dorme") segue no ar até o Lucas trocar os links e desligar. Publicar: `vercel deploy --prod` na raiz (CLI instalado com `npm i -g vercel`, login do Lucas; a pasta é ligada ao projeto por `.vercel/`, gitignorado). A integração com o GitHub **não** está conectada (o app da Vercel precisa ser instalado na conta do Lucas e depois `vercel git connect`): enquanto isso, o `git push` não publica. `vercel.json` (região, duração, arquivos excluídos) e `.python-version` só importam para a Vercel (entrada `main.py`, instância `app`; dependências de `requirements.txt`, que precisa ser UTF-8). O CLI **envia o `.env` junto com o código** apesar do `.gitignore`; por isso existe o `.vercelignore` (exclui `.env*`, `.venv`, originais, testes). Conferir sempre que mexer nele: `vercel api /v6/deployments/<id>/files` lista o que subiu (no Git Bash use `MSYS_NO_PATHCONV=1`). `GEMINI_API_KEY` está como Secret em Production e Preview (e, se quiser, `GEMINI_MODEL`); trocar com `vercel env rm`/`add` ou no painel. Nomes `*.vercel.app` são globais: `lucas-costa-portfolio` já era de outra pessoa. Deploy e troca de links são ações externas: pedir confirmação ao Lucas.

## Arquitetura

```
main.py                  cria `app = Flask(__name__, static_folder="public/static", ...)` e faz `from views import *` no final
vercel.json, .python-version  configuração da Vercel (duração máxima da função, arquivos excluídos do pacote, Python 3.12)
views.py                 rotas, cliente Gemini (criado sob demanda), limite de uso e leitura dos prompts
conteudo.py              conteúdo da homepage (frentes, trajetória, projetos, especialidades, ferramentas, sobre-mim, redes, currículo); o template só percorre estas listas
templates/macros.html    macros `tags` (etiquetas com logotipo) e `icone` (ícones SVG em traço único)
PRODUCT.md, DESIGN.md    contexto de produto e sistema visual (Impeccable); `.impeccable/design.json` e `.impeccable/surfaces/` são o apoio
imagens-originais/       imagens de origem (PNG/JPEG pesados), fora da pasta servida; o site usa só os WebP gerados
prompts/persona.md       persona e regras da "Puxa Saco" (instrução do sistema)
prompts/conhecimento.md  base de conhecimento do bot (currículo, projetos); editar o .md e reiniciar o servidor
templates/homepage.html  página única: abertura (primeira tela), trajetória, portfólio, especialidades, sobre, contato, rodapé, chat
public/static/style.css  todo o CSS; tokens em :root; mobile-first com breakpoints em 40rem, 48rem e 64rem
public/static/main.js   menu, seção atual no menu, chatbot (fetch POST /api/chat)
public/static/fonts/   Bricolage Grotesque e Onest (woff2, licença OFL em LICENSE.txt)
public/static/images/   WebP gerados por tools/otimizar_imagens.py (projetos/, icones/, lucas.webp); cada um com .json de proveniência
tools/otimizar_imagens.py  converte os originais em WebP leves (e recolore os ícones no verde-azulado do acento)
tests/                   test_chat.py (endpoint do chat) e test_conteudo.py (conteúdo, imagens, fontes, acessibilidade básica)
```

- **Rotas** (`views.py`): `GET /` (endpoint `pagina_home`, renderiza `homepage.html`) e `POST /api/chat`.
- **Import circular** `main` ↔ `views`: `views.py` faz `from main import app`. Funciona, mas é frágil; manter `from views import *` no **fim** do `main.py` e não adicionar imports de `views` antes de `app` existir.
- **Chatbot**: o front envia `{message}` para `/api/chat`; o back valida (texto, até 500 caracteres, senão 400), limita a 10 mensagens/min e 100/dia por IP (429), e chama `client.models.generate_content` com persona + conhecimento (`prompts/*.md`) em `system_instruction` e a mensagem do usuário só em `contents`. Devolve `{reply}` ou `{error}` (500 se o Gemini falhar). É stateless (sem histórico entre mensagens). `prompts/conhecimento.md` é a **única fonte de conhecimento** do bot.
- **Tema**: fundo claro e frio, superfícies brancas, tinta azul-grafite e **um único acento verde-azulado** (`--acento`) para ação, estado atual e dados; faixa escura só em "Vamos conversar" e no rodapé. Títulos em Bricolage Grotesque, texto em Onest. Assinatura: a curva normal discreta atrás da foto na primeira tela. O currículo é discreto de propósito: um botão no menu e outro em "Vamos conversar", nada na primeira tela. Cores só por variáveis de `:root`; regras completas em `DESIGN.md`.

## Convenções do código

- Nomes em português: classes CSS (`.abertura`, `.marco`, `.projeto`, `.chips`), ids, endpoint (`pagina_home`), comentários e mensagens de commit curtas ("Adicionando o Projeto da Perda Esperada").
- Grafia **"portfolio"** (sem acento) em classes, ids e âncoras (`.portfolio`, `#portfolio`) e **"portfólio"** no texto visível e no `<title>`. Foi renomeado de "portifolio" em out/2026; um teste confere que não sobrou nenhuma ocorrência. O repositório (`meu-portifolio`) e a pasta local mantêm a grafia antiga de propósito.
- Indentação de 4 espaços. CSS organizado em blocos com cabeçalho em comentário MAIÚSCULO (`/* ESTILO DO CABEÇALHO */`); HTML fecha blocos grandes com comentário (`</section><!--trajetoria-->`).
- Arquivos estáticos ficam em `public/static/` (a Vercel só serve estáticos de `public/`; o endereço público continua `/static/...`). Imagens sempre via `{{ url_for('static', filename='images/...') }}` e sempre os WebP gerados (nunca os originais); cores sempre via variáveis CSS (nada de hex solto fora de `:root`).
- Movimento: só a entrada suave ("surgir") da primeira tela; tudo desligado em `prefers-reduced-motion`. Hover só dentro de `@media (hover: hover)`.
- Sem kicker/rótulo acima de título, sem cartões iguais de ícone + título + texto, **sem emojis** (o Lucas pediu para tirá-los; a persona do bot também manda não usar). Ícones sempre pela macro `icone`.
- `appendMessage` em `main.js` usa `textContent` de propósito (evita injeção de HTML vinda do modelo). Manter assim.

## Manutenção do conteúdo (sincronização manual)

O conteúdo da página vive em `conteudo.py`; o do chatbot, em `prompts/conhecimento.md` (editado à mão). Os dois precisam andar juntos:

- **Novo projeto / cargo / habilidade**: atualizar (1) `conteudo.py` (o card aparece sozinho), (2) `prompts/conhecimento.md` (senão o chatbot responde que "não tem essa informação") e (3) `SOBRE_MIM` em `conteudo.py`, se o texto mudar.
- **Novo projeto na página**: copiar um item de `PROJETOS` em `conteudo.py` (`titulo`, `tags` com `tag("icones/x.webp", nome)`, `imagem` em `projetos/x.webp`, `link`, `descricao` em HTML, `chave_bot`). Para gerar o WebP: colocar o original em `imagens-originais/`, incluí-lo no mapa de `tools/otimizar_imagens.py` e rodar o script; depois registrar a origem (`impeccable embed-prompt`, que cria o `.json` ao lado).
- **Novo cargo**: item em `TRAJETORIA` (do mais recente para o mais antigo; `atual: True` só no cargo em andamento).
- Links de redes sociais (LinkedIn, GitHub, e-mail) ficam em `REDES` e aparecem sozinhos no sobre-mim e no contato.
- **Currículo**: o PDF baixável é `public/static/docs/Curriculo-Lucas-Costa.pdf` (configurado em `CURRICULO`, `conteudo.py`). O Word de origem fica **fora** do repositório (pasta `Documents\Curriculo` do Lucas); para atualizar, editar o Word, exportar o PDF e trocar o arquivo, mantendo o nome. O PDF tem link para a URL do site (hoje `lucas-costa-estatistico.vercel.app`): se o endereço mudar, atualizar o currículo também. Troca só do link sem abrir o Word: editar o destino em `word/_rels/document.xml.rels` do .docx e, no PDF, o `/URI` da anotação (pypdf), pois a automação do Word por COM travou nesta máquina.
- **Persona do bot** (`prompts/persona.md`): tom sóbrio (um elogio curto e baseado em fato por resposta, sem superlativos), respostas de 2 a 5 frases em texto simples (o front mostra Markdown cru), fidelidade aos dados (não liga ferramenta a empresa sem os dados ligarem; curso não é certificação), recusa assunto fora do Lucas e tentativas de revelar instruções, não promete nada em nome dele. Ao mexer, rodar uma bateria de perguntas reais (inclui injeção de prompt, idioma e dados ausentes) e ler as respostas.
- `pytest` confere se as imagens citadas existem, se a home renderiza todo o conteúdo e se cada projeto tem sua `chave_bot` em `prompts/conhecimento.md` (projeto novo na página sem entrar no conhecimento do bot faz o teste falhar).
- Texto profissional, persona e dados pessoais são conteúdo do Lucas: perguntar antes de reescrever ou "melhorar" o texto.

## Armadilhas conhecidas (revisar/remover conforme forem corrigidas)

- A foto (`public/static/images/lucas.webp`) vem de um original de 720 px de largura: fica um pouco mole em telas 2x. Se o Lucas tiver uma foto de 1000 px ou mais, trocar em `imagens-originais/` e rodar `tools/otimizar_imagens.py`.
- A frase da meta description e da prévia de compartilhamento (`og.jpg`, feita a partir dos títulos das frentes) foi composta fora dos textos do Lucas e aguarda a aprovação dele. Para refazer a prévia, ver o HTML de origem no histórico do git ou recriar com Chrome `--screenshot` a 1200x630.
- O raciocínio (thinking) do Gemini conta no `max_output_tokens`: sem teto a resposta saía cortada no meio. Por isso `views.py` usa `ORCAMENTO_RACIOCINIO = 256` e `LIMITE_TOKENS_RESPOSTA = 2048` (o `flash-lite` não aceita `thinking_budget=0` e às vezes pensa além do orçamento; resposta vazia é refeita uma vez). A data de hoje vai na instrução do sistema para o bot calcular tempo de experiência.
- O limite de uso do chat é em memória e vale por instância do servidor (em hospedagem serverless é "melhor esforço"). Atrás de proxy usa `ProxyFix(x_for=1, x_proto=1, x_host=1)` em `main.py` (IP, https e host reais; a prévia de compartilhamento monta endereços absolutos a partir deles); sem proxy, os cabeçalhos `X-Forwarded-*` podem ser forjados (burla o limite do chat e muda os endereços da prévia).

## Skills

- `.claude/skills/<nome>/SKILL.md` guarda as skills baixadas do GitHub. A pasta `.claude/` inteira está no `.gitignore`: em outra máquina, recriar com os comandos abaixo (ou `npx skills experimental_install`, que restaura as do Emil a partir do `skills-lock.json`).
- Instaladas de `emilkowalski/skills` (commit `2d22863`, licença MIT em `.claude/skills/LICENSE-emilkowalski-skills`). Instaladas com `npx skills@latest add emilkowalski/skills --skill '*' --agent claude-code --copy -y` (`--copy` porque link simbólico no Windows exige administrador e este repo tem `core.symlinks=false`). Versões registradas em `skills-lock.json`; para atualizar: `npx skills@latest update`.
- Relevantes para este site: `emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance`, `animation-vocabulary`, `apple-design`, `mobile-native`, `break-ui`, `prototype`. Não se aplicam (projeto sem React/Swift/Expo): `animate-expo`, `write-swift`, `ask-sonner`.
- `impeccable` (design de interfaces: `shape`, `critique`, `audit`, `polish`, `animate`, `layout`, `typeset` etc.), de `pbakaus/impeccable`. Instalada com `npx impeccable install --providers=claude --project --no-hooks --force -y` (cópia em `.claude/skills/impeccable` + subagentes em `.claude/agents/`; o `npx impeccable link` não serve aqui porque cria link simbólico). Para atualizar: `npx impeccable update`. O submódulo `.impeccable/` do setup inicial foi removido do repositório (não era usado pela instalação atual).
- Hooks do Impeccable **não** foram instalados (`--no-hooks`; não existe `.claude/settings.json`). O binário do motor (`impeccable.exe`, ~19 MB) fica em `.claude/skills/impeccable/scripts/bin/windows-x64/`. A telemetria anônima do Impeccable está ligada (`npx impeccable telemetry off` desliga).
