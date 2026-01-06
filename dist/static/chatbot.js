function toggleChatbot() {
    const panel = document.getElementById('chatbotPanel');
    panel.classList.toggle('open');
}

function toggleFaq(element) {
    const allFaqs = document.querySelectorAll('.faq-item');
    allFaqs.forEach(faq => {
        if (faq !== element) {
            faq.classList.remove('active');
        }
    });
    element.classList.toggle('active');
}
