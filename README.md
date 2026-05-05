# 🔍 Network Behavior Analysis & Anomaly Detection System


> A practical cybersecurity project that captures, analyzes, and monitors real-time network traffic using Wireshark and Python — with an integrated rule-based anomaly detection and alerting engine.


---

## 📌 Project Overview

This project models normal network behavior by capturing traffic under controlled scenarios and building an automated analysis pipeline to detect deviations. It demonstrates hands-on skills in network traffic analysis, Python scripting, security monitoring, and documentation — core competencies for roles in cybersecurity, SOC analysis, and network security.

The project is divided into two layers:

- **Manual Analysis** — Using Wireshark to inspect protocol distribution, IP communication patterns, DNS activity, and traffic timing across different usage scenarios
- **Automated Analysis** — A Python CLI tool built with PyShark that processes `.pcap` files, extracts key metrics, detects anomalies using rule-based logic, and generates structured alert logs and reports

---

## 🎯 Key Skills Demonstrated

| Skill Area | Tools / Concepts |
|---|---|
| Packet Capture & Analysis | Wireshark, `.pcap` files, Protocol Hierarchy |
| Network Protocols | TCP, UDP, DNS, HTTP, HTTPS |
| Python Scripting | PyShark, Argparse, Collections, OS |
| Anomaly Detection | Rule-based detection engine, Baseline modeling |
| Security Alerting | Structured alert logs, Severity classification |
| Data Visualization | Matplotlib (protocol charts, IP frequency graphs) |
| Documentation | Formal report, Methodology, Comparative findings |
| Version Control | Git, GitHub, Feature branching workflow |

---

## 🗂️ Project Structure

```
network-behavior-anomaly-detection/
│
├── captures/                  # Raw .pcap files from each scenario
│   ├── idle.pcap
│   ├── browsing.pcap
│   └── app_usage.pcap
│
├── scripts/                   # Python analysis tool
│   ├── main.py                # CLI entry point
│   ├── parser.py              # Packet loading via PyShark
│   ├── metrics.py             # Protocol, IP, and DNS extraction
│   ├── detection.py           # Rule-based anomaly detection engine
│   ├── alerting.py            # Alert log generation
│   ├── visualizer.py          # Graph generation via Matplotlib
│   └── reporter.py            # Text report generation
│
├── reports/                   # Per-scenario analysis reports
│   ├── idle_report.txt
│   ├── browsing_report.txt
│   └── app_usage_report.txt
│
├── alerts/                    # Per-scenario anomaly alert logs
│   ├── idle_alerts.txt
│   ├── browsing_alerts.txt
│   └── app_usage_alerts.txt
│
├── visualizations/            # Generated graphs
│   ├── idle_protocols.png
│   ├── browsing_protocols.png
│   └── ...
│
├── docs/
│   └── project_report.md      # Full formal project report
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Wireshark with Npcap installed
- Git

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Example `requirements.txt`

```
pyshark
matplotlib
pandas
```

---

## 🚀 How to Run

### Basic Usage

```bash
python scripts/main.py --pcap captures/idle.pcap --scenario idle
```

### Run All Three Scenarios

```bash
python scripts/main.py --pcap captures/idle.pcap --scenario idle
python scripts/main.py --pcap captures/browsing.pcap --scenario browsing
python scripts/main.py --pcap captures/app_usage.pcap --scenario app_usage
```

### CLI Arguments

| Argument | Description | Required |
|---|---|---|
| `--pcap` | Path to the `.pcap` file to analyze | Yes |
| `--scenario` | Scenario label: `idle`, `browsing`, or `app_usage` | Yes |

---

## 🧠 Anomaly Detection Rules

The detection engine evaluates each capture against the following rules:

| Rule | Description | Severity |
|---|---|---|
| Suspicious DNS TLD | Flags DNS queries to uncommon or high-risk TLDs such as `.xyz`, `.top`, `.ru`, `.cn` | High |
| High Packet Volume | Flags any single source IP that exceeds the defined packet threshold within the capture window | Medium |
| Unexpected Idle Connection | Flags outbound connections to IPs not in the known-good list during idle state captures | Medium |

> Detection thresholds are configurable inside `detection.py` to allow sensitivity tuning.

---

## 📄 Output Files

After running the tool, three types of output are generated per scenario:

**Analysis Report (`reports/`)** — A structured text summary covering protocol distribution, top communicating IPs, and DNS query frequency.

**Alert Log (`alerts/`)** — A dedicated log file listing every triggered detection rule, including the offending IP or domain, the rule name, severity level, and a summary count of alerts by severity.

**Visualizations (`visualizations/`)** — Bar charts showing protocol distribution and top source IP activity for each scenario.

---

## 📊 Capture Scenarios

| Scenario | Description | Duration |
|---|---|---|
| `idle` | System on, no user activity, all applications closed | 5 minutes |
| `browsing` | Active web browsing across multiple websites | 5 minutes |
| `app_usage` | Single application in use, all others closed | 5 minutes |

Comparing traffic across these three scenarios forms the behavioral baseline — the foundation for determining what is normal and what is anomalous on this system.

---

## 📝 Documentation

The full project report is available in `docs/project_report.md` and covers:

- Objectives and methodology
- Capture strategy and scenario design
- Manual Wireshark analysis findings per scenario
- Baseline definition and modeling approach
- Detection rule design and rationale
- Alert findings and interpretation
- Comparative analysis across all three scenarios
- Conclusions and potential future enhancements

---

## 🔭 Potential Future Enhancements

- JSON export of analysis results for SIEM integration (e.g., Splunk, ELK Stack)
- Whitelist/blacklist IP logic for more precise idle state monitoring
- HTML dashboard using Plotly for interactive visualization
- Machine learning based anomaly scoring
- Real-time packet capture and monitoring
- Integration with external threat intelligence feeds

---

## 👤 Author

**Poorvajaa S**  
Integrated M.Tech CSE, cybersecurity — Year 1  

-GitHub: [poorvajaa-04](https://github.com/poorvajaa-04) 
-LinkedIn: [https://www.linkedin.com/in/poorvajaa-s-286a50398/]

---

## 📃 License

This project is intended for educational purposes as part of a cybersecurity degree portfolio.
