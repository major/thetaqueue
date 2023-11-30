# Enqueue trades from thetagang.com for processing.
import requests


def run() -> str:
    """Main function for enqueueing trades."""
    # resp = requests.get("https://api3.thetagang.com/trades", timeout=10)

    # if resp.status_code != 200:
    #     raise Exception(f"GET /api/trades {resp.status_code}")

    # trades = next(x["guid"] for x in resp.json()["data"])
    # return trades
    return ["test"]
