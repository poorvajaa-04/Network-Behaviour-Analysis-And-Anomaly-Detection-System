import os

def generate_report(metrics, scenario, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{scenario}_report.txt")

    with open(filename, "w") as f:
        f.write(f"ANALYSIS REPORT — Scenario: {scenario.upper()}\n")
        f.write("=" * 60 + "\n\n")

        f.write("PROTOCOL DISTRIBUTION\n")
        for proto, count in metrics["protocol_counts"].most_common(10):
            f.write(f"  {proto}: {count}\n")

        f.write("\nTOP SOURCE IPs\n")
        for ip, count in metrics["top_src_ips"]:
            f.write(f"  {ip}: {count} packets\n")

        f.write("\nTOP DESTINATION IPs\n")
        for ip, count in metrics["top_dst_ips"]:
            f.write(f"  {ip}: {count} packets\n")

        f.write("\nDNS QUERIES\n")
        for domain, count in metrics["dns_queries"]:
            f.write(f"  {domain}: {count} queries\n")

    print(f"Report saved to {filename}")
