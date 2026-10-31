# Customs Bonded Warehouse Duty Deferral & Cash Flow Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `model_bonded_warehouse_duty_deferral`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Models cash-flow time-value of money (TVM) and inventory carrying cost savings from utilizing bonded warehouses (Class 2 / Class 3) to defer customs duties until final entry.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Agentic Commerce (Trade Finance & Customs Warehousing)`

## MCP Tool Specification
### `model_bonded_warehouse_duty_deferral`
Parameters:
- `annual_imported_goods_value_usd` (float): Total CIF value of imported merchandise (USD)
- `average_ad_valorem_duty_rate_pct` (float): Average duty rate (e.g. 12.5%)
- `average_warehouse_dwell_months` (float): Average dwell time in bonded storage before domestic release
- `cost_of_capital_wacc_pct` (float): Company Weighted Average Cost of Capital (e.g. 9.5%)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-agentic-commerce-customs-bonded-warehouse-duty-deferral-skill": {
      "command": "python",
      "args": ["/path/to/genpark-agentic-commerce-customs-bonded-warehouse-duty-deferral-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
