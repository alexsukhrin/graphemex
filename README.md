# graphemex

[![GitHub](https://img.shields.io/badge/GitHub-graphemex-blue)](https://github.com/alexsukhrin/graphemex)
[![PyPI](https://img.shields.io/pypi/v/graphemex)](https://pypi.org/project/graphemex/)

Fast Unicode grapheme cluster segmentation library written in Rust using PyO3.

## About

`graphemex` is a high-performance Python library for Unicode grapheme cluster handling, powered by Rust. It provides correct and efficient text segmentation according to Unicode standards, which is essential for proper text processing in many applications.

## Key Benefits

- 🚀 **High Performance**: Implemented in Rust for maximum speed
- 🌍 **Unicode Correctness**: Properly handles all Unicode grapheme clusters
- 🔧 **Simple API**: Just 4 intuitive functions for common text operations
- 💻 **Cross-Platform**: Works on all major operating systems
- 🐍 **Python Friendly**: Seamless Python integration via PyO3
- 🛠 **Zero Dependencies**: Only requires Python standard library at runtime

## Features

### Single Operations
* `split(text: str) -> List[str]`: Splits text into grapheme clusters
* `grapheme_len(text: str) -> int`: Returns the number of grapheme clusters in the string
* `slice(text: str, start: int, end: int) -> str`: Extracts a substring by grapheme cluster indices
* `truncate(text: str, max_len: int) -> str`: Truncates string to specified maximum number of grapheme clusters

### Batch Operations
* `batch_split(texts: List[str]) -> List[List[str]]`: Splits multiple texts into grapheme clusters
* `batch_grapheme_len(texts: List[str]) -> List[int]`: Returns the number of grapheme clusters for multiple strings
* `batch_slice(texts: List[str], start: int, end: int) -> List[str]`: Extracts substrings by grapheme cluster indices for multiple strings
* `batch_truncate(texts: List[str], max_len: int) -> List[str]`: Truncates multiple strings to specified maximum number of grapheme clusters

## Installation

## Use Cases

- Text editors and IDEs
- Input validation and processing
- Social media character counting
- Text truncation for UI elements
- Natural language processing
- Data cleaning and normalization

## Performance

`graphemex` is significantly faster than pure Python implementations:
- Up to 227.6x faster for batch operations
- Up to 62.9x faster for single operations
- Minimal memory overhead
- Efficient handling of large texts

### Batch vs Python Performance

Running batch vs grapheme (Python) benchmarks...
Each test runs 100 times (batch size: 1000)

#### Split: Simple Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 65.897 ms         | 348.297 ms        | 5.3x         |
| Median | 64.438 ms         | 347.191 ms        | 5.4x         |
| Min    | 58.534 ms         | 343.628 ms        | 5.9x         |
| Max    | 109.630 ms        | 406.835 ms        | 3.7x         |
| StdDev | 6.734 ms          | 6.405 ms          | N/A          |

#### Grapheme Len: Simple Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 4.531 ms          | 345.278 ms        | 76.2x        |
| Median | 4.492 ms          | 345.251 ms        | 76.9x        |
| Min    | 4.326 ms          | 340.078 ms        | 78.6x        |
| Max    | 5.490 ms          | 350.240 ms        | 63.8x        |
| StdDev | 0.194 ms          | 1.695 ms          | N/A          |

#### Split: Emoji Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 44.512 ms         | 878.896 ms        | 19.7x        |
| Median | 44.512 ms         | 878.877 ms        | 19.7x        |
| Min    | 43.058 ms         | 873.524 ms        | 20.3x        |
| Max    | 47.180 ms         | 914.023 ms        | 19.4x        |
| StdDev | 0.583 ms          | 4.161 ms          | N/A          |

#### Grapheme Len: Emoji Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 5.207 ms          | 872.983 ms        | 167.7x       |
| Median | 5.175 ms          | 872.254 ms        | 168.5x       |
| Min    | 5.046 ms          | 869.192 ms        | 172.3x       |
| Max    | 5.965 ms          | 912.559 ms        | 153.0x       |
| StdDev | 0.141 ms          | 4.485 ms          | N/A          |

#### Split: Mixed Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 110.419 ms        | 1481.557 ms       | 13.4x        |
| Median | 109.929 ms        | 1476.163 ms       | 13.4x        |
| Min    | 106.516 ms        | 1468.433 ms       | 13.8x        |
| Max    | 137.677 ms        | 1540.124 ms       | 11.2x        |
| StdDev | 3.572 ms          | 15.597 ms         | N/A          |

#### Grapheme Len: Mixed Batch
| Metric | graphemex (batch) | grapheme (Python) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 6.440 ms          | 1465.842 ms       | 227.6x       |
| Median | 6.393 ms          | 1459.345 ms       | 228.3x       |
| Min    | 6.234 ms          | 1456.319 ms       | 233.6x       |
| Max    | 7.144 ms          | 1543.400 ms       | 216.0x       |
| StdDev | 0.161 ms          | 17.820 ms         | N/A          |

### Single Operations Performance

Comparing graphemex (Rust) vs grapheme (Python)

#### Simple Text - Split
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.291 ms         | 3.403 ms          | 11.7x        |
| Median | 0.271 ms         | 3.397 ms          | 12.5x        |
| Min    | 0.265 ms         | 3.309 ms          | 12.5x        |
| Max    | 0.733 ms         | 3.633 ms          | 5.0x         |
| StdDev | 0.058 ms         | 0.032 ms          | N/A          |

#### Emoji Text - Split
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.297 ms         | 8.502 ms          | 28.6x        |
| Median | 0.294 ms         | 8.488 ms          | 28.9x        |
| Min    | 0.291 ms         | 8.444 ms          | 29.1x        |
| Max    | 0.557 ms         | 9.024 ms          | 16.2x        |
| StdDev | 0.014 ms         | 0.056 ms          | N/A          |

#### Mixed Text - Split
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.617 ms         | 14.093 ms         | 22.8x        |
| Median | 0.615 ms         | 14.064 ms         | 22.9x        |
| Min    | 0.610 ms         | 14.004 ms         | 23.0x        |
| Max    | 0.750 ms         | 14.763 ms         | 19.7x        |
| StdDev | 0.009 ms         | 0.091 ms          | N/A          |

#### Simple Text - Length
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.193 ms         | 3.442 ms          | 17.9x        |
| Median | 0.191 ms         | 3.427 ms          | 17.9x        |
| Min    | 0.191 ms         | 3.364 ms          | 17.6x        |
| Max    | 0.245 ms         | 4.278 ms          | 17.5x        |
| StdDev | 0.005 ms         | 0.064 ms          | N/A          |

#### Emoji Text - Length
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.186 ms         | 8.551 ms          | 46.0x        |
| Median | 0.184 ms         | 8.515 ms          | 46.2x        |
| Min    | 0.183 ms         | 8.474 ms          | 46.2x        |
| Max    | 0.254 ms         | 8.977 ms          | 35.3x        |
| StdDev | 0.005 ms         | 0.077 ms          | N/A          |

#### Mixed Text - Length
| Metric | graphemex (Rust) | grapheme (Python) | Times Faster |
|--------|------------------|-------------------|--------------|
| Mean   | 0.225 ms         | 14.178 ms         | 62.9x        |
| Median | 0.224 ms         | 14.113 ms         | 63.1x        |
| Min    | 0.223 ms         | 14.012 ms         | 62.7x        |
| Max    | 0.337 ms         | 14.954 ms         | 44.4x        |
| StdDev | 0.006 ms         | 0.137 ms          | N/A          |

### Batch vs Single Performance

Running batch vs single benchmarks...
Each test runs 100 times (batch size: 1000)

#### Split: Simple Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.291 ms          | 65.897 ms         | 0.004x       |
| Median | 0.271 ms          | 64.438 ms         | 0.004x       |
| Min    | 0.265 ms          | 58.534 ms         | 0.005x       |
| Max    | 0.733 ms          | 109.630 ms        | 0.007x       |
| StdDev | 0.058 ms          | 6.734 ms          | N/A          |

#### Grapheme Len: Simple Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.193 ms          | 4.531 ms          | 0.043x       |
| Median | 0.191 ms          | 4.492 ms          | 0.043x       |
| Min    | 0.191 ms          | 4.326 ms          | 0.044x       |
| Max    | 0.245 ms          | 5.490 ms          | 0.045x       |
| StdDev | 0.005 ms          | 0.194 ms          | N/A          |

#### Split: Emoji Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.297 ms          | 44.512 ms         | 0.007x       |
| Median | 0.294 ms          | 44.512 ms         | 0.007x       |
| Min    | 0.291 ms          | 43.058 ms         | 0.007x       |
| Max    | 0.557 ms          | 47.180 ms         | 0.012x       |
| StdDev | 0.014 ms          | 0.583 ms          | N/A          |

#### Grapheme Len: Emoji Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.186 ms          | 5.207 ms          | 0.036x       |
| Median | 0.184 ms          | 5.175 ms          | 0.036x       |
| Min    | 0.183 ms          | 5.046 ms          | 0.036x       |
| Max    | 0.254 ms          | 5.965 ms          | 0.043x       |
| StdDev | 0.005 ms          | 0.141 ms          | N/A          |

#### Split: Mixed Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.617 ms          | 110.419 ms        | 0.006x       |
| Median | 0.615 ms          | 109.929 ms        | 0.006x       |
| Min    | 0.610 ms          | 106.516 ms        | 0.006x       |
| Max    | 0.750 ms          | 137.677 ms        | 0.005x       |
| StdDev | 0.009 ms          | 3.572 ms          | N/A          |

#### Grapheme Len: Mixed Batch
| Metric | graphemex (single) | graphemex (batch) | Times Faster |
|--------|-------------------|-------------------|--------------|
| Mean   | 0.225 ms          | 6.440 ms          | 0.035x       |
| Median | 0.224 ms          | 6.393 ms          | 0.035x       |
| Min    | 0.223 ms          | 6.234 ms          | 0.036x       |
| Max    | 0.337 ms          | 7.144 ms          | 0.047x       |
| StdDev | 0.006 ms          | 0.161 ms          | N/A          |

## Requirements

- Python ≥3.7
- No additional runtime dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Alexandr Sukhryn (alexandrvirtual@gmail.com)