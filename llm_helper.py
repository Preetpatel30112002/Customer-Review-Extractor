import google.generativeai as genai

# Configure with your API key
GOOGLE_API_KEY = "AIzaSyAteErf2v5_Qzo1Iou5TjvaNWRo8_n3FLA"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

def get_likely_review_elements(htmlcontent):
    prompt = f"""Given the following HTML content, suggest the MOST LIKELY CSS selector to extract individual customer review elements. Return ONLY the selector:
    ```html
    {htmlcontent}
    ```"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        print("response",response.text.strip())
        return response.text.strip()
    except Exception as e:
        print(f"LLM API Error: {e}")
        # Fallback to a default selector
        return ".review-container"  # Replace with a suitable default selector