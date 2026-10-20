# Windows Security Log Analysis

A beginner-friendly cybersecurity portfolio project exploring Windows authentication events and a small Python-based CSV analyzer.

## Why I built this

I am learning the fundamentals of Security Operations Center (SOC) investigations. This project documents a guided investigation of Windows Event Viewer on my own computer and demonstrates basic Python automation with **synthetic** log data.

## Tools

- Windows Event Viewer (Windows Logs → Security)
- Python 3 (standard library only)
- GitHub

## Part 1 — Manual investigation

### Successful logon: Event ID 4624

| Field | Observed value |
| --- | --- |
| Event ID | 4624 |
| Result | Audit Success |
| Logon Type | 5 (Service) |
| Target account | SYSTEM |

**Interpretation:** The event is consistent with a Windows service signing in using the built-in SYSTEM account. This observation alone cannot establish that the system is safe or compromised.

### Failed logon: Event ID 4625

| Field | Observed value |
| --- | --- |
| Event ID | 4625 |
| Result | Audit Failure |
| Logon Type | 2 (Interactive) |
| Status | `0xC000006D` |
| SubStatus | `0xC0000380` |
| Logon process | User32 |
| Authentication package | Negotiate |

**Interpretation:** The log records an unsuccessful interactive authentication attempt. Status `0xC000006D` indicates a logon failure. The reviewed evidence does not establish the precise cause or indicate an attack by itself. A SOC analyst would correlate additional events and context before drawing conclusions.

## Part 2 — Python CSV log analyzer

`log_analyzer.py` reads a CSV file containing an `EventID` column and counts events 4624 and 4625. The alert is a **simple count-based threshold**, not an intrusion detection verdict.

The included `sample_events.csv` contains **fictional training data**, not exports from my computer.

### Run

Open PowerShell in this folder and run:

```powershell
python log_analyzer.py
```

If `python` is not recognized, try:

```powershell
py log_analyzer.py
```

Expected result for the sample data:

```text
Windows Security Log Analysis
-----------------------------
Successful logons (4624): 3
Failed logons (4625): 3
Alert: Failed logon count reached the configured threshold.
Note: This is a simple count, not evidence of an attack.
```

You can also specify a CSV file and threshold:

```powershell
python log_analyzer.py sample_events.csv --threshold 5
```

### Tests

```powershell
python -m unittest discover -s tests -v
```

## Skills practiced

- Locating and filtering Windows Security events
- Interpreting Windows logon event IDs and logon types
- Writing a Python CSV analyzer
- Testing a small Python script
- Documenting observations without overstating security conclusions

## Privacy and scope

- Analysis was limited to my own computer.
- No passwords, real usernames, IP addresses, or raw private security logs are included.
- The CSV dataset is synthetic and intended for learning.

## Future improvements

- Group failures by account and time window.
- Parse sanitized event exports from a controlled lab.
- Compare baseline activity against unusual spikes.
