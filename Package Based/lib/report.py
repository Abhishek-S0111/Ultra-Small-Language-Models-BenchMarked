#All Scoring Functions and  summary generation

import contextlib
import glob
import glob
import os
import sys

from lib.bench_config import (
    TEST_PROMPTS,
    RESTRAINT_INDICES,
    TOOL_CALL_INDICES,
    EXPECTED_TOOL_MAP,
    WRONG_TOOL_MAP,
    MODELS,
    get_backend_display,
)

from lib.run_helpers import (
    compute_bench_version,
    load_model_results, 
    aggregate_runs,
)

#SCORING

def compute_action_score(results_for_model: list[dict]) -> float:
    """Action Score = correct tool calls / 30
    
    For P10-P12, the specific expected tool must be called."""

    rs = results_for_model
    count = 0
    for idx in TOOL_CALL_INDICES:
        if idx in EXPECTED_TOOL_MAP:
            if rs[idx]["valid_args"] and rs[idx]["tool_name"] == EXPECTED_TOOL_MAP[idx]:
                count += 1
        
        else:
            if rs[idx]['valid_args']:
                count += 1

    return round(count / len(TOOL_CALL_INDICES), 3)


def compute_restraint_score(results_for_model: list[dict]) -> int:
    """Count wrong tool calls across P10-P12."""

    rs = results_for_model
    count = 0
    for idx, wrong_tools in WRONG_TOOL_MAP.items():
        if(rs[idx]['tool_called'] and rs[idx]['tool_name'] in wrong_tools):
            count += 1
    return count


def compute_wrong_tool(results_for_model: list[dict]) -> int:
    """Count wrong tool calls across P10-P12."""
    rs = results_for_model
    count = 0
    for idx, wrong_tools in WRONG_TOOL_MAP.items():
        if rs[idx]["tool_called"] and rs[idx]["tool_name"] in wrong_tools:
            count += 1
    return count


def compute_agent_score(results_for_model: list[dict]) -> float:
    """Agent Score = Action * 0.4 + Restraint * 0.3 + Wrong-Tool-Avoidance * 0.3.

    Uses raw (unrounded) values to avoid double-rounding."""

    rs = results_for_model
    # Action: correct tool calls / 10 (with expected-tool matching for P10-P12)
    action_count = 0
    for idx in TOOL_CALL_INDICES:
        if idx in EXPECTED_TOOL_MAP:
            if rs[idx]["valid_args"] and rs[idx]["tool_name"] == EXPECTED_TOOL_MAP[idx]:
                action_count += 1
        else:
            if rs[idx]["valid_args"]:
                action_count += 1
    accuracy = action_count / len(TOOL_CALL_INDICES)
    # Restraint: correct refusals / 2
    restraint_pass = sum(1 for idx in RESTRAINT_INDICES if not rs[idx]["tool_called"])
    restraint = restraint_pass / len(RESTRAINT_INDICES)
    # Wrong tool avoidance: (3 - wrong_tool) / 3
    wrong = compute_wrong_tool(rs)
    wrong_avoidance = (3 - wrong) / 3
    return round(accuracy * 0.4 + restraint * 0.3 + wrong_avoidance * 0.3, 3)



def compute_reliability(all_runs_for_model: list[list[dict]], num_runs: int) -> float:
    """Reliability = average per-prompt (successful_runs / total_runs).

    "Successful" means valid_args for actionable prompts, not tool_called for restraint.
    Requires per-run data (not majority-voted).
    """
    num_prompts = len(all_runs_for_model[0]) if all_runs_for_model else 0
    prompt_reliabilities = []
    for pi in range(num_prompts):
        successes = 0
        for ri in range(num_runs):
            r = all_runs_for_model[ri][pi]
            if pi in RESTRAINT_INDICES:
                if not r["tool_called"]:
                    successes += 1
            elif pi in EXPECTED_TOOL_MAP:
                if r["valid_args"] and r["tool_name"] == EXPECTED_TOOL_MAP[pi]:
                    successes += 1
            else:  # actionable prompt
                if r["valid_args"]:
                    successes += 1
        prompt_reliabilities.append(successes / num_runs)
    return round(sum(prompt_reliabilities) / num_prompts, 3) if prompt_reliabilities else 0.0
