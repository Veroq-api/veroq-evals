# VEROQ Evals

Open evaluation suite for financial intelligence APIs. Benchmark accuracy, speed, and coverage across providers.

## What We Test

| Category | Queries | What's Measured |
|----------|---------|-----------------|
| Price accuracy | 50 tickers | Correct price, latency |
| Earnings data | 30 companies | Date accuracy, EPS |
| Claim verification | 100 claims | Verdict accuracy vs ground truth |
| Coverage breadth | 200 tickers | Which providers have data |
| Response time | All queries | p50, p95, p99 latency |

## Run

```bash
pip install veroq
export VEROQ_API_KEY=vq_live_xxx
python eval.py
```

## Results

Results are published in `results/` after each run.

## Contributing

Add test cases to `test_cases/` and submit a PR. We welcome community-contributed evaluation datasets.

## Links

- [VEROQ](https://veroq.ai) | [API Reference](https://veroq.ai/api-reference)
