import random
from collections import defaultdict

class MarketingAIAgent:
    def __init__(self):
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
        if not strategy:
            strategy = random.choice(list(self.strategies.keys()))
        tactic = random.choice(self.strategies[strategy])
        return f"Campaign Idea: {strategy} focusing on {tactic}"
    
    def analyze_market_trends(self):
        """Provide detailed market trend analysis."""
        trend, description = random.choice(list(self.market_trends.items()))
        return f"Current Trend: {trend}\nDescription: {description}"
    
    def suggest_target_audience(self):
        """Suggest a target audience with detailed information."""
        audience, details = random.choice(list(self.audiences.items()))
        return f"Target Audience: {audience}\nAge Range: {details['age']}\nKey Interests: {', '.join(details['interests'])}"
    
    def perform_sentiment_analysis(self, text):
        """Perform basic sentiment analysis on given text."""
        positive_words = set(['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic'])
        negative_words = set(['bad', 'poor', 'terrible', 'awful', 'horrible', 'disappointing'])
        
        words = text.lower().split()
        positive_count = sum(word in positive_words for word in words)
        negative_count = sum(word in negative_words for word in words)
        
        if positive_count > negative_count:
            return "Positive"
        elif negative_count > positive_count:
            return "Negative"
        else:
            return "Neutral"
    
    def analyze_competitors(self, competitors):
        """Perform a basic competitor analysis."""
        analysis = defaultdict(list)
        for competitor in competitors:
            strength = random.choice(["Strong brand presence", "Innovative products", "Competitive pricing", "Excellent customer service"])
            weakness = random.choice(["Limited market reach", "Outdated technology", "Poor customer reviews", "Lack of product diversity"])
            analysis[competitor] = [f"Strength: {strength}", f"Weakness: {weakness}"]
        return dict(analysis)
    
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

def main():
    agent = MarketingAIAgent()
    print("Advanced Marketing AI Agent Demo")
    print("--------------------------------")
    print(agent.generate_campaign_idea())
    print("\n" + agent.analyze_market_trends())
    print("\n" + agent.suggest_target_audience())
    
    print("\nSentiment Analysis:")
    print(agent.perform_sentiment_analysis("This product is amazing and fantastic!"))
    
    print("\nCompetitor Analysis:")
    competitors = ["CompanyA", "CompanyB"]
    print(agent.analyze_competitors(competitors))
    
    print("\nBudget Allocation:")
    print(agent.suggest_budget_allocation(10000))

if __name__ == "__main__":
    main()
