import time
import statistics
from typing import Callable, Any
import graphemex
from tabulate import tabulate

BATCH_SIZE = 1000
ITERATIONS = 100

# Test data
simple_text = "Hello, World!" * 100
emoji_text = "👨‍👩‍👧‍👦 Hello 🌍! 😊 " * 50
mixed_text = "привіт 👋 світ 🌍 123 漢字 한글" * 50

test_batches = [
    ("Simple Batch", [simple_text] * BATCH_SIZE),
    ("Emoji Batch", [emoji_text] * BATCH_SIZE),
    ("Mixed Batch", [mixed_text] * BATCH_SIZE),
]

def measure_time(func: Callable, *args: Any) -> float:
    start = time.perf_counter()
    func(*args)
    return (time.perf_counter() - start) * 1000

def benchmark_function(func: Callable, *args: Any, iterations: int = ITERATIONS) -> dict:
    times = [measure_time(func, *args) for _ in range(iterations)]
    return {
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "stdev": statistics.stdev(times),
        "min": min(times),
        "max": max(times)
    }

def compare_results(single: dict, batch: dict) -> dict:
    return {
        "mean_diff": single["mean"] / batch["mean"],
        "median_diff": single["median"] / batch["median"],
        "min_diff": single["min"] / batch["min"],
        "max_diff": single["max"] / batch["max"]
    }

def print_comparison(name: str, single: dict, batch: dict):
    comparison = compare_results(single, batch)
    table_data = [
        ["Metric", "Single (sum)", "Batch", "Speedup"],
        ["Mean", f"{single['mean']:.3f} ms", f"{batch['mean']:.3f} ms", f"{comparison['mean_diff']:.1f}x"],
        ["Median", f"{single['median']:.3f} ms", f"{batch['median']:.3f} ms", f"{comparison['median_diff']:.1f}x"],
        ["Min", f"{single['min']:.3f} ms", f"{batch['min']:.3f} ms", f"{comparison['min_diff']:.1f}x"],
        ["Max", f"{single['max']:.3f} ms", f"{batch['max']:.3f} ms", f"{comparison['max_diff']:.1f}x"],
        ["StdDev", f"{single['stdev']:.3f} ms", f"{batch['stdev']:.3f} ms", "N/A"]
    ]
    print(f"\n=== {name} ===")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

def main():
    print("Running batch vs single benchmarks...")
    print(f"Each test runs {ITERATIONS} times (batch size: {BATCH_SIZE})\n")
    tests = [
        ("Split", lambda batch: [graphemex.split(t) for t in batch], lambda batch: graphemex.batch_split(batch)),
        ("Grapheme Len", lambda batch: [graphemex.grapheme_len(t) for t in batch], lambda batch: graphemex.batch_grapheme_len(batch)),
    ]
    for batch_name, batch in test_batches:
        for test_name, single_func, batch_func in tests:
            single_stats = benchmark_function(single_func, batch)
            batch_stats = benchmark_function(batch_func, batch)
            print_comparison(f"{test_name}: {batch_name}", single_stats, batch_stats)

if __name__ == "__main__":
    main() 