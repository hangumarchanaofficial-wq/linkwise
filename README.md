diff --git a/README.md b/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..2ecc5ef216a4559df672704189253bbac4b4a4f8
--- /dev/null
+++ b/README.md
@@ -0,0 +1,30 @@
+# Linkwise
+
+Linkwise is a small Flask web app that summarizes a URL. It scrapes readable content from a page, trims the text, and sends it to a local Ollama model to generate a concise summary.
+
+## Features
+- Submit a URL from a simple web UI.
+- Extracts readable content from common page containers (`article`, `main`, `body`).
+- Summarizes content using a local Ollama instance.
+
+## Requirements
+- Python 3.9+
+- Ollama running locally on `http://localhost:11434`
+- Python packages: `flask`, `requests`, `beautifulsoup4`
+
+## Setup
+```bash
+python -m venv .venv
+source .venv/bin/activate
+pip install flask requests beautifulsoup4
+```
+
+## Run
+```bash
+python run.py
+```
+Then open `http://localhost:5000` in your browser.
+
+## Notes
+- The summarization model is configured in `app/services/ollama_api.py` (default: `gemma3:4b`).
+- The scraper limits extracted text to 8,000 characters to keep prompts lightweight.
