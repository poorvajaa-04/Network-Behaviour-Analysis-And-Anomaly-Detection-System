import matplotlib.pyplot as plt
import os


def plot_protocol_distribution(protocol_counts, scenario, output_dir="visualizations"):
    os.makedirs(output_dir, exist_ok=True)

    labels = list(protocol_counts.keys())[:8]
    values = [protocol_counts[l] for l in labels]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color="steelblue")
    plt.title(f"Protocol Distribution — {scenario}")
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            f"{scenario}_protocols.png"
        )
    )

    plt.close()


def plot_top_ips(top_ips, scenario, output_dir="visualizations"):
    os.makedirs(output_dir, exist_ok=True)

    ips = [x[0] for x in top_ips[:10]]
    counts = [x[1] for x in top_ips[:10]]

    plt.figure(figsize=(12, 5))
    plt.barh(ips, counts, color="darkorange")
    plt.title(f"Top Source IPs — {scenario}")
    plt.xlabel("Packet Count")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            f"{scenario}_top_ips.png"
        )
    )

    plt.close()