# Wi-Fi Network Scanner

[راهنمای فارسی](README_FA.md)

A small local network scanner adapted from a previous Wi-Fi experiment. It lists visible SSIDs and signal strength from the first available wireless interface. It does not connect to networks, try passwords, or collect credentials.

## Run

On a computer with a supported Wi-Fi adapter:

```bash
pip install -r requirements.txt
python scanner.py
```

Use `--wait 4` if your adapter needs longer to return scan results. The program has not been exercised with a physical adapter in this preparation environment. The original password-guessing and password-logging code is intentionally excluded. MIT licensed.
