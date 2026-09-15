# py-url-normalizer

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-url-normalizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency URL canonicalizer for Python: strips UTM tracking parameters, sorts query params, and normalizes hostnames.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library (`urllib.parse`).
- 🧹 **Strip Tracking Parameters**: Removes `utm_source`, `utm_medium`, `fbclid`, `gclid`, and `ref`.
- 🔀 **Deterministic Canonical URLs**: Sorts query string keys for optimal cache hit ratios and deduplication.

---

## 📦 Installation

```bash
pip install py-url-normalizer
```

---

## 🛠️ Quickstart

```python
from py_url_normalizer import normalize_url

raw = "https://EXAMPLE.COM:443/products/?b=2&utm_source=twitter&a=1#section"
clean = normalize_url(raw, strip_tracking=True)
print(clean)
# Output: https://example.com/products?a=1&b=2#section
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library simplified your URL deduplication, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
