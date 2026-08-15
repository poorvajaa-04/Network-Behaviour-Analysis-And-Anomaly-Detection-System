from datetime import datetime
import os


def generate_alert_log(alerts, scenario, output_dir="alerts"):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, f"{scenario}_alerts.txt")

    severity_counts = {"High": 0, "Medium": 0, "Low": 0}

    with open(filename, "w") as f:
        f.write(f"ALERT LOG — Scenario: {scenario.upper()}\n")
        f.write(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        f.write("=" * 60 + "\n\n")

        if not alerts:
            f.write("No anomalies detected.\n")

        else:
            for i, alert in enumerate(alerts, 1):
                severity = alert.get("severity", "Low")
                severity_counts[severity] += 1

                f.write(f"[ALERT {i}]\n")
                f.write(f" Rule     : {alert['rule']}\n")
                f.write(f" Detail   : {alert['detail']}\n")
                f.write(f" Severity : {severity}\n")
                f.write(
                    f" Time     : {datetime.now().strftime('%H:%M:%S')}\n\n"
                )

        f.write("=" * 60 + "\n")
        f.write("SUMMARY\n")

        for level, count in severity_counts.items():
            f.write(f" {level}: {count} alert(s)\n")

    print(f"Alert log saved to {filename}")