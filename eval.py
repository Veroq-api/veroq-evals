"""Benchmark VEROQ API — accuracy, speed, coverage."""
import time
import json
from veroq import VeroqClient

client = VeroqClient()

results = {"tests": [], "summary": {}}

# Test 1: Price accuracy
print("=== Price Accuracy ===")
tickers = ["AAPL", "MSFT", "NVDA", "TSLA", "GOOGL", "AMZN", "META", "BTC", "ETH", "GOLD"]
price_times = []
for t in tickers:
    start = time.time()
    r = client.ask(f"{t} price")
    elapsed = (time.time() - start) * 1000
    price_times.append(elapsed)
    price = r.get("data", {}).get("ticker", {}).get("price", {}).get("current")
    print(f"  {t:6s}: ${price or '?':>10} ({elapsed:.0f}ms)")

# Test 2: Verification accuracy
print("\n=== Verification Accuracy ===")
claims = [
    ("The sky is blue", "supported"),
    ("Apple is a tech company", "supported"),
    ("Bitcoin was created by Satoshi Nakamoto", "supported"),
    ("The Earth is flat", "contradicted"),
    ("Unicorns are real animals", "contradicted"),
]
correct = 0
for claim, expected in claims:
    r = client.verify(claim)
    verdict = r.get("verdict", "unknown")
    match = "supported" in verdict if expected == "supported" else "contradict" in verdict
    if match: correct += 1
    print(f"  {'✓' if match else '✗'} \"{claim[:40]}\" → {verdict} (expected: {expected})")

# Summary
print(f"\n=== Summary ===")
print(f"Price queries: {len(tickers)} tickers, avg {sum(price_times)/len(price_times):.0f}ms")
print(f"Verification: {correct}/{len(claims)} correct ({correct/len(claims)*100:.0f}%)")
