import unittest
from unittest.mock import patch, MagicMock
from marketing_team import MarketingTeam, create_styled_document
from marketing_ai_agent import MarketingAIAgent
from sales_ai_agent import SalesAIAgent
from strategy_ai_agent import StrategyAIAgent
from analytics_ai_agent import AnalyticsAIAgent

class TestMarketingTeam(unittest.TestCase):
    def setUp(self):
        self.marketing_team = MarketingTeam()

    @patch('marketing_team.create_styled_document')
    def test_discuss_marketing_plan(self, mock_create_styled_document):
        # Mock the AI agents' methods
        self.marketing_team.marketing_agent.generate_campaign_idea = MagicMock(return_value="Marketing Campaign Idea")
        self.marketing_team.sales_agent.respond_to_agent = MagicMock(return_value="Sales Feedback")
        self.marketing_team.strategy_agent.analyze_market_trends = MagicMock(return_value="Market Trends Analysis")
        self.marketing_team.analytics_agent.analyze_target_audience = MagicMock(return_value="Target Audience Analysis")
        self.marketing_team.synthesize_plan = MagicMock(return_value="Final Marketing Plan")

        # Test the discuss_marketing_plan method
        product = "Test Product"
        additional_info = {'language': 'english'}
        self.marketing_team.discuss_marketing_plan(product, additional_info)

        # Assert that all methods were called with correct arguments
        self.marketing_team.marketing_agent.generate_campaign_idea.assert_any_call(product, additional_info=additional_info)
        self.marketing_team.marketing_agent.generate_campaign_idea.assert_any_call(product, additional_info="Sales Feedback\nMarket Trends Analysis\nTarget Audience Analysis")
        self.marketing_team.sales_agent.respond_to_agent.assert_called_with("Marketing Campaign Idea", language='english')
        self.marketing_team.strategy_agent.analyze_market_trends.assert_called_with(product, "Marketing Campaign Idea\nSales Feedback", language='english')
        self.marketing_team.analytics_agent.analyze_target_audience.assert_called_with(product, "Marketing Campaign Idea\nSales Feedback\nMarket Trends Analysis", language='english')
        self.marketing_team.marketing_agent.generate_campaign_idea.assert_called_with(product, additional_info="Sales Feedback\nMarket Trends Analysis\nTarget Audience Analysis")
        self.marketing_team.synthesize_plan.assert_called_with("Marketing Campaign Idea", "Sales Feedback", "Market Trends Analysis", "Target Audience Analysis", product, additional_info)

        # Assert that create_styled_document was called with correct arguments
        mock_create_styled_document.assert_called_once()
        call_args = mock_create_styled_document.call_args[0][0]
        self.assertEqual(len(call_args), 6)
        self.assertEqual(call_args[0]['title'], "Initial Marketing Campaign Idea")
        self.assertEqual(call_args[1]['title'], "Sales Agent Feedback")
        self.assertEqual(call_args[2]['title'], "Market Trends Analysis")
        self.assertEqual(call_args[3]['title'], "Target Audience Analysis")
        self.assertEqual(call_args[4]['title'], "Final Marketing Campaign Idea")
        self.assertEqual(call_args[5]['title'], "Final Marketing Plan")

    def test_synthesize_plan(self):
        # Test the synthesize_plan method
        marketing = "Marketing input"
        sales = "Sales input"
        strategy = "Strategy input"
        analytics = "Analytics input"
        product = "Test Product"
        additional_info = {'language': 'english', 'target_audience': 'Young adults', 'marketing_goals': 'Increase brand awareness', 'budget': '$10,000'}

        with patch.object(self.marketing_team.marketing_agent, 'call_openrouter_api', return_value="Synthesized Plan"):
            result = self.marketing_team.synthesize_plan(marketing, sales, strategy, analytics, product, additional_info)

        self.assertEqual(result, "Synthesized Plan")
        self.marketing_team.marketing_agent.call_openrouter_api.assert_called_once_with(unittest.mock.ANY, language='english')
        call_args = self.marketing_team.marketing_agent.call_openrouter_api.call_args[0][0]
        self.assertIn(product, call_args)
        self.assertIn(marketing, call_args)
        self.assertIn(sales, call_args)
        self.assertIn(strategy, call_args)
        self.assertIn(analytics, call_args)
        self.assertIn('Young adults', call_args)
        self.assertIn('Increase brand awareness', call_args)
        self.assertIn('$10,000', call_args)

if __name__ == '__main__':
    unittest.main()
