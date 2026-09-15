import pytest
from py_url_normalizer import normalize_url

def test_normalize_url():
    raw = "HTTPS://Example.com:443/shop/?b=2&utm_source=twitter&a=1#section"
    res = normalize_url(raw)
    assert res == "https://example.com/shop?a=1&b=2#section"

def test_strip_fragment():
    res = normalize_url("https://example.com/page#top", strip_fragment=True)
    assert res == "https://example.com/page"
