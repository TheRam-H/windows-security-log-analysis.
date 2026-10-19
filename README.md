# Windows Security Log Analysis

## Overview

This beginner cybersecurity project documents my analysis of Windows Security Event Logs using Windows Event Viewer.

The goal was to understand successful and failed logon events and practice basic Security Operations Center (SOC) investigation skills.

## Tools Used

- Windows 11
- Windows Event Viewer
- Windows Security Event Logs

## Objectives

- Identify successful and failed logon events.
- Understand Windows Event IDs 4624 and 4625.
- Analyze logon types and authentication status codes.
- Document findings and assess their security significance.

## Investigation 1: Successful Logon (Event ID 4624)

| Field | Observed Value |
|---|---|
| Event ID | 4624 |
| Audit Result | Success |
| Logon Type | 5 (Service) |
| Target Account | SYSTEM |

### Analysis

Event ID 4624 records a successful logon. Logon Type 5 indicates a service logon.

The target account was SYSTEM, a built-in Windows account commonly used by system services.

**Assessment:** This event is consistent with normal Windows service activity. The event alone does not establish whether the overall system is secure.

## Investigation 2: Failed Logon (Event ID 4625)

| Field | Observed Value |
|---|---|
| Event ID | 4625 |
| Audit Result | Failure |
| Logon Type | 2 (Interactive) |
| Status | 0xC000006D |
| SubStatus | 0xC0000380 |
| Logon Process | User32 |
| Authentication Package | Negotiate |

### Analysis

Event ID 4625 records a failed logon. Logon Type 2 indicates an interactive logon attempt.

Status `0xC000006D` indicates that authentication failed. The specific cause of the failure was not established from the reviewed information.

**Assessment:** One failed interactive logon does not by itself indicate an attack. Further investigation would require additional event context and correlation.

## Skills Practiced

- Navigating Windows Event Viewer
- Filtering Windows Security Logs by Event ID
- Interpreting logon types and authentication results
- Documenting security findings
- Distinguishing observed facts from assumptions

## Security and Privacy

This project was conducted on my own Windows computer. Personal account details, raw event logs, and sensitive system information are not published.

## Conclusion

This project introduced me to Windows security event analysis and basic SOC investigation methods.

It provided hands-on practice interpreting authentication events and documenting findings for further review.

## Future Improvements

- Compare multiple authentication events over time.
- Analyze additional Windows Security Event IDs.
- Develop a simple Python script to summarize sample log data.
