<div align="center">

# ortho-registry-rwe

**Orthopedic registry follow-up scheduling and RWE outcome events (OMOP-lite export). Zero-dependency Python CLI.** · 骨科登记处随访排程与真实世界数据结局事件采集（OMOP 精简导出）。零依赖 Python CLI。

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Scorecard](https://api.scorecard.dev/projects/github.com/stevenzhao07/ortho-registry-rwe/badge)](https://scorecard.dev)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Zero-Dep](https://img.shields.io/badge/dependencies-zero-green.svg)](module.json)

*Part of the MedXpert medical-device value-chain toolkit · segment: hospital*
*MedXpert 医械全产业链工具链 · hospital 模块*

</div>

---

## Positioning · 定位

**Hospital-side full-lifecycle · zero-dependency · AI-readable contract**

Part of the **33-module MedXpert medical-device value-chain toolkit** — the only
hospital-side suite combining full-lifecycle coverage, zero runtime dependencies,
and an AI-readable layer (`module.json` / `AGENTS.md` / `llms.txt`).

医院端全生命周期 × 零依赖 × AI 可读层：33 模块 MedXpert 医械全产业链工具链的医院端模块，
唯一同时具备全生命周期覆盖、零运行时依赖与 AI 可读契约（module.json / AGENTS.md / llms.txt）的套件。


## Overview · 总览

Follow-up node computation (6w/3m/1y/2y/5y), PROM outcome events with validity check, OMOP-CDM v5.4 lite export.

本工具零依赖（纯标准库）、自带自测与演示，输出机器可读 JSON 与人读报告。

## Quick start · 快速上手

```bash
python ortho_registry_rwe.py --selftest
python ortho_registry_rwe.py --demo
```

| Command | Description |
|---|---|
| `selftest` | python ortho_registry_rwe.py --selftest |
| `demo` | python ortho_registry_rwe.py --demo |
| `schedule` | python ortho_registry_rwe.py --schedule <IMPLANT_DATE> |
| `outcome` | python ortho_registry_rwe.py --outcome --json '<event>' |
| `export` | python ortho_registry_rwe.py --export --json '<data>' |

## AI-readable contract · AI 可读契约
| Artifact | What it gives an AI agent / 给 AI 什么 |
|---|---|
| `module.json` | lgd-skeleton module contract: scope, commands, exit codes, A1/A2/A3 flags |
| `AGENTS.md` | when to use, command contract, data model, privacy, interop |
| `llms.txt` | one-screen LLM summary + protocol + commands |

Every decision record carries A1 authority scope / A2 human-oversight flag / A3 accountability id (LGD convention).

## Security & quality · 安全与质量
- OpenSSF Scorecard supply-chain scoring (weekly CI + per push)
- CodeQL SAST · Dependabot weekly updates · SECURITY.md private-advisory policy
- `--selftest` guards regressions with negative controls

## License · 许可
[Apache-2.0](LICENSE)
