import json

import requests

# Base URL of the API server
BASE_URL = "http://localhost:5000"  # Change to your server address if needed

def test_health():
    """Test the health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print("Health Check Response:", response.json())
    
def test_translation():
    """Test translating text to different languages"""
    test_text = "Education is important for community development."
    
    # Test all supported languages
    languages = ['rutooro', 'luganda', 'acholi', 'runyankore']
    
    print("\nTesting translation to different languages:")
    for lang in languages:
        data = {
            "text": test_text,
            "language": lang
        }
        
        response = requests.post(f"{BASE_URL}/translate", json=data)
        result = response.json()
        
        print(f"\n{lang.capitalize()}: {result.get('translated_text', 'Error')}")

if __name__ == "__main__":
    print("Starting API tests...\n")
    
    # Run the tests
    test_health()
    test_translation()
    
    print("\nTests completed.") 