from typing import List, Tuple


def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.

    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    if k <= 0:
        raise ValueError("Window size k must be > 0")
    if k > len(values):
        return None

    # initial sum of first window
    window_sum = sum(values[:k])
    max_sum = window_sum
    max_index = 0

    # slide window
    for i in range(1, len(values) - k + 1):
        window_sum = window_sum - values[i - 1] + values[i + k - 1]
        if window_sum > max_sum:
            max_sum = window_sum
            max_index = i

    return max_index, max_sum


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return how many length-k windows have average >= target_avg.

    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    if k <= 0:
        raise ValueError("Window size k must be > 0")
    if k > len(values):
        return 0

    target_sum = target_avg * k
    count = 0

    # initial sum
    window_sum = sum(values[:k])
    if window_sum >= target_sum:
        count += 1

    # slide window
    for i in range(1, len(values) - k + 1):
        window_sum = window_sum - values[i - 1] + values[i + k - 1]
        if window_sum >= target_sum:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.

    Empty list -> 0. Single element -> 1.
    """
    if not values:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
