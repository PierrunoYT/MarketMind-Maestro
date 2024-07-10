# Advanced Marketing and Sales AI Team

This project implements an advanced Marketing and Sales AI Team using OpenRouter's Anthropic Claude-3.5-sonnet model. The team consists of multiple AI agents that collaborate to create comprehensive marketing plans based on user input.

## Features

### Marketing Team
- Coordinate discussions between multiple AI agents
- Generate comprehensive marketing plans based on input from all agents

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

### Strategy and Analytics Agents
- Provide strategic insights and market analysis
- Offer data-driven recommendations for marketing campaigns

## Requirements

- Python 3.6+
- OpenRouter API key

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the project root directory and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the main script to interact with the Marketing AI Team:

```
python marketing_team.py
```

Enter your marketing-related question when prompted, and the AI team will collaborate to create a comprehensive marketing plan.

## Customization

You can easily extend the `MarketingAIAgent`, `SalesAIAgent`, and `MarketingTeam` classes to add more functionalities or modify existing ones. The `call_openrouter_api` method can be used to make custom queries to the AI model.

## Note

Ensure you have a valid OpenRouter API key and sufficient credits to make API calls. The scripts will display an error message if the API key is not set or if there are issues with the API call.

## License

This project is open-source and available under the MIT License.
