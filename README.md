# CAN Bus Analyzer

Python tool for parsing, filtering and analyzing CAN bus log files.  
Built as part of an automotive validation engineering portfolio.

## Features

- Parse standard `.log` CAN bus files
- Filter frames by ID, ID range, or timestamp
- Terminal dashboard with frame statistics
- CSV report export with pandas
- Frame frequency analysis

## Project Structure

```
can-bus-analyzer/
├── analyzer/
│   ├── parser.py       # CAN log parser
│   ├── filters.py      # Frame filters and statistics
│   ├── reporter.py     # CSV export with pandas
│   └── dashboard.py    # Terminal dashboard
├── data/
│   └── sample.log      # Sample CAN log file
├── output/             # Generated reports
├── main.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/AMEZOUARm/can-bus-analyzer.git
cd can-bus-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
python main.py data/sample.log
```

## Output Example
```
============================================================
CAN BUS ANALYZER - DASHBOARD
Total frames  : 10
Unique IDs    : 4
Duration      : 0.090s
Avg frequency : 111.1 frames/s
CAN ID          Count  Freq         Bar
0CF11E0F            3  33.3 f/s     ##########
18FEF100            3  33.3 f/s     ##########
0CF00400            2  22.2 f/s     ######
18F00503            2  22.2 f/s     ######
```
## Stack

- Python 3.x
- python-can
- pandas
- matplotlib

## Author

Mohamed AMEZOUAR - Automotive Validation Engineer  
[GitHub Profile](https://github.com/AMEZOUARm)
