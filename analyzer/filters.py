from typing import List


class CANFrame:
    pass


try:
    from analyzer.parser import CANFrame
except ImportError:
    pass


def filter_by_id(frames, can_id):
    return [f for f in frames if f.can_id == can_id.upper()]


def filter_by_id_range(frames, id_min, id_max):
    min_val = int(id_min, 16)
    max_val = int(id_max, 16)
    return [f for f in frames if min_val <= int(f.can_id, 16) <= max_val]


def filter_by_time(frames, t_start, t_end):
    return [f for f in frames if t_start <= f.timestamp <= t_end]


def get_statistics(frames):
    if not frames:
        return {}
    ids = [f.can_id for f in frames]
    return {
        "total_frames": len(frames),
        "unique_ids": len(set(ids)),
        "most_frequent_id": max(set(ids), key=ids.count),
        "duration_s": round(frames[-1].timestamp - frames[0].timestamp, 3),
    }