from collections import Counter


def print_dashboard(frames):
    counter = Counter(f.can_id for f in frames)
    total = len(frames)
    duration = frames[-1].timestamp - frames[0].timestamp

    print("\n" + "=" * 60)
    print("       CAN BUS ANALYZER - DASHBOARD")
    print("=" * 60)
    print(f"  Total frames  : {total}")
    print(f"  Unique IDs    : {len(counter)}")
    print(f"  Duration      : {duration:.3f}s")
    print(f"  Avg frequency : {round(total / duration, 1)} frames/s")
    print("-" * 60)
    print(f"  {'CAN ID':<15} {'Count':>6}  {'Freq':<12} Bar")
    print("-" * 60)

    for can_id, count in counter.most_common():
        bar_len = int((count / total) * 30)
        bar = "#" * bar_len
        freq = round(count / duration, 1)
        print(f"  {can_id:<15} {count:>6}  {str(freq)+' f/s':<12} {bar}")

    print("=" * 60 + "\n")