"""List nearby Wi-Fi networks without attempting to connect to them."""

import argparse
import time


def scan(wait_seconds: float = 2.0) -> list[tuple[str, int]]:
    from pywifi import PyWiFi

    interfaces = PyWiFi().interfaces()
    if not interfaces:
        raise RuntimeError("No Wi-Fi interface was found.")
    interface = interfaces[0]
    interface.scan()
    time.sleep(wait_seconds)
    return sorted(
        {(item.ssid or "<hidden>", item.signal) for item in interface.scan_results()},
        key=lambda item: item[1],
        reverse=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="List nearby Wi-Fi networks")
    parser.add_argument("--wait", type=float, default=2.0, help="Seconds to wait for scan results")
    args = parser.parse_args()
    if args.wait < 0:
        parser.error("--wait must be non-negative")
    try:
        networks = scan(args.wait)
    except Exception as exc:
        parser.exit(1, f"Scan failed: {exc}\n")
    for ssid, signal in networks:
        print(f"{signal:>4} dBm  {ssid}")


if __name__ == "__main__":
    main()
