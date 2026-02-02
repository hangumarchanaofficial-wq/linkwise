from flask import Blueprint, request, jsonify, render_template
from app.services.scraper import scrape_url
from app.services.ollama_api import get_llm_summary

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/summarize', methods=['POST'])
def handle_summarize():
    # Use request.get_json() to handle incoming POST data
    data = request.get_json()
    target_url = data.get('url')
    
    if not target_url:
        return jsonify({'error': 'URL is required'}), 400
    
    raw_text = scrape_url(target_url)
    summary = get_llm_summary(raw_text)
    
    return jsonify({'summary': summary})