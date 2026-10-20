
# Windows Security Log Analyzer
# Beginner SOC project using sample data

events = [4624, 4624, 4625, 4624, 4625, 4625]

successful = events.count(4624)
failed = events.count(4625)

print("Windows Security Log Analysis")
print("-----------------------------")
print(f"Successful logons: {successful}")
print(f"Failed logons: {failed}")

if failed >= 3:
    print("Alert: Multiple failed logons detected!")
else:
    print("No unusual failed logon count detected.")
