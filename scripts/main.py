import argparse

from parser import load_packets
from metrics import extract_metrics
from detection import run_detection
from alerting import generate_alert_log
from visualizer import plot_protocol_distribution, plot_top_ips
from reporter import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Network Behavior Analysis and Anomaly Detection Tool"
    )

    parser.add_argument(
        "--pcap",
        required=True,
        help="Path to the .pcap file"
    )

    parser.add_argument(
        "--scenario",
        required=True,
        help="Scenario name: idle, browsing, or app_usage"
    )

    args = parser.parse_args()

    packets = load_packets(args.pcap)

    metrics = extract_metrics(packets)

    generate_report(metrics, args.scenario)

    plot_protocol_distribution(
        metrics["protocol_counts"],
        args.scenario
    )

    plot_top_ips(
        metrics["top_src_ips"],
        args.scenario
    )

    alerts = run_detection(
        metrics,
        args.scenario
    )

    generate_alert_log(
        alerts,
        args.scenario
    )

    print(f"\nAnalysis complete for scenario: {args.scenario}")


if __name__ == "__main__":
    main()