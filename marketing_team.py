import os
from marketing_ai_agent import MarketingAIAgent
from sales_ai_agent import SalesAIAgent
from strategy_ai_agent import StrategyAIAgent
from analytics_ai_agent import AnalyticsAIAgent

class MarketingTeam:
    def __init__(self):
        self.marketing_agent = MarketingAIAgent()
        self.sales_agent = SalesAIAgent()
        self.strategy_agent = StrategyAIAgent()
        self.analytics_agent = AnalyticsAIAgent()

    def discuss_marketing_plan(self, question):
        print(f"Marketing Team discussing: {question}\n")

        # Marketing Agent's input
        marketing_input = self.marketing_agent.generate_campaign_idea()
        print(f"Marketing Agent: {marketing_input}\n")

        # Sales Agent's input
        sales_input = self.sales_agent.generate_sales_pitch("the proposed marketing campaign")
        print(f"Sales Agent: {sales_input}\n")

        # Strategy Agent's input
        strategy_input = self.strategy_agent.analyze_market_trends()
        print(f"Strategy Agent: {strategy_input}\n")

        # Analytics Agent's input
        analytics_input = self.analytics_agent.suggest_target_audience()
        print(f"Analytics Agent: {analytics_input}\n")

        # Final plan synthesis
        final_plan = self.synthesize_plan(marketing_input, sales_input, strategy_input, analytics_input)
        print(f"Final Marketing Plan:\n{final_plan}")

    def synthesize_plan(self, marketing, sales, strategy, analytics):
        prompt = f"""
        Synthesize a comprehensive marketing plan based on the following inputs:
        Marketing: {marketing}
        Sales: {sales}
        Strategy: {strategy}
        Analytics: {analytics}

        Provide a cohesive plan that incorporates insights from all agents.
        """
        return self.marketing_agent.call_openrouter_api(prompt)

def main():
    team = MarketingTeam()
    question = input("Enter your marketing question: ")
    team.discuss_marketing_plan(question)

if __name__ == "__main__":
    main()
