# MarketMind Maestro: Advanced Marketing and Sales AI Team

This project implements an advanced Marketing and Sales AI Team using OpenRouter's Anthropic Claude-3.5-sonnet model. The team consists of multiple AI agents that collaborate to create comprehensive marketing plans based on user input.

## Features

### Marketing Team
- Coordinate discussions between multiple AI agents
- Generate comprehensive marketing plans based on input from all agents
- Create styled Word documents with the final marketing plan

### Marketing AI Agent
- Generate detailed marketing campaign ideas
- Analyze current market trends
- Suggest target audiences for campaigns
- Perform sentiment analysis on text
- Conduct competitor analysis
- Suggest budget allocation for marketing channels

### Sales AI Agent
- Generate compelling sales pitches
- Handle various types of sales objections
- Suggest follow-up strategies
- Analyze sales performance data

### Strategy AI Agent
- Provide strategic insights and market analysis
- Analyze market trends and their impact on the product
- Offer recommendations for leveraging trends and mitigating risks

### Analytics AI Agent
- Conduct in-depth target audience analysis
- Provide detailed demographic and psychographic profiles
- Analyze behavioral patterns and decision-making processes
- Suggest tailored messaging strategies for different audience segments

## New Features
- Multi-language support (English and German)
- Interactive command-line interface with colorful output
- Progress indicators for each AI agent's thinking process
- Styled Word document output with custom formatting

## Requirements

- Python 3.6+
- OpenRouter API key

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/PierrunoYT/MarketMind-Maestro.git
   ```
2. Navigate to the project directory:
   ```
   cd MarketMind-Maestro
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
6. Create a `.env` file in the project root directory and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the main script to interact with the Marketing AI Team:

```
python marketing_team.py
```

Follow the prompts to enter your product information, additional context, and preferred language. The AI team will collaborate to create a comprehensive marketing plan and save it as a styled Word document.

## Customization

You can easily extend the `MarketingAIAgent`, `SalesAIAgent`, `StrategyAIAgent`, `AnalyticsAIAgent`, and `MarketingTeam` classes to add more functionalities or modify existing ones. The `call_openrouter_api` method can be used to make custom queries to the AI model.

## Testing

Unit tests are provided in the `test_marketing_team.py` file. Run the tests using:

```
python -m unittest test_marketing_team.py
```

## Note

Ensure you have a valid OpenRouter API key and sufficient credits to make API calls. The scripts will display an error message if the API key is not set or if there are issues with the API call.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Links

- [GitHub Repository](https://github.com/PierrunoYT/MarketMind-Maestro)
- [Issue Tracker](https://github.com/PierrunoYT/MarketMind-Maestro/issues)
- [Documentation](https://github.com/PierrunoYT/MarketMind-Maestro/wiki)
