import os
import google.generativeai as genai

# Configure Google Gemini API Key
# Note: Get a free API key from Google AI Studio
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

class SmartEcomAssistant:
    def __init__(self):
        # Initializing the latest stable flash model for fast responses
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # System instructions to lock the AI into an E-commerce Persona
        self.system_prompt = (
            "You are an expert E-commerce Shopping Assistant. Your goal is to help users find the best "
            "products based on their budget, requirements, and preferences. Be polite, concise, and professional. "
            "Structure your product recommendations cleanly using bullet points, estimated pricing, and pros/cons."
        )

    def get_recommendation(self, user_query, budget):
        full_prompt = (
            f"{self.system_prompt}\n\n"
            f"User is looking for: {user_query}\n"
            f"User Budget: {budget}\n\n"
            f"Please recommend 3 best options matching this criteria."
        )
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"\n❌ Error connecting to GenAI API: Please check your API key. Details: {str(e)}"

def main():
    assistant = SmartEcomAssistant()
    
    print("\n" + "="*45)
    print("   GEN AI E-COMMERCE SHOPPING ASSISTANT   ")
    print("="*45)
    print("Welcome! I am your AI assistant. Tell me what you want to buy today.")
    
    while True:
        print("\n" + "-"*45)
        user_query = input("What item are you looking for? (Type 'exit' to quit): ")
        
        if user_query.lower() == 'exit':
            print("\nThank you for shopping with us! Goodbye.")
            break
            
        budget = input("Enter your maximum budget (e.g., $50, ₹10,000, Under $500): ")
        
        print("\n🤖 AI is searching and analyzing products for you...")
        
        recommendations = assistant.get_recommendation(user_query, budget)
        
        print("\n" + "="*20 + " AI RECOMMENDATIONS " + "="*20)
        print(recommendations)
        print("="*50)

if __name__ == "__main__":
    main()
