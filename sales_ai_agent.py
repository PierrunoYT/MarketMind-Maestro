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
        prompt = f"Generate a compelling sales pitch for jetflame lighters. Include key benefits, unique selling points, and a strong call to action."
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
        """Make a streaming API call to OpenRouter's Anthropic Claude-3.5-sonnet model."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }
        response = requests.post(self.base_url, headers=headers, json=data, stream=True)
        if response.status_code == 200:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    chunk = line.decode('utf-8')
                    if chunk.startswith("data: "):
                        chunk_data = json.loads(chunk[6:])
                        if chunk_data['choices'][0]['finish_reason'] is None:
                            content = chunk_data['choices'][0]['delta'].get('content', '')
                            full_response += content
                            print(content, end='', flush=True)
            print()  # Print a newline at the end
            return full_response
        else:
            return f"Error: {response.status_code}, {response.text}"

    def respond_to_agent(self, message):
        """Respond to messages from other agents."""
        prompt = f"As a sales AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt)

# Note: main() function removed as it's no longer needed in this file
