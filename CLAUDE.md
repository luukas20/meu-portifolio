# CLAUDE.md

Portfólio pessoal de **Lucas Costa** (Estatístico; Ciência de Dados, BI e Risco de Crédito). Site de página única em Flask + HTML/CSS/JS puros, com um chatbot ("Puxa Saco") que responde sobre o Lucas usando a API do Gemini.
Repositório: `github.com/luukas20/meu-portifolio` (branch `main`). Todo o conteúdo, UI e commits são em **pt-BR**.

## Stack

- Python 3.12, Flask 3.1, `google-genai` (modelo padrão `gemini-3.8-flash` com reserva `gemini-3.5-flash-lite`; trocáveis por `GEMINI_MODEL` e `GEMINI_MODEL_RESERVA`), `Flask-Limiter`, `python-dotenv`, `gunicorn` (produção)
- Front: templates Jinja2, `static/style.css` (CSS puro), `static/main.js` (JS vanilla). CDNs: Google Fonts (Poppins), bootstrap-icons, MathJax (fórmula da Perda Esperada)
- Sem banco de dados, sem build/bundler, sem CI/CD no repositório. Testes só do chatbot (`tests/`, pytest)

## Comandos (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt   # requirements.txt = produção; requirements-dev.txt = + pytest

flask --app main run --debug     # dev em http://127.0.0.1:5000 (python main.py também funciona)
gunicorn main:app                # produção
pytest                           # testes do chatbot (Gemini simulado, não gasta cota)
```

- Variáveis de ambiente em `.env` (gitignorado): `GEMINI_API_KEY` e, opcionalmente, `GEMINI_MODEL` / `GEMINI_MODEL_RESERVA`. **Nunca ler, imprimir ou commitar o conteúdo do `.env`.**
- Não há linter: para o resto, validar mudanças subindo o servidor e conferindo no navegador (desktop e mobile ≤ 1020px).
- Modelos do Gemini saem do ar com frequência (`gemini-2.0-flash` e `2.5-flash` retornam 404 para esta chave). Antes de trocar o padrão, conferir a [página de depreciações](https://ai.google.dev/gemini-api/docs/deprecations) e testar com uma chamada real. Modelos maiores (`3.6`/`3.8-flash`) exigem créditos no AI Studio; o `flash-lite` funcionou sem eles. Se o principal falhar com 402/404/429/500/503, o back-end tenta o modelo de reserva.
- Node.js LTS (24.x) instalado via winget só para rodar ferramentas `npx` (skills); o app em si não usa Node. Em terminais já abertos o PATH só atualiza após reiniciar.
- O deploy não está descrito no repositório (não há Procfile/Dockerfile/render.yaml). Perguntar ao Lucas antes de assumir a plataforma.

## Arquitetura

```
main.py                  cria `app = Flask(__name__)` e faz `from views import *` no final
views.py                 rotas, cliente Gemini (criado sob demanda), limite de uso e leitura dos prompts
prompts/persona.md       persona e regras da "Puxa Saco" (instrução do sistema)
prompts/conhecimento.md  base de conhecimento do bot (currículo, projetos); editar o .md e reiniciar o servidor
templates/homepage.html  página única: topo, especialidades, sobre-mim, portifólio, contato, footer, widget do chat
static/style.css         todo o CSS; tema por variáveis em :root; um único breakpoint (max-width: 1020px)
static/main.js           menu mobile + chatbot (fetch POST /api/chat)
static/images/           PNGs/JPEG usados via url_for (nomes com espaço e acento)
tests/test_chat.py       testes do endpoint do chat (pytest, Gemini simulado)
```

- **Rotas** (`views.py`): `GET /` (endpoint `pagina_home`, renderiza `homepage.html`) e `POST /api/chat`.
- **Import circular** `main` ↔ `views`: `views.py` faz `from main import app`. Funciona, mas é frágil; manter `from views import *` no **fim** do `main.py` e não adicionar imports de `views` antes de `app` existir.
- **Chatbot**: o front envia `{message}` para `/api/chat`; o back valida (texto, até 500 caracteres, senão 400), limita a 10 mensagens/min e 100/dia por IP (429), e chama `client.models.generate_content` com persona + conhecimento (`prompts/*.md`) em `system_instruction` e a mensagem do usuário só em `contents`. Devolve `{reply}` ou `{error}` (500 se o Gemini falhar). É stateless (sem histórico entre mensagens). `prompts/conhecimento.md` é a **única fonte de conhecimento** do bot.
- **Tema**: cores só via variáveis (`--primary-*`, `--accent-*`, `--text-*`, `--bg-*`); fonte Poppins. Seção do portifólio = lista de `.project-card` dentro de `.project-container` (2 por linha no desktop, 1 no mobile).

## Convenções do código

- Nomes em português: classes CSS (`.sobre-mim`, `.especialidades-box`), ids, endpoint (`pagina_home`), comentários e mensagens de commit curtas ("Adicionando o Projeto da Perda Esperada").
- A grafia **"portifolio"** (sic) é usada de forma consistente em classes, ids e âncoras (`.portifolio`, `#portifolio`, `<title>`). Não corrigir só uma ocorrência; se for renomear, trocar tudo (HTML, CSS, links de navegação).
- Indentação de 4 espaços. CSS organizado em blocos com cabeçalho em comentário MAIÚSCULO (`/* ESTILO DO CABEÇALHO */`); HTML fecha divs com comentário (`</div><!--flex-->`).
- Imagens sempre via `{{ url_for('static', filename='images/...') }}`; cores sempre via variáveis CSS (nada de hex solto).
- `appendMessage` em `main.js` usa `textContent` de propósito (evita injeção de HTML vinda do modelo). Manter assim.

## Manutenção do conteúdo (sincronização manual)

Não existe fonte única de dados; o mesmo conteúdo vive em mais de um lugar:

- **Novo projeto / cargo / habilidade**: atualizar (1) o card em `homepage.html`, (2) `prompts/conhecimento.md` (senão o chatbot responde que "não tem essa informação") e (3) o texto de "Sobre mim", se mudar.
- **Novo card**: copiar um `.project-card` existente (header com título + `.project-tag` com ícone, `.card-image` com `background-image`, `.project-description`).
- Links de redes sociais (LinkedIn, GitHub, e-mail) aparecem duas vezes em `homepage.html` (sobre-mim e contato).
- Texto profissional, persona e dados pessoais são conteúdo do Lucas: perguntar antes de reescrever ou "melhorar" o texto.

## Armadilhas conhecidas (revisar/remover conforme forem corrigidas)

- `homepage.html` carrega `polyfill.io` (domínio comprometido em 2024); o MathJax v3 não precisa dele. Também carrega bootstrap-icons sem usar nenhum ícone.
- Imagens pesadas em `static/images/` (`Eu Hexagonal.png` 4,4 MB, `Perda Esperada.png` 4,4 MB, `Cat vs Dog.png` 3,9 MB), carregadas sem lazy-load.
- Cards "Perda Esperada" e "Controle de Gastos" têm `href="#"` (sem destino).
- O limite de uso do chat é em memória e vale por instância do servidor (em hospedagem serverless é "melhor esforço"). Atrás de proxy usa `ProxyFix(x_for=1)` em `main.py`; sem proxy, o cabeçalho `X-Forwarded-For` pode ser forjado e burlar o limite.

## Skills

- `.claude/skills/<nome>/SKILL.md` guarda as skills baixadas do GitHub. A pasta `.claude/` inteira está no `.gitignore`: em outra máquina, recriar com os comandos abaixo (ou `npx skills experimental_install`, que restaura as do Emil a partir do `skills-lock.json`).
- Instaladas de `emilkowalski/skills` (commit `2d22863`, licença MIT em `.claude/skills/LICENSE-emilkowalski-skills`). Instaladas com `npx skills@latest add emilkowalski/skills --skill '*' --agent claude-code --copy -y` (`--copy` porque link simbólico no Windows exige administrador e este repo tem `core.symlinks=false`). Versões registradas em `skills-lock.json`; para atualizar: `npx skills@latest update`.
- Relevantes para este site: `emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance`, `animation-vocabulary`, `apple-design`, `mobile-native`, `break-ui`, `prototype`. Não se aplicam (projeto sem React/Swift/Expo): `animate-expo`, `write-swift`, `ask-sonner`.
- `impeccable` (design de interfaces: `shape`, `critique`, `audit`, `polish`, `animate`, `layout`, `typeset` etc.), de `pbakaus/impeccable`. Instalada com `npx impeccable install --providers=claude --project --no-hooks --force -y` (cópia em `.claude/skills/impeccable` + subagentes em `.claude/agents/`; o `npx impeccable link` não serve aqui porque cria link simbólico). Para atualizar: `npx impeccable update`. O submódulo `.impeccable/` do setup inicial foi removido do repositório (não era usado pela instalação atual).
- Hooks do Impeccable **não** foram instalados (`--no-hooks`; não existe `.claude/settings.json`). O binário do motor (`impeccable.exe`, ~19 MB) fica em `.claude/skills/impeccable/scripts/bin/windows-x64/`. A telemetria anônima do Impeccable está ligada (`npx impeccable telemetry off` desliga).
