"""CSV loading and research-source validation helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


def read_csv_records(path: Path) -> list[dict[str, str]]:
    """Read UTF-8 CSV records and report file/header failures clearly."""
    if not path.is_file():
        raise FileNotFoundError(f"Required project CSV was not found: {path}")
    with path.open(encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames:
            raise ValueError(f"CSV has no header row: {path}")
        return list(reader)


def validate_source_records(
    records: list[dict[str, str]],
    *,
    required_ids: Iterable[str],
    dated_ids: Iterable[str],
) -> None:
    """Validate required source rows, HTTPS links, and dates where documented."""
    required = set(required_ids)
    dated = set(dated_ids)
    seen: set[str] = set()
    for record in records:
        source_id = record.get("source_id", "").strip()
        if source_id in seen:
            raise ValueError(f"Duplicate source_id in research source log: {source_id}")
        if source_id:
            seen.add(source_id)
    missing = sorted(required - seen)
    if missing:
        raise ValueError(f"Research source log is missing required IDs: {', '.join(missing)}")

    for record in records:
        source_id = record.get("source_id", "").strip()
        if source_id not in required:
            continue
        if not record.get("url", "").startswith("https://"):
            raise ValueError(f"Source {source_id} is missing a valid HTTPS URL.")
        if source_id in dated and not record.get("publication_date", "").strip():
            raise ValueError(f"Source {source_id} is missing its publication date.")
