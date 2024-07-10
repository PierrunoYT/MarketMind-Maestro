import random

class MarketingAIAgent:
    def __init__(self):
        self.strategies = [
            "Social Media Marketing",
            "Content Marketing",
            "Email Marketing",
            "Influencer Marketing",
            "SEO Optimization"
        ]
    
    def generate_campaign_idea(self):
        """Generate a random marketing campaign idea."""
        return f"Campaign Idea: {random.choice(self.strategies)}"
    
    def analyze_market_trends(self):
        """Simulate market trend analysis."""
        trends = ["Mobile-first", "Video Content", "Personalization", "AI-driven Marketing"]
        return f"Current Trend: {random.choice(trends)}"
    
    def suggest_target_audience(self):
        """Suggest a target audience."""
        audiences = ["Millennials", "Gen Z", "Baby Boomers", "Small Business Owners", "Tech Enthusiasts"]
        return f"Target Audience: {random.choice(audiences)}"

def main():
    agent = MarketingAIAgent()
    print("Marketing AI Agent Demo")
    print("-----------------------")
    print(agent.generate_campaign_idea())
    print(agent.analyze_market_trends())
    print(agent.suggest_target_audience())

if __name__ == "__main__":
    main()
