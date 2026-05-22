import pandas as pd
import os


def frames_to_dataframe(frames):
    return pd.DataFrame([{
        "timestamp": f.timestamp,
        "interface": f.interface,
        "can_id": f.can_id,
        "dlc": f.dlc,
        "data_hex": f.data.hex().upper(),
    } for f in frames])


def export_report(frames, output_path="output/report.csv"):
    os.makedirs("output", exist_ok=True)

    df = frames_to_dataframe(frames)

    stats = df.groupby("can_id").agg(
        count=("timestamp", "count"),
        avg_dlc=("dlc", "mean"),
        first_seen=("timestamp", "min"),
        last_seen=("timestamp", "max"),
    ).reset_index()

    df.to_csv(output_path, index=False)
    stats_path = output_path.replace(".csv", "_stats.csv")
    stats.to_csv(stats_path, index=False)

    print(f"Report exported : {output_path}")
    print(f"Stats exported  : {stats_path}")
    print(f"\n{stats.to_string()}")