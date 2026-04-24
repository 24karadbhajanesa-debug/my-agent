import google.generativeai as genai
import config
from tools.tavily_tool import search_medicine_info

genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

class MedicineAgent:
    def __init__(self):
        self.system_prompt = (
            "You are a professional AI Medicine Agent. "
            "Your goal is to provide accurate and safe information about medicines. "
            "You MUST state that you are not a medical professional and that the information "
            "provided is for educational purposes only. Always advise the user to consult "
            "a healthcare provider."
        )

    def analyze_medicine(self, query):
        # Step 1: Search for information
        search_results = search_medicine_info(query)
        
        # Step 2: Combine and synthesize with Gemini
        context = "\n".join([f"Title: {res['title']}\nContent: {res['content']}" for res in search_results])
        
        prompt = (
            f"{self.system_prompt}\n\n"
            f"User Query: {query}\n\n"
            f"Search Context:\n{context}\n\n"
            "Synthesize this information and describe the medicine, its uses, dosage, and side effects. "
            "Ensure you provide a clear, concise, and professional summary."
        )
        
        response = model.generate_content(prompt)
        return response.text
