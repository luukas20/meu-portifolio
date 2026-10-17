document.addEventListener('DOMContentLoaded', () => {

    // ---------- MENU MOBILE ----------
    let btnMenu = document.getElementById('btn-abrir-menu')
    let menu = document.getElementById('menu-mobile')
    let OverlayMenu = document.getElementById('overlay-menu')

    btnMenu.addEventListener('click', ()=>{
        menu.classList.add('abrir-menu')
    })
    menu.addEventListener('click', ()=>{
        menu.classList.remove('abrir-menu')
    })
    OverlayMenu.addEventListener('click', ()=>{
        menu.classList.remove('abrir-menu')
    })


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

    function openChat() {
        chatContainer.classList.add('aberto');
        chatButton.setAttribute('aria-expanded', 'true');
        chatInput.focus({ preventScroll: true });
    }

    function closeChatWindow() {
        const focoDentro = chatContainer.contains(document.activeElement);
        chatContainer.classList.remove('aberto');
        chatButton.setAttribute('aria-expanded', 'false');
        // Devolve o foco ao botão para quem navega pelo teclado
        if (focoDentro) chatButton.focus({ preventScroll: true });
    }

    // Este botão abre E fecha o chat
    chatButton.addEventListener('click', () => {
        if (chatContainer.classList.contains('aberto')) {
            closeChatWindow();
        } else {
            openChat();
        }
    });
    closeChat.addEventListener('click', closeChatWindow);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && chatContainer.classList.contains('aberto')) closeChatWindow();
    });

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
