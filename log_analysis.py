def filter_by_level(lines, wanted_level):
    """Return log lines whose level matches wanted_level."""
    filtered = []
    for line in lines:
        if not line or "|" not in line:
            continue
        parts = line.split("|")
        if len(parts) < 3:
            continue
        level = parts[1].strip()
        if level == wanted_level:
            filtered.append(line)
    return filtered


def count_levels(lines):
    """Count log entries by level."""
    counts = {}
    for line in lines:
        if not line or "|" not in line:
            continue
        parts = line.split("|")
        if len(parts) < 3:
            continue
        level = parts[1].strip()
        if not level:
            continue
        counts[level] = counts.get(level, 0) + 1
    return counts


def count_services(lines):
    """Count log entries by service."""
    counts = {}
    for line in lines:
        if not line or "|" not in line:
            continue
        parts = line.split("|")
        if len(parts) < 3:
            continue
        service = parts[2].strip()
        if not service:
            continue
        counts[service] = counts.get(service, 0) + 1
    return counts


if __name__ == '__main__':
    logs = [
        "2026-02-05 08:11:20 | ERROR | db | DB timeout",
        "2026-02-05 08:11:21 | INFO | api | Request received",
        "2026-02-05 08:11:22 | WARN | disk | Disk almost full",
        "2026-02-05 08:11:23 | ERROR | api | Failed request",
        "2026-02-05 08:11:24 | INFO | auth | User login",
        "2026-02-05 08:11:25 | WARN | api | Slow response",
    ]

    print("Filtered ERROR logs:")
    for l in filter_by_level(logs, "ERROR"):
        print(l)

    print("\nCount by level:", count_levels(logs))
    print("Count by service:", count_services(logs))
