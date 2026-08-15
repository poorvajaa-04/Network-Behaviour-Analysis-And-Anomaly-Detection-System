SUSPICIOUS_TLDS = ['.xyz', '.top', '.ru', '.cn', '.tk', '.pw']

HIGH_PACKET_THRESHOLD = 1000

IDLE_ALLOWED_IPS = []  # Fill this in after your first idle analysis


def check_suspicious_dns(dns_queries):
    alerts = []

    for domain, count in dns_queries:
        for tld in SUSPICIOUS_TLDS:
            if domain.endswith(tld):
                alerts.append({
                    "rule": "Suspicious DNS TLD",
                    "detail": f"Domain '{domain}' queried {count} times",
                    "severity": "High"
                })

    return alerts


def check_high_volume_ips(top_src_ips):
    alerts = []

    for ip, count in top_src_ips:
        if count > HIGH_PACKET_THRESHOLD:
            alerts.append({
                "rule": "High Packet Volume from Single IP",
                "detail": f"IP {ip} sent {count} packets",
                "severity": "Medium"
            })

    return alerts


def check_unexpected_idle_connections(top_dst_ips, scenario):
    alerts = []

    if scenario == "idle":
        for ip, count in top_dst_ips:
            if IDLE_ALLOWED_IPS and ip not in IDLE_ALLOWED_IPS:
                alerts.append({
                    "rule": "Unexpected Outbound Connection During Idle",
                    "detail": f"Connection to {ip} with {count} packets during idle state",
                    "severity": "Medium"
                })

    return alerts


def run_detection(metrics, scenario):
    all_alerts = []

    all_alerts += check_suspicious_dns(metrics["dns_queries"])

    all_alerts += check_high_volume_ips(metrics["top_src_ips"])

    all_alerts += check_unexpected_idle_connections(
        metrics["top_dst_ips"],
        scenario
    )

    return all_alerts