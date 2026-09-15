from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from typing import Set

TRACKING_PARAMS: Set[str] = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "msclkid", "mc_eid", "ref", "source"
}

def normalize_url(
    url: str,
    strip_tracking: bool = True,
    strip_fragment: bool = False,
    sort_query: bool = True,
) -> str:
    """Normalize and canonicalize a URL string."""
    if not url:
        return ""

    parts = urlsplit(url.strip())
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()

    # Remove default ports
    if scheme == "http" and netloc.endswith(":80"):
        netloc = netloc[:-3]
    elif scheme == "https" and netloc.endswith(":443"):
        netloc = netloc[:-4]

    # Path normalization
    path = parts.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]

    # Query string normalization
    query_pairs = parse_qsl(parts.query, keep_blank_values=True)
    if strip_tracking:
        query_pairs = [(k, v) for k, v in query_pairs if k.lower() not in TRACKING_PARAMS]

    if sort_query:
        query_pairs = sorted(query_pairs, key=lambda x: x[0])

    normalized_query = urlencode(query_pairs)
    fragment = "" if strip_fragment else parts.fragment

    return urlunsplit((scheme, netloc, path, normalized_query, fragment))
