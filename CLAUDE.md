# CLAUDE.md

Portfólio pessoal de **Lucas Costa** (Estatístico; Ciência de Dados, BI e Risco de Crédito). Site de página única em Flask + HTML/CSS/JS puros, com um chatbot ("Puxa Saco") que responde sobre o Lucas usando a API do Gemini.
Repositório: `github.com/luukas20/meu-portifolio` (branch `main`). Todo o conteúdo, UI e commits são em **pt-BR**.

## Stack

- Python 3.12, Flask 3.1, `google-genai` (modelo `gemini-2.0-flash`), `python-dotenv`, `gunicorn` (produção)
- Front: templates Jinja2, `static/style.css` (CSS puro), `static/main.js` (JS vanilla). CDNs: Google Fonts (Poppins), bootstrap-icons, MathJax (fórmula da Perda Esperada)
- Sem banco de dados, sem testes, sem build/bundler, sem CI/CD no repositório

## Comandos (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

flask --app main run --debug     # dev em http://127.0.0.1:5000 (python main.py também funciona)
gunicorn main:app                # produção
```

- Variável de ambiente em `.env` (gitignorado): `GEMINI_API_KEY`. **Nunca ler, imprimir ou commitar o conteúdo do `.env`.**
- Não há suíte de testes nem linter: validar mudanças subindo o servidor e conferindo no navegador (desktop e mobile ≤ 1020px).
- Node.js LTS (24.x) instalado via winget só para rodar ferramentas `npx` (skills); o app em si não usa Node. Em terminais já abertos o PATH só atualiza após reiniciar.
- O deploy não está descrito no repositório (não há Procfile/Dockerfile/render.yaml). Perguntar ao Lucas antes de assumir a plataforma.

## Arquitetura

```
main.py                  cria `app = Flask(__name__)` e faz `from views import *` no final
views.py                 rotas, cliente Gemini, base de conhecimento e prompt do chatbot
templates/homepage.html  página única: topo, especialidades, sobre-mim, portifólio, contato, footer, widget do chat
templates/projetos.html  LEGADO/órfão (ver "Armadilhas")
static/style.css         todo o CSS; tema por variáveis em :root; um único breakpoint (max-width: 1020px)
static/main.js           menu mobile + chatbot (fetch POST /api/chat)
static/images/           PNGs/JPEG usados via url_for (nomes com espaço e acento)
```

- **Rotas** (`views.py`): `GET /` (endpoint `pagina_home`, renderiza `homepage.html`) e `POST /api/chat`.
- **Import circular** `main` ↔ `views`: `views.py` faz `from main import app`. Funciona, mas é frágil; manter `from views import *` no **fim** do `main.py` e não adicionar imports de `views` antes de `app` existir.
- **Chatbot**: o front envia `{message}` para `/api/chat`; o back monta um prompt único (persona "Puxa Saco" + texto `dados_linkedin` + a mensagem) e chama `client.models.generate_content`; devolve `{reply}` ou `{error}` com status 500. É stateless (sem histórico entre mensagens). `dados_linkedin` é um texto fixo dentro do `views.py` — é a **única fonte de conhecimento** do bot.
- **Tema**: cores só via variáveis (`--primary-*`, `--accent-*`, `--text-*`, `--bg-*`); fonte Poppins. Seção do portifólio = lista de `.project-card` dentro de `.project-container` (2 por linha no desktop, 1 no mobile).

## Convenções do código

- Nomes em português: classes CSS (`.sobre-mim`, `.especialidades-box`), ids, endpoint (`pagina_home`), comentários e mensagens de commit curtas ("Adicionando o Projeto da Perda Esperada").
- A grafia **"portifolio"** (sic) é usada de forma consistente em classes, ids e âncoras (`.portifolio`, `#portifolio`, `<title>`). Não corrigir só uma ocorrência; se for renomear, trocar tudo (HTML, CSS, links de navegação).
- Indentação de 4 espaços. CSS organizado em blocos com cabeçalho em comentário MAIÚSCULO (`/* ESTILO DO CABEÇALHO */`); HTML fecha divs com comentário (`</div><!--flex-->`).
- Imagens sempre via `{{ url_for('static', filename='images/...') }}`; cores sempre via variáveis CSS (nada de hex solto).
- `appendMessage` em `main.js` usa `textContent` de propósito (evita injeção de HTML vinda do modelo). Manter assim.

## Manutenção do conteúdo (sincronização manual)

Não existe fonte única de dados; o mesmo conteúdo vive em mais de um lugar:

- **Novo projeto / cargo / habilidade**: atualizar (1) o card em `homepage.html`, (2) `dados_linkedin` em `views.py` (senão o chatbot responde que "não tem essa informação") e (3) o texto de "Sobre mim", se mudar.
- **Novo card**: copiar um `.project-card` existente (header com título + `.project-tag` com ícone, `.card-image` com `background-image`, `.project-description`).
- Links de redes sociais (LinkedIn, GitHub, e-mail) aparecem duas vezes em `homepage.html` (sobre-mim e contato).
- Texto profissional, persona e dados pessoais são conteúdo do Lucas: perguntar antes de reescrever ou "melhorar" o texto.

## Armadilhas conhecidas (revisar/remover conforme forem corrigidas)

- **`.venv` local quebrada**: foi criada em outro caminho (OneDrive) e está sem os pacotes (nem Flask). Recriar com os comandos acima.
- **`templates/projetos.html` é código morto**: não há rota para ele, referencia `url_for('pagina_projetos')` (endpoint inexistente → `BuildError` se renderizado), carrega Tailwind via CDN e está desatualizado (faltam os projetos Perda Esperada e Cat vs Dog). `main.js` também quebraria nele (não tem os elementos do menu mobile).
- **`requirements.txt` inflado**: tem Streamlit, pandas, numpy, altair, pydeck, git-filter-repo, GitPython etc., que o app Flask não usa. Também lista `google-generativeai` (legado, só `google-genai` é importado) e `dotenv` além de `python-dotenv`.
- **Versionados apesar do `.gitignore`**: `__pycache__/*.pyc` (cpython-311) e `Portifolio.code-workspace`.
- `homepage.html` carrega `polyfill.io` (domínio comprometido em 2024); o MathJax v3 não precisa dele.
- Chatbot sem validação do corpo (`request.json['message']`), sem limite de tamanho/taxa, e com a mensagem do usuário interpolada direto no prompt (prompt injection possível).

## Skills

- `.claude/skills/<nome>/SKILL.md` guarda as skills baixadas do GitHub. A pasta `.claude/` inteira está no `.gitignore`: em outra máquina, recriar com os comandos abaixo (ou `npx skills experimental_install`, que restaura as do Emil a partir do `skills-lock.json`).
- Instaladas de `emilkowalski/skills` (commit `2d22863`, licença MIT em `.claude/skills/LICENSE-emilkowalski-skills`). Instaladas com `npx skills@latest add emilkowalski/skills --skill '*' --agent claude-code --copy -y` (`--copy` porque link simbólico no Windows exige administrador e este repo tem `core.symlinks=false`). Versões registradas em `skills-lock.json`; para atualizar: `npx skills@latest update`.
- Relevantes para este site: `emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance`, `animation-vocabulary`, `apple-design`, `mobile-native`, `break-ui`, `prototype`. Não se aplicam (projeto sem React/Swift/Expo): `animate-expo`, `write-swift`, `ask-sonner`.
- `impeccable` (design de interfaces: `shape`, `critique`, `audit`, `polish`, `animate`, `layout`, `typeset` etc.), de `pbakaus/impeccable`. Instalada com `npx impeccable install --providers=claude --project --no-hooks --force -y` (cópia em `.claude/skills/impeccable` + subagentes em `.claude/agents/`; o `npx impeccable link` não serve aqui porque cria link simbólico). Para atualizar: `npx impeccable update`. O submódulo `.impeccable/` (não editar nada ali) ficou do setup inicial e **não é usado** pela instalação atual.
- Hooks do Impeccable **não** foram instalados (`--no-hooks`; não existe `.claude/settings.json`). O binário do motor (`impeccable.exe`, ~19 MB) fica em `.claude/skills/impeccable/scripts/bin/windows-x64/`. A telemetria anônima do Impeccable está ligada (`npx impeccable telemetry off` desliga).
