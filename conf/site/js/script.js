// script.js

function enviarMensagem() {
    var nome = document.getElementById("nome").value;
    var email = document.getElementById("email").value;
    var mensagem = document.getElementById("mensagem").value;

    if (nome && email && mensagem) {
        var dadosFormulario = {
            nome: nome,
            email: email,
            mensagem: mensagem
        };

        // Substitua a URL da webhook pela sua própria
        var webhookURL = "https://discord.com/api/webhooks/1215360674637549568/CKpuK5D6KhoYqUT2XEwAxIiQjD3YkOD38jG3w39IHDAGdErqFdYoXpZsA2Jqt-PB4ucC";

        var payload = {
            embeds: [{
                title: "Nova mensagem de contato",
                color: 0x3498db, // Cor do embed
                fields: [
                    { name: "Nome", value: `:bust_in_silhouette: ${nome}`, inline: true },
                    { name: "Email", value: `:email: ${email}`, inline: true },
                    { name: "Mensagem", value: `\`\`\`markdown\n${mensagem}\n\`\`\`` }
                ]
            }]
        };

        fetch(webhookURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        })
        .then(response => {
            if (response.ok) {
                alert("Mensagem enviada com sucesso!");
                // Adicione qualquer lógica adicional necessária após o envio bem-sucedido.
            } else {
                alert("Erro ao enviar mensagem. Por favor, tente novamente.");
            }
        })
        .catch(error => {
            console.error("Erro durante o envio da mensagem:", error);
            alert("Ocorreu um erro. Por favor, tente novamente mais tarde.");
        });
    } else {
        alert("Por favor, preencha todos os campos.");
    }
}


// Outras funções ou lógica relacionada ao seu projeto podem ser adicionadas aqui.
