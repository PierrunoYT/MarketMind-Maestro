import os
import requests
import json
import logging

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

    def generate_sales_pitch(self, product, additional_info=None):
        """Generate a sales pitch for a given product."""
        prompt = f"Create a highly persuasive and tailored sales pitch for {product}. Your pitch should include:\n"
        prompt += "1. A compelling opening hook\n"
        prompt += "2. Clear articulation of the product's unique value proposition\n"
        prompt += "3. At least three key benefits, with specific examples or data points\n"
        prompt += "4. Anticipation and preemptive addressing of potential objections\n"
        prompt += "5. A strong, action-oriented close with a clear next step\n"
        prompt += "6. Incorporate storytelling elements to make the pitch more engaging and memorable\n"
        if additional_info:
            prompt += f"\nConsider the following additional information:\n"
            prompt += f"Target Audience: {additional_info.get('target_audience', 'Not specified')}\n"
            prompt += f"Marketing Goals: {additional_info.get('marketing_goals', 'Not specified')}\n"
            prompt += f"Budget: {additional_info.get('budget', 'Not specified')}\n"
        prompt += "\nEnsure the pitch is adaptable for various communication channels (in-person, phone, email, video call)."
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

    def call_openrouter_api(self, prompt, language='english'):
        """Make a streaming API call to OpenRouter's Anthropic Claude-3.5-sonnet model."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": f"Respond in {language}. {prompt}"}],
            "stream": True
        }
        try:
            response = requests.post(self.base_url, headers=headers, json=data, stream=True)
            response.raise_for_status()
            full_response = ""
            response_id = None
            for line in response.iter_lines():
                if line:
                    chunk = line.decode('utf-8')
                    if chunk.startswith("data: "):
                        try:
                            chunk_data = json.loads(chunk[6:])
                            if 'id' in chunk_data and not response_id:
                                response_id = chunk_data['id']
                            if chunk_data['choices'][0]['finish_reason'] is None:
                                content = chunk_data['choices'][0]['delta'].get('content', '')
                                full_response += content
                                pass
                            elif 'usage' in chunk_data:
                                print(f"Usage data: {chunk_data['usage']}")
                        except json.JSONDecodeError as e:
                            print(f"JSON decode error: {e}")
                            print(f"Problematic chunk: {chunk}")
                            continue
            print()  # Print a newline at the end
            print(f"Response ID: {response_id}")
            return full_response
        except requests.exceptions.RequestException as e:
            print(f"API request error: {e}")
            return f"Error: {str(e)}"

    def respond_to_agent(self, message, language='english'):
        """Respond to messages from other agents."""
        prompt = f"As a sales AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt, language=language)

# Note: main() function removed as it's no longer needed in this file
