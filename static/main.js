document.addEventListener('DOMContentLoaded', () => {

    // ---------- MENU MOBILE ----------
    const menuBotao = document.getElementById('menu-botao');
    const menu = document.getElementById('menu');

    function definirMenu(aberto) {
        menu.classList.toggle('aberto', aberto);
        menuBotao.setAttribute('aria-expanded', String(aberto));
        menuBotao.querySelector('.so-leitor').textContent = aberto ? 'Fechar menu' : 'Abrir menu';
    }

    menuBotao.addEventListener('click', () => {
        definirMenu(menuBotao.getAttribute('aria-expanded') !== 'true');
    });
    menu.addEventListener('click', (e) => {
        if (e.target.closest('a')) definirMenu(false);
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && menu.classList.contains('aberto')) {
            definirMenu(false);
            menuBotao.focus({ preventScroll: true });
        }
    });


    // ---------- SEÇÃO ATUAL NO MENU ----------
    const linksMenu = [...menu.querySelectorAll('a[href^="#"]')];
    const secoes = linksMenu.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);
    if ('IntersectionObserver' in window && secoes.length) {
        const observador = new IntersectionObserver((entradas) => {
            entradas.forEach((entrada) => {
                if (!entrada.isIntersecting) return;
                linksMenu.forEach((link) => {
                    if (link.getAttribute('href') === '#' + entrada.target.id) {
                        link.setAttribute('aria-current', 'true');
                    } else {
                        link.removeAttribute('aria-current');
                    }
                });
            });
        }, { rootMargin: '-35% 0px -55% 0px' });
        secoes.forEach((secao) => observador.observe(secao));
    }


    // ---------- A TORRE SENDO CONSTRUÍDA (só quando o visitante pede) ----------
    const construir = document.getElementById('construir');
    const fiadasTrajetoria = document.getElementById('fiadas-trajetoria');

    construir.addEventListener('click', () => {
        // Remove, força o navegador a recalcular e põe de novo: a animação recomeça da base
        fiadasTrajetoria.classList.remove('reconstruir');
        void fiadasTrajetoria.offsetWidth;
        fiadasTrajetoria.classList.add('reconstruir');
    });


    // --- LÓGICA DO CHATBOT ---
    const chatContainer = document.getElementById('chat-container');
    const chatButton = document.getElementById('chat-button');
    const closeChat = document.getElementById('close-chat');
    const sendChat = document.getElementById('send-chat');
    const chatInput = document.getElementById('chat-input');
    const chatBox = document.getElementById('chat-box');

    // A URL aponta para o nosso próprio back-end
    const API_URL = '/api/chat';
    const TEMPO_LIMITE_MS = 30000; // desiste da resposta depois de 30 s
    let isSending = false;
    let botaoQueAbriu = chatButton;

    const arcos = document.querySelectorAll('[data-abrir-chat]');
    const rotulosFechados = new Map();
    arcos.forEach((arco) => rotulosFechados.set(arco, arco.getAttribute('aria-label')));

    // Todos os arcos acompanham o estado do chat (rótulo e aria-expanded)
    function sincronizarArcos(aberto) {
        arcos.forEach((arco) => {
            arco.setAttribute('aria-expanded', String(aberto));
            arco.setAttribute('aria-label', aberto ? 'Fechar chat com a Puxa Saco' : rotulosFechados.get(arco));
        });
    }

    function openChat(origem) {
        botaoQueAbriu = origem || chatButton;
        chatContainer.classList.add('aberto');
        sincronizarArcos(true);
        chatInput.focus({ preventScroll: true });
    }

    function closeChatWindow() {
        const focoDentro = chatContainer.contains(document.activeElement);
        chatContainer.classList.remove('aberto');
        sincronizarArcos(false);
        // Devolve o foco ao botão que abriu o chat, para quem navega pelo teclado
        if (focoDentro) botaoQueAbriu.focus({ preventScroll: true });
    }

    // Os arcos (o da primeira tela e o fixo) abrem E fecham o chat
    arcos.forEach((botao) => {
        botao.addEventListener('click', () => {
            if (chatContainer.classList.contains('aberto')) {
                closeChatWindow();
            } else {
                openChat(botao);
            }
        });
    });
    closeChat.addEventListener('click', closeChatWindow);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && chatContainer.classList.contains('aberto')) closeChatWindow();
    });

    // O arco fixo só aparece depois que a primeira tela (onde já existe um arco) sai de vista
    const torre = document.querySelector('.torre');
    if (torre && 'IntersectionObserver' in window) {
        new IntersectionObserver(([entrada]) => {
            chatButton.classList.toggle('oculto', entrada.isIntersecting);
        }, { threshold: 0.15 }).observe(torre);
    }

    sendChat.addEventListener('click', sendMessage);
    chatInput.addEventListener('keydown', (e) => {
        // isComposing evita enviar no meio de uma composição (acentos, IME)
        if (e.key === 'Enter' && !e.isComposing) {
            e.preventDefault();
            sendMessage();
        }
    });

    function setSending(value) {
        isSending = value;
        sendChat.disabled = value;
        chatBox.setAttribute('aria-busy', String(value));
    }

    async function sendMessage() {
        const userMessage = chatInput.value.trim();
        if (!userMessage || isSending) return;

        appendMessage(userMessage, 'user');
        chatInput.value = '';
        setSending(true);
        const typing = appendMessage('Puxa Saco está digitando…', 'bot', 'typing-message');

        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), TEMPO_LIMITE_MS);

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                // Enviamos apenas a mensagem do usuário
                body: JSON.stringify({ message: userMessage }),
                signal: controller.signal
            });

            // O back-end responde {reply} ou {error}, inclusive nos erros 4xx/5xx
            const data = await response.json().catch(() => ({}));
            typing.remove();

            if (!response.ok || !data.reply) {
                appendMessage(data.error || "Desculpe, não consegui responder agora. Tente novamente.", 'bot', 'error-message');
                return;
            }
            appendMessage(data.reply, 'bot');

        } catch (error) {
            console.error("Erro ao contatar o back-end:", error);
            typing.remove();
            const texto = error.name === 'AbortError'
                ? "A resposta demorou demais. Tente novamente."
                : "Desculpe, estou com problemas para me conectar no momento. Tente novamente mais tarde.";
            appendMessage(texto, 'bot', 'error-message');
        } finally {
            clearTimeout(timer);
            setSending(false);
        }
    }

    function appendMessage(message, sender, extraClass = '') {
        const messageDiv = document.createElement('div');
        // textContent (e não innerHTML) evita injeção de HTML vinda do modelo
        messageDiv.textContent = message;
        messageDiv.className = `chat-message ${sender}-message ${extraClass}`.trim();
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
        return messageDiv;
    }

});
