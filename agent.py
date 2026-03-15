from tools import get_campaigns

def ai_agent(question):

    q = question.lower()

    if "campaign" in q:
        return get_campaigns()

    if "reward" in q:
        return "Many Binance campaigns offer token rewards or USDT prizes."

    return """
You can ask things like:

Find Binance campaigns
Show campaign rewards
"""