import os

from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

# Translation endpoint
@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Lazy load the model on first use
        global translator
        if 'translator' not in globals():
            print("Loading translation model...")
            model_name = "mmuniversity/rutooro-multilingual-translator"
            translator = pipeline("translation", model=model_name, device="cpu")
            print("Model loaded successfully!")
        
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
        
        # Format input with language token
        input_text = f">>{target_language}<< {text}"
        
        # Perform translation
        translation = translator(input_text)
        
        return jsonify({
            "original_text": text,
            "translated_text": translation[0]['translation_text'],
            "target_language": target_language
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Batch translation endpoint
@app.route('/translate/batch', methods=['POST'])
def batch_translate():
    try:
        # Lazy load the model on first use
        global translator
        if 'translator' not in globals():
            print("Loading translation model...")
            model_name = "mmuniversity/rutooro-multilingual-translator"
            translator = pipeline("translation", model=model_name, device="cpu")
            print("Model loaded successfully!")
        
        data = request.json
        
        if not data or 'texts' not in data:
            return jsonify({"error": "Missing 'texts' field in request"}), 400
        
        texts = data['texts']
        target_language = data.get('language', 'rutooro')
        
        # Validate target language
        valid_languages = ['rutooro', 'luganda', 'acholi', 'runyankore']
        if target_language not in valid_languages:
            return jsonify({
                "error": f"Invalid target language. Supported languages are: {', '.join(valid_languages)}"
            }), 400
        
        results = []
        for text in texts:
            # Format input with language token
            input_text = f">>{target_language}<< {text}"
            
            # Perform translation
            translation = translator(input_text)
            
            results.append({
                "original_text": text,
                "translated_text": translation[0]['translation_text']
            })
        
        return jsonify({
            "translations": results,
            "target_language": target_language
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 