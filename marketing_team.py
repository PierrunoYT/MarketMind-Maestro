import os
import json
import logging
from dotenv import load_dotenv
from marketing_ai_agent import MarketingAIAgent
from sales_ai_agent import SalesAIAgent
from strategy_ai_agent import StrategyAIAgent
from analytics_ai_agent import AnalyticsAIAgent
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_styled_document(content):
    doc = Document()
    
    # Create and apply styles
    if 'Title' not in doc.styles:
        title_style = doc.styles.add_style('Title', WD_STYLE_TYPE.PARAGRAPH)
        title_style.font.size = Pt(18)
        title_style.font.bold = True
    else:
        title_style = doc.styles['Title']
    
    if 'Heading' not in doc.styles:
        heading_style = doc.styles.add_style('Heading', WD_STYLE_TYPE.PARAGRAPH)
        heading_style.font.size = Pt(14)
        heading_style.font.bold = True
    else:
        heading_style = doc.styles['Heading']
    
    if 'Body' not in doc.styles:
        body_style = doc.styles.add_style('Body', WD_STYLE_TYPE.PARAGRAPH)
        body_style.font.size = Pt(11)
    else:
        body_style = doc.styles['Body']
    
    # Add content to the document
    doc.add_paragraph("Marketing Team Discussion", style='Title')
    
    for section in content:
        doc.add_paragraph(section['title'], style='Heading')
        doc.add_paragraph(section['content'], style='Body')
    
    # Save the document
    doc.save('marketing_plan.docx')
    print("Marketing plan saved as 'marketing_plan.docx'")

def check_api_key():
    api_key = os.getenv("OPENROUTER_API_KEY")
    print(f"Current API key value: {api_key}")
    if not api_key or api_key.strip() == "":
        print("OpenRouter API key not found or empty in environment variables.")
        new_key = input("Please enter your OpenRouter API key: ").strip()
        if new_key:
            with open(".env", "w") as env_file:
                env_file.write(f"OPENROUTER_API_KEY={new_key}")
            print("API key has been added to .env file.")
            os.environ["OPENROUTER_API_KEY"] = new_key
            api_key = new_key
        else:
            print("No API key provided. Exiting.")
            exit(1)
    return api_key

class MarketingTeam:
    def __init__(self):
        self.marketing_agent = MarketingAIAgent()
        self.sales_agent = SalesAIAgent()
        self.strategy_agent = StrategyAIAgent()
        self.analytics_agent = AnalyticsAIAgent()

    def discuss_marketing_plan(self, product):
        print(f"{Fore.CYAN}Marketing Team discussing: {product}{Style.RESET_ALL}\n", flush=True)
        logging.info(f"Starting marketing plan discussion for {product}")

        content = []

        # Marketing Agent's input
        print(f"{Fore.RED}Marketing Agent: ", end='', flush=True)
        marketing_input = self.marketing_agent.generate_campaign_idea(product)
        logging.debug(f"Marketing Agent response: {marketing_input}")
        content.append({"title": "Marketing Campaign Idea", "content": marketing_input})
        print(f"{Style.RESET_ALL}\n", flush=True)

        # Sales Agent's input
        print(f"{Fore.GREEN}Sales Agent: ", end='', flush=True)
        sales_input = self.sales_agent.generate_sales_pitch(product)
        logging.debug(f"Sales Agent response: {sales_input}")
        content.append({"title": "Sales Pitch", "content": sales_input})
        print(f"{Style.RESET_ALL}\n", flush=True)

        # Strategy Agent's input
        print(f"{Fore.YELLOW}Strategy Agent: ", end='', flush=True)
        strategy_input = self.strategy_agent.analyze_market_trends(product)
        logging.debug(f"Strategy Agent response: {strategy_input}")
        content.append({"title": "Market Trends Analysis", "content": strategy_input})
        print(f"{Style.RESET_ALL}\n", flush=True)

        # Analytics Agent's input
        print(f"{Fore.MAGENTA}Analytics Agent: ", end='', flush=True)
        analytics_input = self.analytics_agent.analyze_target_audience(product)
        logging.debug(f"Analytics Agent response: {analytics_input}")
        content.append({"title": "Target Audience Analysis", "content": analytics_input})
        print(f"{Style.RESET_ALL}\n", flush=True)

        # Final plan synthesis
        print(f"{Fore.BLUE}Synthesizing final plan...\n", flush=True)
        final_plan = self.synthesize_plan(marketing_input, sales_input, strategy_input, analytics_input, product)
        logging.debug(f"Final plan: {final_plan}")
        content.append({"title": "Final Marketing Plan", "content": final_plan})

        # Create styled Word document
        create_styled_document(content)
        logging.info("Marketing plan discussion completed")

    def synthesize_plan(self, marketing, sales, strategy, analytics, product):
        prompt = f"""
        Synthesize a comprehensive marketing plan for {product} based on the following inputs:
        Marketing: {marketing}
        Sales: {sales}
        Strategy: {strategy}
        Analytics: {analytics}

        Provide a cohesive plan that incorporates insights from all agents, specifically tailored for {product}.
        """
        return self.marketing_agent.call_openrouter_api(prompt)

def main():
    api_key = check_api_key()
    os.environ["OPENROUTER_API_KEY"] = api_key
    team = MarketingTeam()
    product = input("Enter the product for the marketing plan (e.g., jet flame lighter or turbo handheld fans): ")
    team.discuss_marketing_plan(product)

if __name__ == "__main__":
    main()
