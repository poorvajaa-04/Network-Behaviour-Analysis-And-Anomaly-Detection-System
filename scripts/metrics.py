from collections import Counter

def extract_metrics(packets):

    protocols = []
    src_ips = []
    dst_ips = []
    dns_queries = []

    for pkt in packets:

        try:
            protocols.append(pkt.highest_layer)
        except:
            pass

        try:
            src_ips.append(pkt.ip.src)
            dst_ips.append(pkt.ip.dst)
        except:
            pass

        try:
            if hasattr(pkt, 'dns') and hasattr(pkt.dns, 'qry_name'):
                dns_queries.append(pkt.dns.qry_name)
        except:
            pass

    return {
        "protocol_counts": Counter(protocols),
        "top_src_ips": Counter(src_ips).most_common(10),
        "top_dst_ips": Counter(dst_ips).most_common(10),
        "dns_queries": Counter(dns_queries).most_common(20)
    }

