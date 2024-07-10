import random
from collections import defaultdict
import requests
import os
import json

class MarketingAIAgent:
    def __init__(self):
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.strategies = {
            "Social Media Marketing": ["Facebook", "Instagram", "Twitter", "LinkedIn", "TikTok"],
            "Content Marketing": ["Blog posts", "Whitepapers", "Infographics", "Videos", "Podcasts"],
            "Email Marketing": ["Newsletters", "Drip campaigns", "Promotional emails", "Transactional emails"],
            "Influencer Marketing": ["Micro-influencers", "Celebrity endorsements", "Brand ambassadors"],
            "SEO Optimization": ["On-page SEO", "Off-page SEO", "Technical SEO", "Local SEO"]
        }
        self.market_trends = {
            "Mobile-first": "Prioritizing mobile user experience in all digital strategies",
            "Video Content": "Short-form videos, live streaming, and interactive video content",
            "Personalization": "Tailoring content and offers to individual user preferences",
            "AI-driven Marketing": "Utilizing AI for predictive analytics and automated marketing tasks",
            "Voice Search Optimization": "Adapting content for voice-activated devices and searches",
            "Sustainability": "Eco-friendly practices and messaging in marketing campaigns"
        }
        self.audiences = {
            "Millennials": {"age": "25-40", "interests": ["Technology", "Experiences", "Social causes"]},
            "Gen Z": {"age": "10-25", "interests": ["Social media", "Authenticity", "Diversity"]},
            "Baby Boomers": {"age": "57-75", "interests": ["Health", "Travel", "Financial security"]},
            "Small Business Owners": {"age": "Various", "interests": ["Efficiency", "Networking", "Growth strategies"]},
            "Tech Enthusiasts": {"age": "Various", "interests": ["Gadgets", "Innovation", "Early adoption"]}
        }
    
    def generate_campaign_idea(self, strategy=None):
        """Generate a detailed marketing campaign idea."""
        prompt = f"Generate a detailed marketing campaign idea for {strategy if strategy else 'any marketing strategy'}. Include specific tactics and channels."
        return self.call_openrouter_api(prompt)
    
    def analyze_market_trends(self):
        """Provide detailed market trend analysis."""
        prompt = "Analyze current market trends in digital marketing. Provide detailed descriptions of at least 3 significant trends."
        return self.call_openrouter_api(prompt)
    
    def suggest_target_audience(self):
        """Suggest a target audience with detailed information."""
        prompt = "Suggest a target audience for a marketing campaign. Include age range, key interests, and any other relevant demographic information."
        return self.call_openrouter_api(prompt)
    
    def perform_sentiment_analysis(self, text):
        """Perform sentiment analysis on given text."""
        prompt = f"Perform a detailed sentiment analysis on the following text. Classify it as positive, negative, or neutral, and explain why: '{text}'"
        return self.call_openrouter_api(prompt)
    
    def analyze_competitors(self, competitors):
        """Perform a competitor analysis."""
        prompt = f"Perform a detailed competitor analysis for the following companies: {', '.join(competitors)}. For each competitor, provide strengths, weaknesses, and potential strategies to compete against them."
        return self.call_openrouter_api(prompt)
    
    def suggest_budget_allocation(self, total_budget):
        """Suggest budget allocation for different marketing channels."""
        channels = ["Social Media Ads", "Content Creation", "Influencer Partnerships", "SEO", "Email Marketing"]
        allocation = {}
        remaining_budget = total_budget
        for channel in channels[:-1]:
            amount = round(random.uniform(0.1, 0.3) * remaining_budget, 2)
            allocation[channel] = amount
            remaining_budget -= amount
        allocation[channels[-1]] = round(remaining_budget, 2)
        return allocation

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
        prompt = f"As a marketing AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt)

# Note: main() function removed as it's no longer needed in this file
