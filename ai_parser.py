import requests

# We use Ollama to run Gemma locally. 
# This ensures bank SMS data never leaves the user's device (100% Privacy).
OLLAMA_URL = "http://localhost:11434/api/generate"

sms_text = "Alert: Debited Rs 174.00 from A/c XXXX for spending at DMart on 24-Oct. Avl Bal Rs 5000."

prompt = f"""
You are a secure financial data extractor. Read this bank SMS. 
Extract ONLY the merchant name and amount spent. 
Calculate the 'spare change' needed to round up the amount to the nearest 50.

Output exactly like this:
Merchant: [Name]
Amount Spent: ₹[Amount]
Round-up Delta (Saved): ₹[Spare Change]

SMS Text: {sms_text}
"""

payload = {
    "model": "gemma", # Change to "gemma:2b" or "gemma2" if your tag is different
    "prompt": prompt,
    "stream": False
}

print("Processing incoming SMS locally with Gemma via Ollama...")
try:
    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()
    print("\n--- GEMMA PARSING RESULT ---")
    print(result.get("response", "").strip())
except Exception as e:
    print("Error: Ensure Ollama is running locally. Details:", e)
