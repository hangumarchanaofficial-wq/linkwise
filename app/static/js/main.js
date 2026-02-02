document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('summarizeForm');
    const input = document.getElementById('urlInput');
    const button = document.getElementById('submitBtn');
    const resultsSection = document.getElementById('resultsSection');
    const summaryOutput = document.getElementById('summaryOutput');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 1. Loading State
        button.disabled = true;
        button.innerHTML = `<span>Analysing...</span> <i class="ph-bold ph-circle-notch animate-spin"></i>`;
        resultsSection.classList.add('hidden');

        try {
            // 2. Fetch from Flask API
            const response = await fetch('/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: input.value }),
            });

            if (!response.ok) throw new Error('Failed to fetch summary');

            const data = await response.json();

            // 3. Display Results
            summaryOutput.innerText = data.summary;
            resultsSection.classList.remove('hidden');
            
            // Smooth scroll to results
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'center' });

        } catch (error) {
            console.error('Error:', error);
            summaryOutput.innerHTML = `<span class="text-red-400">Error: Could not reach the AI. Make sure Ollama and your Flask server are running.</span>`;
            resultsSection.classList.remove('hidden');
        } finally {
            // 4. Reset Button
            button.disabled = false;
            button.innerHTML = `<span>Summarize</span> <i class="ph-bold ph-sparkle"></i>`;
        }
    });
});