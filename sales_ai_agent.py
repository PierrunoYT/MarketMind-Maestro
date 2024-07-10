import os
import requests

class SalesAIAgent:
    def __init__(self):
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.sales_techniques = [
            "SPIN Selling",
            "Consultative Selling",
            "Solution Selling",
            "Challenger Sale",
            "Value Selling"
        ]
        self.objection_types = [
            "Price",
            "Product",
            "Competitor",
            "No need",
            "Time"
        ]

    def generate_sales_pitch(self, product):
        """Generate a sales pitch for a given product."""
        prompt = f"Generate a compelling sales pitch for the following product: {product}. Include key benefits and a call to action."
        return self.call_openrouter_api(prompt)

    def handle_objection(self, objection_type):
        """Provide strategies to handle a specific type of sales objection."""
        prompt = f"Provide effective strategies to handle the following type of sales objection: {objection_type}. Include specific examples and responses."
        return self.call_openrouter_api(prompt)

    def suggest_follow_up(self, interaction_summary):
        """Suggest a follow-up strategy based on a summary of the previous interaction."""
        prompt = f"Based on the following summary of a sales interaction, suggest an effective follow-up strategy: {interaction_summary}"
        return self.call_openrouter_api(prompt)

    def analyze_sales_performance(self, sales_data):
        """Analyze sales performance data and provide insights."""
        prompt = f"Analyze the following sales performance data and provide actionable insights: {sales_data}"
        return self.call_openrouter_api(prompt)

    def call_openrouter_api(self, prompt):
        """Make an API call to OpenRouter's Anthropic Claude-3.5-sonnet model."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "anthropic/claude-3-sonnet-20240229",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code}, {response.text}"

def main():
    agent = SalesAIAgent()
    print("Sales AI Agent Demo")
    print("------------------")
    try:
        print(agent.generate_sales_pitch("Smart Home Security System"))
        print("\nHandling Objection:")
        print(agent.handle_objection("Price"))
        print("\nSuggesting Follow-up:")
        print(agent.suggest_follow_up("Customer showed interest but didn't commit to a purchase"))
        print("\nAnalyzing Sales Performance:")
        print(agent.analyze_sales_performance("Q1 sales were up 15%, but Q2 saw a 5% decline"))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please make sure you have set the OPENROUTER_API_KEY environment variable.")

if __name__ == "__main__":
    main()
