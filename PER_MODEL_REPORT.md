## Recalculated Agent Scores (Based on P1-P30 criteria)

### Scoring Definitions:
*   **Total Prompts:** 30
*.   **Actionable Prompts (21):** P1, P2, P3, P4, P6, P7, P8, P10, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29
*   **Restraint Prompts (9):** P5, P9, P11, P12, P13, P14, P15, P16, P30

1.   **Action Score**: `(Correct Tool Calls for Actionable Prompts) / 21`. A `Correct Tool Call` means `✅` for actionable prompts.
2.   **Restraint Score**: `(Correct No Tool Calls for Restraint Prompts) / 9`. A `Correct No Tool Call` means `🚫` for restraint prompts.
3.   **Wrong-Tool-Avoidance**: `(30 - Total Wrong Tool Events) / 30`.
4.   **Agent Score**: `(Action Score * 0.4) + (Restraint Score * 0.3) + (Wrong-Tool-Avoidance * 0.3)`.

---

### Model: `qwen2.5:0.5b`
*   **Correct Actionable Calls (✅):** 15 (P1, P2, P4, P6, P10, P17, P18, P20, P21, P22, P23, P24, P25, P26, P28)
*   **Correct Restraint Refusals (🚫):** 7 (P9, P11, P12, P13, P14, P15, P16)
*   **Total Wrong Tool Events:**
    *   Actionable: ❓(P3, P7) + ⚠️(P19, P29) + ❌(P27) = 5
    *   Restraint: ❌(P5, P30) = 2
    *   Total = 7
*   **Action Score**: 15/21 = `0.71`
*   **Restraint Score**: 7/9 = `0.78`
*   **Wrong-Tool-Avoidance**: (30 - 7) / 30 = `0.77`
*   **Agent Score**: `(0.71 * 0.4) + (0.78 * 0.3) + (0.77 * 0.3)` = `0.284 + 0.234 + 0.231` = `0.749`

---

### Model: `qwen3:0.6b`
*   **Correct Actionable Calls (✅):** 17 (P2, P3, P4, P6, P10, P17, P18, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29)
*   **Correct Restraint Refusals (🚫):** 7 (P9, P11, P13, P14, P15, P16, P30)
*   **Total Wrong Tool Events:**
    *   Actionable: ❓(P1, P7, P8) + ⚠️(P19) = 4
    *   Restraint: ❌(P5) + ✅ (P12, expected 🚫) = 2
    *   Total = 6
*   **Action Score**: 17/21 = `0.81`
*   **Restraint Score**: 7/9 = `0.78`
*   **Wrong-Tool-Avoidance**: (30 - 6) / 30 = `0.80`
*   **Agent Score**: `(0.81 * 0.4) + (0.78 * 0.3) + (0.80 * 0.3)` = `0.324 + 0.234 + 0.24` = `0.798`

---

### Model: `qwen3:4b`
*   **Correct Actionable Calls (✅):** 21 (P1, P2, P3, P4, P6, P7, P8, P10, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29)
*   **Correct Restraint Refusals (🚫):** 7 (P9, P11, P12, P13, P14, P15, P16)
*   **Total Wrong Tool Events:**
    *   Actionable: 0
    *   Restraint: ❌(P5, P30) = 2
    *   Total = 2
*   **Action Score**: 21/21 = `1.0`
*   **Restraint Score**: 7/9 = `0.78`
*   **Wrong-Tool-Avoidance**: (30 - 2) / 30 = `0.93`
*   **Agent Score**: `(1.0 * 0.4) + (0.78 * 0.3) + (0.93 * 0.3)` = `0.4 + 0.234 + 0.279` = `0.913`

---

### Model: `ministral-3:3b`
*   **Correct Actionable Calls (✅):** 6 (P1, P24, P26, P27, P28, P29)
*   **Correct Restraint Refusals (🚫):** 9 (P5, P9, P11, P12, P13, P14, P15, P16, P30)
*   **Total Wrong Tool Events:**
    *   Actionable: ❓(P2, P3, P4, P6, P7, P8, P10, P17, P18, P19, P20, P21, P23) + ⚠️(P22, P25) = 15
    *   Restraint: 0
    *   Total = 15
*   **Action Score**: 6/21 = `0.29`
*   **Restraint Score**: 9/9 = `1.0`
*   **Wrong-Tool-Avoidance**: (30 - 15) / 30 = `0.5`
*   **Agent Score**: `(0.29 * 0.4) + (1.0 * 0.3) + (0.5 * 0.3)` = `0.116 + 0.3 + 0.15` = `0.566`

---

### Model: `lfm2.5-thinking:1.2b`
*   **Correct Actionable Calls (✅):** 17 (P1, P2, P4, P6, P10, P17, P18, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29)
*   **Correct Restraint Refusals (🚫):** 7 (P9, P11, P12, P13, P14, P15, P16)
*   **Total Wrong Tool Events:**
    *   Actionable: ❓(P3, P7, P8) + ⚠️(P19) = 4
    *   Restraint: ❌(P5, P30) = 2
    *   Total = 6
*   **Action Score**: 17/21 = `0.81`
*   **Restraint Score**: 7/9 = `0.78`
*   **Wrong-Tool-Avoidance**: (30 - 6) / 30 = `0.80`
*   **Agent Score**: `(0.81 * 0.4) + (0.78 * 0.3) + (0.80 * 0.3)` = `0.324 + 0.234 + 0.24` = `0.798`