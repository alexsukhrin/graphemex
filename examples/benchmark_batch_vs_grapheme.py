import time
import statistics
from typing import Callable, Any
import graphemex
import grapheme
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

def compare_results(batch: dict, py: dict) -> dict:
    return {
        "mean_diff": py["mean"] / batch["mean"],
        "median_diff": py["median"] / batch["median"],
        "min_diff": py["min"] / batch["min"],
        "max_diff": py["max"] / batch["max"]
    }

def print_comparison(name: str, batch: dict, py: dict):
    comparison = compare_results(batch, py)
    table_data = [
        ["Metric", "graphemex (batch)", "grapheme (Python)", "Times Faster"],
        ["Mean", f"{batch['mean']:.3f} ms", f"{py['mean']:.3f} ms", f"{comparison['mean_diff']:.1f}x"],
        ["Median", f"{batch['median']:.3f} ms", f"{py['median']:.3f} ms", f"{comparison['median_diff']:.1f}x"],
        ["Min", f"{batch['min']:.3f} ms", f"{py['min']:.3f} ms", f"{comparison['min_diff']:.1f}x"],
        ["Max", f"{batch['max']:.3f} ms", f"{py['max']:.3f} ms", f"{comparison['max_diff']:.1f}x"],
        ["StdDev", f"{batch['stdev']:.3f} ms", f"{py['stdev']:.3f} ms", "N/A"]
    ]
    print(f"\n=== {name} ===")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

def main():
    print("Running batch vs grapheme (Python) benchmarks...")
    print(f"Each test runs {ITERATIONS} times (batch size: {BATCH_SIZE})\n")
    tests = [
        ("Split", lambda batch: graphemex.batch_split(batch), lambda batch: [list(grapheme.graphemes(t)) for t in batch]),
        ("Grapheme Len", lambda batch: graphemex.batch_grapheme_len(batch), lambda batch: [len(list(grapheme.graphemes(t))) for t in batch]),
    ]
    for batch_name, batch in test_batches:
        for test_name, batch_func, py_func in tests:
            batch_stats = benchmark_function(batch_func, batch)
            py_stats = benchmark_function(py_func, batch)
            print_comparison(f"{test_name}: {batch_name}", batch_stats, py_stats)

if __name__ == "__main__":
    main() 