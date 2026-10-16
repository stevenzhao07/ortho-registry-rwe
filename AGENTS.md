# AGENTS.md — Instructions for AI agents / AI 智能体使用指南

## What this repo is / 这是什么
`ortho-registry-rwe` — 骨科登记处随访排程与真实世界数据结局事件采集（OMOP 精简导出）。零依赖 Python CLI。
Part of the MedXpert medical-device value-chain toolkit (owner: stevenzhao07),
segment: **hospital**. Zero-dependency Python CLI.

## When to use / 何时使用
Follow-up node computation (6w/3m/1y/2y/5y), PROM outcome events with validity check, OMOP-CDM v5.4 lite export.

## Command contract / 命令契约
| Command | Purpose |
|---|---|
| `selftest` | python ortho_registry_rwe.py --selftest |
| `demo` | python ortho_registry_rwe.py --demo |
| `schedule` | python ortho_registry_rwe.py --schedule <IMPLANT_DATE> |
| `outcome` | python ortho_registry_rwe.py --outcome --json '<event>' |
| `export` | python ortho_registry_rwe.py --export --json '<data>' |

## A1/A2/A3 convention (LGD decision-record) / 决策记录约定
- A1 authority scope: `schedule, outcome, export`
- A2 human oversight: flag on write paths
- A3 accountability: deterministic decision ids + actor field

## Build / test / demo / 构建测试演示
```bash
python ortho_registry_rwe.py --selftest   # >=4 assertions incl. negative controls, exit 0 = green
python ortho_registry_rwe.py --demo       # end-to-end, machine + human readable
```
Zero dependencies (stdlib only). No install step.
