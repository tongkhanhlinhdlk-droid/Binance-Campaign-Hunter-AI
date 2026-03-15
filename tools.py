def get_campaigns():

    campaigns = [
        {
            "name": "Binance Launchpool",
            "reward": "Token rewards"
        },
        {
            "name": "Trading Competition",
            "reward": "USDT prizes"
        }
    ]

    result = "Latest Binance Campaigns:\n"

    for c in campaigns:
        result += f"\n{c['name']} — Reward: {c['reward']}"

    return result