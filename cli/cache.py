import os
from joblib import Memory

CACHE_ROOT = os.path.join(os.path.dirname(__file__), '.cache')
os.makedirs(CACHE_ROOT, exist_ok=True)

def get_cache(name: str) -> Memory:
    """Return a Memory cache located under the cli cache root."""
    path = os.path.join(CACHE_ROOT, name)
    return Memory(cachedir=path, verbose=0)

