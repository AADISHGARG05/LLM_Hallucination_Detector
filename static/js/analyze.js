const textInput = document.getElementById('text-input');
const charCount = document.getElementById('char-count');
const analyzeBtn = document.getElementById('analyze-btn');
const inputView = document.getElementById('input-view');
const resultsView = document.getElementById('results-view');

// Character counter logic
textInput.addEventListener('input', () => {
    const len = textInput.value.length;
    charCount.textContent = `${len} / 5000 characters`;
    analyzeBtn.disabled = len < 10;
});

/**
 * Simulates the API call to /analyze and UI transition
 */
async function performAnalysis() {
    if (textInput.value.length < 20) return;

    const btnText = analyzeBtn.querySelector('.btn-text');
    const loader = analyzeBtn.querySelector('.loader');

    analyzeBtn.disabled = true;
    btnText.style.opacity = '0.5';
    loader.classList.remove('hidden');

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: textInput.value })
        });

        const data = await response.json();

        showResults({
            score: Math.round(data.hallucination_risk * 100),
            bert: Math.round(data.signals.model_probability * 100),
            consistency: Math.round(data.signals.semantic_consistency * 100),
            uncertainty: Math.round(data.signals.linguistic_uncertainty * 100),
            label: data.risk_label
        });

    } catch (err) {
        alert("Error analyzing text");
    }
}


/**
 * Renders the results view with animations
 */
function showResults(data) {
    inputView.classList.add('hidden');

    setTimeout(() => {
        inputView.style.display = 'none';
        resultsView.style.display = 'block';
        resultsView.classList.remove('hidden');

        const scoreText = document.getElementById('score-text');
        const scoreFill = document.getElementById('score-fill');
        const riskStatus = document.getElementById('risk-status');

        // % circle
        scoreText.textContent = `${data.score}%`;
        scoreFill.style.strokeDasharray = `${data.score}, 100`;

        // ✅ THIS IS THE IMPORTANT PART
        riskStatus.textContent = data.label + " Risk";

        if (data.label === "High") {
            riskStatus.style.color = "var(--accent-red)";
        } else if (data.label === "Medium") {
            riskStatus.style.color = "var(--accent-orange)";
        } else {
            riskStatus.style.color = "var(--accent-green)";
        }

        // Progress bars
        document.getElementById('bert-bar').style.width = `${data.bert}%`;
        document.getElementById('semantic-bar').style.width = `${data.consistency}%`;
        document.getElementById('uncertainty-bar').style.width = `${data.uncertainty}%`;

    }, 400);
}
/**
 * Resets the UI back to input state
 */
function resetAnalysis() {
    resultsView.classList.add('hidden');
    
    setTimeout(() => {
        resultsView.style.display = 'none';
        inputView.style.display = 'block';
        inputView.classList.remove('hidden');
        
        // Reset inputs
        textInput.value = '';
        charCount.textContent = '0 / 5000 characters';
        
        // Reset loader
        analyzeBtn.disabled = false;
        analyzeBtn.querySelector('.btn-text').style.opacity = '1';
        analyzeBtn.querySelector('.loader').classList.add('hidden');
    }, 400);
}