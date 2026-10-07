def interval_merge(intervals):
    """
    Merge overlapping intervals.
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        Last = merged[-1]
        if current[0] <= Last[-1]:
            Last[-1] = max(Last[-1], current[-1])
        else:
            merged.append(current)
    return merged