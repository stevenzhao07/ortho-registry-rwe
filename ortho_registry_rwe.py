#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ortho-registry-rwe — Orthopedic registry follow-up scheduling + RWE outcome events.
骨科登记处随访排程与真实世界数据（RWE）结局事件采集。Zero-dependency."""
import argparse, hashlib, json, sys
from datetime import date, timedelta

TOOL_VERSION = "0.1.0"
FOLLOWUP_POINTS = [(6, "week"), (3, "month"), (1, "year"), (2, "year"), (5, "year")]

def followup_schedule(implant_date, points=None):
    pts = points or FOLLOWUP_POINTS
    base = date.fromisoformat(implant_date)
    out = []
    for n, unit in pts:
        if unit == "week":
            d = base + timedelta(weeks=n)
        elif unit == "month":
            d = base.replace(year=base.year + (base.month + n - 1) // 12,
                             month=(base.month + n - 1) % 12 + 1)
        else:
            d = base.replace(year=base.year + n)
        out.append({"point": "%d%s" % (n, unit), "due": d.isoformat()})
    return out

def outcome_event(patient_key, implant_date, prom_score, adverse=""):
    base = date.fromisoformat(implant_date)
    rec = {"patient_key": patient_key, "implant_date": implant_date,
           "prom_score": prom_score, "prom_valid": 0 <= prom_score <= 100,
           "adverse_event": adverse,
           "event_id": "evt-" + hashlib.sha256((patient_key + implant_date + str(prom_score)).encode()).hexdigest()[:10]}
    return rec

def export_omop(schedule, events):
    return {"schema": "omop-cdm-v5.4-lite", "followup_visits": schedule,
            "measurement_events": events, "domain": "orthopedic-registry"}

def run_selftest():
    checks = []
    s = followup_schedule("2026-01-01")
    c1 = len(s) == 5 and s[0]["point"] == "6week" and s[0]["due"] == "2026-02-12"
    checks.append(("positive: 6-week followup computed", c1))
    c2 = s[2]["point"] == "1year" and s[2]["due"] == "2027-01-01"
    checks.append(("positive: 1-year followup computed", c2))
    c3 = outcome_event("p1", "2026-01-01", 105)["prom_valid"] is False
    checks.append(("negative: PROM 105 rejected", c3))
    c4 = followup_schedule("2025-02-28")[1]["due"] == "2025-05-28"
    checks.append(("negative: month-roll edge (Feb 28 -> May 28)", c4))
    for name, ok in checks:
        print("[selftest] %s PASS" % name if ok else "[selftest] %s FAIL" % name)
    return 0 if all(ok for _, ok in checks) else 1

def run_demo():
    print("=== ortho-registry-rwe demo (v%s) ===" % TOOL_VERSION)
    s = followup_schedule("2026-03-10")
    print("[SCHEDULE] " + json.dumps(s, ensure_ascii=False))
    ev = [outcome_event("p1", "2026-03-10", 78), outcome_event("p1", "2026-03-10", 101)]
    print("[EVENTS]   " + json.dumps(ev, ensure_ascii=False))
    print("[OMOP]     " + json.dumps(export_omop(s, ev), ensure_ascii=False))
    return 0

def main():
    ap = argparse.ArgumentParser(description="Orthopedic registry follow-up + RWE outcome toolkit")
    ap.add_argument("--schedule", metavar="IMPLANT_DATE", help="YYYY-MM-DD -> follow-up nodes JSON")
    ap.add_argument("--outcome", action="store_true", help="record an outcome event")
    ap.add_argument("--export", action="store_true", help="export OMOP-lite JSON")
    ap.add_argument("--json", metavar="PAYLOAD", help="JSON payload for outcome/export")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(run_selftest())
    if args.demo:
        sys.exit(run_demo())
    if args.schedule:
        try:
            print(json.dumps(followup_schedule(args.schedule), ensure_ascii=False)); sys.exit(0)
        except ValueError:
            print("[error] implant_date must be YYYY-MM-DD", file=sys.stderr); sys.exit(2)
    if args.outcome:
        if not args.json:
            print("--outcome requires --json", file=sys.stderr); sys.exit(2)
        d = json.loads(args.json)
        rec = outcome_event(d["patient_key"], d["implant_date"], d["prom_score"], d.get("adverse", ""))
        print(json.dumps(rec, ensure_ascii=False)); sys.exit(0 if rec["prom_valid"] else 1)
    if args.export:
        if not args.json:
            print("--export requires --json", file=sys.stderr); sys.exit(2)
        d = json.loads(args.json)
        print(json.dumps(export_omop(d.get("schedule", []), d.get("events", [])), ensure_ascii=False)); sys.exit(0)
    ap.print_help(); sys.exit(2)

if __name__ == "__main__":
    main()
