# Advanced Marketing and Sales AI Agents

This project implements advanced Marketing and Sales AI Agents using OpenRouter's Anthropic Claude-3.5-sonnet model. The agents provide various marketing and sales-related functionalities to assist in campaign planning, market analysis, sales strategies, and strategic decision-making.

## Features

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

## Requirements

- Python 3.6+
- `requests` library
- OpenRouter API key

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install requests
   ```
3. Set up your OpenRouter API key as an environment variable:
   ```
   export OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the main scripts to see demonstrations of the AI Agents' capabilities:

```
python marketing_ai_agent.py
python sales_ai_agent.py
```

## Customization

You can easily extend the `MarketingAIAgent` and `SalesAIAgent` classes to add more functionalities or modify existing ones. The `call_openrouter_api` method can be used to make custom queries to the AI model.

## Note

Ensure you have a valid OpenRouter API key and sufficient credits to make API calls. The scripts will display an error message if the API key is not set or if there are issues with the API call.

## License

This project is open-source and available under the MIT License.
