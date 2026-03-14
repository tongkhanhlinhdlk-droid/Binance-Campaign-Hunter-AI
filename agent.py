def ai_agent(question):
    q = question.lower()

    if "campaign" in q:
        return """
Latest Binance Campaigns

1. Launchpool Event
Reward: Token rewards

2. Trading Competition
Reward: USDT prize pool
"""

    if "reward" in q:
        return "Many Binance campaigns offer token rewards or USDT prizes."

    return "Ask me about Binance campaigns."

while True:
    user = input("You: ")
    print("AI:", ai_agent(user))
