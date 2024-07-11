import os
import requests
import json
import logging

class AnalyticsAIAgent:
    def __init__(self):
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.audiences = {
            "Millennials": {"age": "25-40", "interests": ["Technology", "Experiences", "Social causes"]},
            "Gen Z": {"age": "10-25", "interests": ["Social media", "Authenticity", "Diversity"]},
            "Baby Boomers": {"age": "57-75", "interests": ["Health", "Travel", "Financial security"]},
            "Small Business Owners": {"age": "Various", "interests": ["Efficiency", "Networking", "Growth strategies"]},
            "Tech Enthusiasts": {"age": "Various", "interests": ["Gadgets", "Innovation", "Early adoption"]}
        }

    def analyze_target_audience(self, product, additional_info=None):
        """Analyze the target audience for a given product."""
        prompt = f"Conduct an in-depth target audience analysis for {product}. Your analysis should include:\n"
        prompt += "1. Detailed demographic profile (age, gender, income, education, occupation, location)\n"
        prompt += "2. Psychographic characteristics (interests, values, lifestyle, personality traits)\n"
        prompt += "3. Behavioral patterns (purchasing habits, brand loyalties, media consumption)\n"
        prompt += "4. Pain points and challenges the audience faces that {product} can address\n"
        prompt += "5. Decision-making process and factors influencing their choices\n"
        prompt += "6. Segmentation of the audience into distinct buyer personas\n"
        prompt += "7. Channels and platforms where this audience can be effectively reached\n"
        prompt += "8. Tailored messaging strategies for each segment\n"
        prompt += "9. Potential objections or resistance points from this audience\n"
        prompt += "10. Opportunities for audience expansion or market penetration\n"
        if additional_info:
            prompt += f"\nConsider the following additional context in your analysis:\n{additional_info}"
        return self.call_openrouter_api(prompt)

    def perform_sentiment_analysis(self, text):
        """Perform sentiment analysis on given text."""
        prompt = f"Perform a detailed sentiment analysis on the following text. Classify it as positive, negative, or neutral, and explain why: '{text}'"
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
                                print(content, end='', flush=True)
                            elif 'usage' in chunk_data:
                                logging.info(f"Usage data: {chunk_data['usage']}")
                        except json.JSONDecodeError as e:
                            logging.error(f"JSON decode error: {e}")
                            logging.error(f"Problematic chunk: {chunk}")
                            continue
            print()  # Print a newline at the end
            logging.info(f"Response ID: {response_id}")
            return full_response
        except requests.exceptions.RequestException as e:
            logging.error(f"API request error: {e}")
            return f"Error: {str(e)}"

    def respond_to_agent(self, message):
        """Respond to messages from other agents."""
        prompt = f"As an analytics AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt)
