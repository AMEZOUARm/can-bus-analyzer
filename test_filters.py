import sys
sys.path.insert(0, '.')

from analyzer.parser import parse_log_file
from analyzer.filters import filter_by_id, filter_by_id_range, filter_by_time, get_statistics

frames = parse_log_file("data/sample.log")

filtered = filter_by_id(frames, "0CF11E0F")
print(f"Filtre ID=0CF11E0F : {len(filtered)} trames")

filtered2 = filter_by_id_range(frames, "0CF00000", "0CFFFFFF")
print(f"Filtre plage 0CF... : {len(filtered2)} trames")

filtered3 = filter_by_time(frames, 0.0, 0.05)
print(f"Filtre 0.0s-0.05s  : {len(filtered3)} trames")

stats = get_statistics(frames)
print(f"\nStats globales :")
for k, v in stats.items():
    print(f"  {k}: {v}")

from analyzer.reporter import export_report
export_report(frames)

from analyzer.dashboard import print_dashboard

print_dashboard(frames)