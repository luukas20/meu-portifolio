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

    // ---------- Outras funções do site podem ir aqui ----------
    // exemplo: sliders, modais, filtros, etc.

});
