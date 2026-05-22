import re
from dataclasses import dataclass
from typing import List


@dataclass
class CANFrame:
    timestamp: float
    interface: str
    can_id: str
    data: bytes
    dlc: int


def parse_log_file(filepath: str) -> List[CANFrame]:
    frames = []
    pattern = r'\((\d+\.\d+)\)\s+(\w+)\s+([0-9A-Fa-f]+)#([0-9A-Fa-f]*)'

    with open(filepath, 'r') as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                ts, iface, can_id, data_hex = match.groups()
                data = bytes.fromhex(data_hex) if data_hex else b''
                frames.append(CANFrame(
                    timestamp=float(ts),
                    interface=iface,
                    can_id=can_id.upper(),
                    data=data,
                    dlc=len(data)
                ))
    return frames


if __name__ == "__main__":
    frames = parse_log_file("data/sample.log")
    print(f"Frames parsed: {len(frames)}")
    for f in frames:
        print(f"  [{f.timestamp:.3f}s] ID={f.can_id} DLC={f.dlc} DATA={f.data.hex().upper()}")