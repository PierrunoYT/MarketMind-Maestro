import os
import requests

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

    def analyze_target_audience(self, product):
        """Analyze the target audience for a given product."""
        prompt = f"Perform a comprehensive target audience analysis for {product}. Include demographic information (age, gender, income, education), psychographic details (interests, values, lifestyle), behavioral patterns, and any other relevant characteristics. Explain why this audience is suitable for {product} and how to effectively reach and engage them."
        return self.call_openrouter_api(prompt)

    def perform_sentiment_analysis(self, text):
        """Perform sentiment analysis on given text."""
        prompt = f"Perform a detailed sentiment analysis on the following text. Classify it as positive, negative, or neutral, and explain why: '{text}'"
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

    def respond_to_agent(self, message):
        """Respond to messages from other agents."""
        prompt = f"As an analytics AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt)
