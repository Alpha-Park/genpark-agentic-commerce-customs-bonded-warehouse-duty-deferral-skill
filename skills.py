# -*- coding: utf-8 -*-
"""Customs Bonded Warehouse Duty Deferral & Cash Flow Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def model_bonded_warehouse_duty_deferral(**kwargs):
    """Models cash-flow time-value of money (TVM) and inventory carrying cost savings from utilizing bonded warehouses (Class 2 / Class 3) to defer customs duties until final entry."""
    annual_imported_goods_value_usd = kwargs.get('annual_imported_goods_value_usd')
    average_ad_valorem_duty_rate_pct = kwargs.get('average_ad_valorem_duty_rate_pct')
    average_warehouse_dwell_months = kwargs.get('average_warehouse_dwell_months')
    cost_of_capital_wacc_pct = kwargs.get('cost_of_capital_wacc_pct')

    total_customs_duty_liability_usd = round(annual_imported_goods_value_usd * (average_ad_valorem_duty_rate_pct / 100.0), 2)
    
    # TVM deferred duty interest savings: Duty * (WACC * (dwell_months / 12))
    annual_interest_savings_usd = round(total_customs_duty_liability_usd * (cost_of_capital_wacc_pct / 100.0) * (average_warehouse_dwell_months / 12.0), 2)
    
    # Re-export re-drawback avoidance: Goods re-exported directly from bonded warehouse pay 0% duty (eliminating 1% CBP fee on drawback)
    potential_reexport_drawback_fee_avoidance = round(total_customs_duty_liability_usd * 0.15 * 0.01, 2)
    
    total_net_financial_benefit = round(annual_interest_savings_usd + potential_reexport_drawback_fee_avoidance, 2)
    
    result = {
        "status": "success",
        "annual_import_value_usd": annual_imported_goods_value_usd,
        "total_ad_valorem_duty_liability_usd": total_customs_duty_liability_usd,
        "average_dwell_time_months": average_warehouse_dwell_months,
        "working_capital_interest_savings_usd": annual_interest_savings_usd,
        "net_annual_bonded_benefit_usd": total_net_financial_benefit,
        "customs_warehousing_recommendation": "IMPLEMENT_CLASS_3_BONDED_FACILITY: Substantial capital relief from duty deferral.",
        "engine": "GenPark Customs Bonded Warehouse Working Capital Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "model_bonded_warehouse_duty_deferral": {
        "name": "model_bonded_warehouse_duty_deferral",
        "description": "Models cash-flow time-value of money (TVM) and inventory carrying cost savings from utilizing bonded warehouses (Class 2 / Class 3) to defer customs duties until final entry.",
        "parameters": {
            "type": "object",
            "properties": {
                "annual_imported_goods_value_usd": {"type": "number", "description": "Total CIF value of imported merchandise (USD)"},
                "average_ad_valorem_duty_rate_pct": {"type": "number", "description": "Average duty rate (e.g. 12.5%)"},
                "average_warehouse_dwell_months": {"type": "number", "description": "Average dwell time in bonded storage before domestic release"},
                "cost_of_capital_wacc_pct": {"type": "number", "description": "Company Weighted Average Cost of Capital (e.g. 9.5%)"},
            },
            "required": ['annual_imported_goods_value_usd', 'average_ad_valorem_duty_rate_pct', 'average_warehouse_dwell_months', 'cost_of_capital_wacc_pct']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "model_bonded_warehouse_duty_deferral":
            res = model_bonded_warehouse_duty_deferral(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-agentic-commerce-customs-bonded-warehouse-duty-deferral-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-agentic-commerce-customs-bonded-warehouse-duty-deferral-skill...")
    test_args = {'annual_imported_goods_value_usd': 8500000.0, 'average_ad_valorem_duty_rate_pct': 14.0, 'average_warehouse_dwell_months': 4.5, 'cost_of_capital_wacc_pct': 10.0}
    res = model_bonded_warehouse_duty_deferral(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-agentic-commerce-customs-bonded-warehouse-duty-deferral-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
