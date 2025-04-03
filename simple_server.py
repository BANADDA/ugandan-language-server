import os

from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

# Mock translation endpoint
@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400
        
        text = data['text']
        target_language = data.get('language', 'rutooro')
        
        # Validate target language
        valid_languages = ['rutooro', 'luganda', 'acholi', 'runyankore']
        if target_language not in valid_languages:
            return jsonify({
                "error": f"Invalid target language. Supported languages are: {', '.join(valid_languages)}"
            }), 400
        
        # Mock translation
        mock_translations = {
            'rutooro': 'Okusoma nikwomuhendo ahabw\'okukulaakulana.',
            'luganda': 'Okusoma kikulu nnyo mu nkulaakulana.',
            'acholi': 'Kwan dongo pire me yubo lobo.',
            'runyankore': 'Okushoma nikukuru ahabw\'okukulaakulana.'
        }
        
        return jsonify({
            "original_text": text,
            "translated_text": mock_translations[target_language],
            "target_language": target_language
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 