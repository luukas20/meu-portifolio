document.addEventListener('DOMContentLoaded', () => {

    // ---------- Accordion para subseções ----------
    document.querySelectorAll('.toggle').forEach(header => {
        header.addEventListener('click', () => {
            const flexDiv = header.nextElementSibling; // a div.flex abaixo do h3
            
            // alterna visibilidade da div
            if(flexDiv.style.display === "flex"){
                flexDiv.style.display = "none";
                header.classList.remove('active'); // remove rotação
            } else {
                flexDiv.style.display = "flex";
                header.classList.add('active'); // adiciona rotação
            }
        });
    });

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
    
    // Este botão agora abre E fecha o chat
    chatButton.addEventListener('click', () => {
        const isChatVisible = chatContainer.style.display === 'flex';
        if (isChatVisible) {
        chatContainer.style.display = 'none';
        } else {
        chatContainer.style.display = 'flex';
        }
    });
    closeChat.addEventListener('click', () => chatContainer.style.display = 'none');
    sendChat.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    // **MODIFICADO** A URL agora aponta para o nosso próprio back-end
    const API_URL = '/api/chat'; 
    
    async function sendMessage() {
        const userMessage = chatInput.value.trim();
        if (!userMessage) return;

        appendMessage(userMessage, 'user');
        chatInput.value = '';
        
        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                // **MODIFICADO** Enviamos apenas a mensagem do usuário
                body: JSON.stringify({ message: userMessage })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            // **MODIFICADO** A resposta agora vem em 'data.reply'
            const botMessage = data.reply;
            appendMessage(botMessage, 'bot');

        } catch (error) {
            console.error("Erro ao contatar o back-end:", error);
            appendMessage("Desculpe, estou com problemas para me conectar no momento. Tente novamente mais tarde.", 'bot');
        }
    }

    function appendMessage(message, sender) {
        const messageDiv = document.createElement('div');
        // Sanitize message to prevent HTML injection
        messageDiv.textContent = message;
        messageDiv.className = `chat-message ${sender}-message`;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
    }
    
    // ---------- Outras funções do site podem ir aqui ----------
    // exemplo: sliders, modais, filtros, etc.

});
