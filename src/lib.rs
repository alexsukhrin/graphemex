use pyo3::prelude::*;
use pyo3::exceptions;
use unicode_segmentation::UnicodeSegmentation;
use rayon::prelude::*;


/// Splits text into grapheme clusters.
/// 
/// Returns a list of strings, where each string is a single grapheme cluster.
#[pyfunction]
fn split(text: &str) -> Vec<&str> {
    UnicodeSegmentation::graphemes(text, true).collect()
}

/// Returns the count of grapheme clusters in the string.
/// 
/// This function properly handles Unicode strings including emoji 
/// and complex character combinations.
#[pyfunction]
fn grapheme_len(text: &str) -> usize {
    UnicodeSegmentation::graphemes(text, true).count()
}

/// Extracts a substring using grapheme cluster indices.
/// 
/// Args:
///     text: The input string to slice
///     start: Starting index (inclusive)
///     end: Ending index (exclusive)
/// 
/// Returns:
///     A new string containing the specified range of grapheme clusters
/// 
/// Raises:
///     ValueError: If start or end indices are out of bounds
#[pyfunction]
fn slice(text: &str, start: usize, end: usize) -> PyResult<String> {
    let graphemes: Vec<&str> = UnicodeSegmentation::graphemes(text, true).collect();
    if start > end || end > graphemes.len() {
        return Err(exceptions::PyValueError::new_err("Invalid start or end indices"));
    }
    Ok(graphemes[start..end].concat())
}

/// Truncates string to specified maximum number of grapheme clusters.
/// 
/// Args:
///     text: The input string to truncate
///     max_len: Maximum number of grapheme clusters to keep
/// 
/// Returns:
///     A new string containing at most max_len grapheme clusters
#[pyfunction]
fn truncate(text: &str, max_len: usize) -> String {
    let graphemes: Vec<&str> = UnicodeSegmentation::graphemes(text, true).collect();
    let truncated = if max_len >= graphemes.len() {
        graphemes
    } else {
        graphemes[..max_len].to_vec()
    };
    truncated.concat()
}

// Batch операції
#[pyfunction]
fn batch_split(texts: Vec<String>) -> Vec<Vec<String>> {
    texts.par_iter()
        .map(|text| {
            UnicodeSegmentation::graphemes(text.as_str(), true)
                .map(String::from)
                .collect()
        })
        .collect()
}

#[pyfunction]
fn batch_grapheme_len(texts: Vec<String>) -> Vec<usize> {
    texts.par_iter()
        .map(|text| UnicodeSegmentation::graphemes(text.as_str(), true).count())
        .collect()
}

#[pyfunction]
fn batch_slice(texts: Vec<String>, start: usize, end: usize) -> PyResult<Vec<String>> {
    let results: Result<Vec<String>, _> = texts.par_iter()
        .map(|text| {
            let graphemes: Vec<&str> = UnicodeSegmentation::graphemes(text.as_str(), true).collect();
            if start > end || end > graphemes.len() {
                Err(exceptions::PyValueError::new_err("Invalid start or end indices"))
            } else {
                Ok(graphemes[start..end].concat())
            }
        })
        .collect();

    results
}

#[pyfunction]
fn batch_truncate(texts: Vec<String>, max_len: usize) -> Vec<String> {
    texts.par_iter()
        .map(|text| {
            let graphemes: Vec<&str> = UnicodeSegmentation::graphemes(text.as_str(), true).collect();
            let truncated = if max_len >= graphemes.len() {
                graphemes
            } else {
                graphemes[..max_len].to_vec()
            };
            truncated.concat()
        })
        .collect()
}

/// A Python module for Unicode grapheme cluster operations.
/// 
/// This module provides functions for working with grapheme clusters,
/// which are user-perceived characters in Unicode text.
#[pymodule]
fn graphemex(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // single
    m.add_function(wrap_pyfunction!(split, m)?)?;
    m.add_function(wrap_pyfunction!(grapheme_len, m)?)?;
    m.add_function(wrap_pyfunction!(slice, m)?)?;
    m.add_function(wrap_pyfunction!(truncate, m)?)?;

    // batch
    m.add_function(wrap_pyfunction!(batch_split, m)?)?;
    m.add_function(wrap_pyfunction!(batch_grapheme_len, m)?)?;
    m.add_function(wrap_pyfunction!(batch_slice, m)?)?;
    m.add_function(wrap_pyfunction!(batch_truncate, m)?)?;
    
    Ok(())
}