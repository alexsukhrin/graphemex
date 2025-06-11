import time
import statistics
from typing import Callable, Any
import graphemex
import grapheme
from tabulate import tabulate

def measure_time(func: Callable, *args: Any) -> float:
    """Measures function execution time in milliseconds."""
    start = time.perf_counter()
    func(*args)
    return (time.perf_counter() - start) * 1000

def benchmark_function(func: Callable, *args: Any, iterations: int = 1000) -> dict:
    """Runs benchmark multiple times and returns statistics."""
    times = []
    for _ in range(iterations):
        times.append(measure_time(func, *args))

    return {
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "stdev": statistics.stdev(times),
        "min": min(times),
        "max": max(times)
    }

def compare_results(rust_results: dict, python_results: dict) -> dict:
    """Compares results and calculates performance difference."""
    return {
        "mean_diff": python_results["mean"] / rust_results["mean"],
        "median_diff": python_results["median"] / rust_results["median"],
        "min_diff": python_results["min"] / rust_results["min"],
        "max_diff": python_results["max"] / rust_results["max"]
    }

def print_comparison(name: str, rust_results: dict, python_results: dict):
    """Prints detailed comparison of results."""
    comparison = compare_results(rust_results, python_results)
    
    table_data = [
        ["Metric", "graphemex (Rust)", "grapheme (Python)", "Times Faster"],
        ["Mean", f"{rust_results['mean']:.3f} ms", f"{python_results['mean']:.3f} ms", f"{comparison['mean_diff']:.1f}x"],
        ["Median", f"{rust_results['median']:.3f} ms", f"{python_results['median']:.3f} ms", f"{comparison['median_diff']:.1f}x"],
        ["Min", f"{rust_results['min']:.3f} ms", f"{python_results['min']:.3f} ms", f"{comparison['min_diff']:.1f}x"],
        ["Max", f"{rust_results['max']:.3f} ms", f"{python_results['max']:.3f} ms", f"{comparison['max_diff']:.1f}x"],
        ["StdDev", f"{rust_results['stdev']:.3f} ms", f"{python_results['stdev']:.3f} ms", "N/A"]
    ]
    
    print(f"\n=== {name} ===")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

def main():
    # Test strings of varying complexity
    simple_text = "Hello, World!" * 1000
    emoji_text = "👨‍👩‍👧‍👦 Hello 🌍! 😊 " * 500
    mixed_text = "привіт 👋 світ 🌍 123 漢字 한글" * 500

    test_cases = [
        ("Simple Text - Split", 
         lambda: graphemex.split(simple_text),
         lambda: list(grapheme.graphemes(simple_text))),
        
        ("Emoji Text - Split",
         lambda: graphemex.split(emoji_text),
         lambda: list(grapheme.graphemes(emoji_text))),
        
        ("Mixed Text - Split",
         lambda: graphemex.split(mixed_text),
         lambda: list(grapheme.graphemes(mixed_text))),

        ("Simple Text - Length",
         lambda: graphemex.grapheme_len(simple_text),
         lambda: len(list(grapheme.graphemes(simple_text)))),
        
        ("Emoji Text - Length",
         lambda: graphemex.grapheme_len(emoji_text),
         lambda: len(list(grapheme.graphemes(emoji_text)))),
        
        ("Mixed Text - Length",
         lambda: graphemex.grapheme_len(mixed_text),
         lambda: len(list(grapheme.graphemes(mixed_text))))
    ]

    print("Running benchmarks...")
    print("Each test runs 1000 times")
    print("Comparing graphemex (Rust) vs grapheme (Python)\n")

    for name, rust_func, python_func in test_cases:
        rust_results = benchmark_function(rust_func)
        python_results = benchmark_function(python_func)
        print_comparison(name, rust_results, python_results)

if __name__ == "__main__":
    main()