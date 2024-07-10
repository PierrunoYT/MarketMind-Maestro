import os
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

    def discuss_marketing_plan(self, question):
        print(f"{Fore.CYAN}Marketing Team discussing: {question}{Style.RESET_ALL}\n", flush=True)

        content = []

        product = "jetflame lighters"

        # Marketing Agent's input
        print(f"{Fore.RED}Marketing Agent thinking...", end='', flush=True)
        marketing_input = self.marketing_agent.generate_campaign_idea(product)
        print(f"\r{Fore.RED}Marketing Agent: {marketing_input}{Style.RESET_ALL}\n", flush=True)
        content.append({"title": "Marketing Campaign Idea", "content": marketing_input})

        # Sales Agent's input
        print(f"{Fore.GREEN}Sales Agent thinking...", end='', flush=True)
        sales_input = self.sales_agent.generate_sales_pitch(product)
        print(f"\r{Fore.GREEN}Sales Agent: {sales_input}{Style.RESET_ALL}\n", flush=True)
        content.append({"title": "Sales Pitch", "content": sales_input})

        # Strategy Agent's input
        print(f"{Fore.YELLOW}Strategy Agent thinking...", end='', flush=True)
        strategy_input = self.strategy_agent.analyze_market_trends(product)
        print(f"\r{Fore.YELLOW}Strategy Agent: {strategy_input}{Style.RESET_ALL}\n", flush=True)
        content.append({"title": "Market Trends Analysis", "content": strategy_input})

        # Analytics Agent's input
        print(f"{Fore.MAGENTA}Analytics Agent thinking...", end='', flush=True)
        analytics_input = self.analytics_agent.suggest_target_audience(product)
        print(f"\r{Fore.MAGENTA}Analytics Agent: {analytics_input}{Style.RESET_ALL}\n", flush=True)
        content.append({"title": "Target Audience Suggestion", "content": analytics_input})

        # Final plan synthesis
        print(f"{Fore.BLUE}Synthesizing final plan...", end='', flush=True)
        final_plan = self.synthesize_plan(marketing_input, sales_input, strategy_input, analytics_input, product)
        print(f"\r{Fore.BLUE}Final Marketing Plan:\n{final_plan}{Style.RESET_ALL}", flush=True)
        content.append({"title": "Final Marketing Plan", "content": final_plan})

        # Create styled Word document
        create_styled_document(content)

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
    question = input("Enter your marketing question: ")
    team.discuss_marketing_plan(question)

if __name__ == "__main__":
    main()
