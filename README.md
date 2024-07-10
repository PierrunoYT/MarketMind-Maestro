# Advanced Marketing AI Agent

This project implements an advanced Marketing AI Agent using OpenRouter's Anthropic Claude-3.5-sonnet model. The agent provides various marketing-related functionalities to assist in campaign planning, market analysis, and strategic decision-making.

## Features

- Generate detailed marketing campaign ideas
- Analyze current market trends
- Suggest target audiences for campaigns
- Perform sentiment analysis on text
- Conduct competitor analysis
- Suggest budget allocation for marketing channels

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

Run the main script to see a demonstration of the Marketing AI Agent's capabilities:

```
python marketing_ai_agent.py
```

## Customization

You can easily extend the `MarketingAIAgent` class to add more functionalities or modify existing ones. The `call_openrouter_api` method can be used to make custom queries to the AI model.

## Note

Ensure you have a valid OpenRouter API key and sufficient credits to make API calls. The script will display an error message if the API key is not set or if there are issues with the API call.

## License

This project is open-source and available under the MIT License.
