import graphemex
from typing import List, Tuple

def run_test_case(test_func: callable, input_data: str, expected: any) -> Tuple[bool, str]:
    """Runs a test case and returns result and message."""
    try:
        result = test_func(input_data)
        success = result == expected
        message = "OK" if success else f"Error: expected {expected}, got {result}"
        return success, message
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

def test_all():
    test_cases: List[Tuple[str, callable, str, any]] = [
        # Tests for split()
        ("Simple text split",
         graphemex.split,
         "Hello",
         ["H", "e", "l", "l", "o"]),

        ("Emoji split",
         graphemex.split,
         "👨‍👩‍👧‍👦👋",
         ["👨‍👩‍👧‍👦", "👋"]),

        # Tests for grapheme_len()
        ("Simple text length",
         graphemex.grapheme_len,
         "Hello",
         5),

        ("Emoji length",
         graphemex.grapheme_len,
         "👨‍👩‍👧‍👦 Hello 🌍!",
         10),

        # Tests for complex cases
        ("Mixed text length",
         graphemex.grapheme_len,
         "привіт 👋 світ 🌍 123 漢字 한글",
         19),

        ("Diacritical marks",
         graphemex.split,
         "é",
         ["é"]),
    ]

    print("Running tests...\n")

    passed = 0
    failed = 0

    for test_name, func, input_data, expected in test_cases:
        success, message = run_test_case(func, input_data, expected)

        if success:
            passed += 1
            status = "✅"
        else:
            failed += 1
            status = "❌"

        print(f"{status} {test_name}")
        if not success:
            print(f"   {message}")

    print(f"\nResults:")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {passed + failed}")

if __name__ == "__main__":
    test_all()