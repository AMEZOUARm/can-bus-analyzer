import sys
from analyzer.parser import parse_log_file
from analyzer.filters import filter_by_id, filter_by_id_range, filter_by_time, get_statistics
from analyzer.reporter import export_report
from analyzer.dashboard import print_dashboard


def main():
    log_file = sys.argv[1] if len(sys.argv) > 1 else "data/sample.log"

    print(f"Loading: {log_file}")
    frames = parse_log_file(log_file)

    if not frames:
        print("No frames found in file.")
        return

    print_dashboard(frames)

    stats = get_statistics(frames)
    print("Global stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    export_report(frames)


if __name__ == "__main__":
    main()