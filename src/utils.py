# Build: cfcef3db9f19d7c91906574acb0f1e40

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
