import requests
import os

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
    
    def generate_campaign_idea(self, product, strategy=None):
        """Generate a detailed marketing campaign idea."""
        prompt = f"Generate a detailed marketing campaign idea for {product} using {strategy if strategy else 'any marketing strategy'}. Include specific tactics and channels."
        return self.call_openrouter_api(prompt)
    
    def analyze_competitors(self, competitors):
        """Perform a competitor analysis."""
        prompt = f"Perform a detailed competitor analysis for the following companies: {', '.join(competitors)}. For each competitor, provide strengths, weaknesses, and potential strategies to compete against them."
        return self.call_openrouter_api(prompt)
    
    def suggest_budget_allocation(self, total_budget):
        """Suggest budget allocation for different marketing channels."""
        prompt = f"Suggest a budget allocation for a total marketing budget of ${total_budget}. Include at least 5 different marketing channels and provide a rationale for each allocation."
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
        prompt = f"As a marketing AI agent, respond to the following message from another agent: {message}"
        return self.call_openrouter_api(prompt)
