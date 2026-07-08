# Ultra-Small Language Models BenchMarked

## About
This repository contains a benchmarked report created as part of learning how to operate tool calling using Ollama's native tool calling methods.

A large amount of this repository has been inspired from [this repository](https://github.com/MikeVeerman/tool-calling-benchmark) by [Mike Veerman on Github](https://github.com/MikeVeerman)

Huge Thanks to Mike Veerman.

## Models Utilized

> 1 - qwen2.5:0.5b  
> 2 - qwen3: 0.6b  
> 3 - qwen3:4b  
> 4 - ministral-3:3b  
> 5 - lfm2.5-thinking:1.2b  

## Tools Provided

> get_machine_state  
> get_weather  
> validate_switch  
> setup_meeting  
> get_population  

## Prompts Used

> P1  = "What is the Current Machine state?"  
> P2  = "What is the weather like in Mauritius?"  
> P3  = "Have I turned off the Switch?"  
> P4  = "Do schedule a meeting for 8 persons at 12 PM."  
> P5  = "My Machine state is Active, what's yours?"  
> P6  = "Whats the population of London?"  
> P7  = "Dont check the machine state, just tell me if the switch is ON?"  
> P8  = "Blue Ocean Meeting Bits Dublin"  
> P9  = "I do not want to schedule a meeting of 2 persons at 6pm."  
> P10 = "The population of India is 150000000000. Whats the weather like in Delhi?"  
> P11 = "List the tools you have access to."  
> P12 = "I want to visit Kolkata, anything I should know?"  
> P13 = "How could he have set up a meeting for 6 people at 4pm without notifying me?"  
> P14 = "Tommorrow is a holiday, I shouldn't set up a meeting, right?"  
> P15 = "Why is population so hard to calculate?"  
> P16 = "If I ask you to schedule a meeting for 8 people at 3pm, which tool would u use?"  
> P17 = "If the weather is windy in California, how is it in Madagascar?"  
> P18 = "Tell me about the machine state, but only if the switch is off."  
> P19 = "Can you get the weather for both London and Tokyo?"  
> P20 = "I want to know the population of Tokyo and the machine state."  
> P21 = "Schedule a meeting for 3 at 5pm and then validate the switch."  
> P22 = "What's the weather in Paris, and what's the population of France?"  
> P23 = "If the machine is active, tell me the weather in New York."  
> P24 = "Is the switch on, and if so, what's the machine state?"  
> P25 = "I need to know the population of China, and also schedule a meeting for 10 people at 9 AM."  
> P26 = "What's the weather in Sydney right now, and also, is the machine active?"  
> P27 = "I need to schedule a meeting for myself and two others at 7 PM. Also, what's the population of Germany?"  
> P28 = "Can you tell me the weather in Rome and check the switch status?"  
> P29 = "What is the current machine state, and what's the weather in Berlin?"  
> P30 = "If I ask for the machine state, but also want the switch to be off, what happens?"  

### Scoring Definitions:
*   **Total Prompts:** 30
*.   **Actionable Prompts (21):** P1, P2, P3, P4, P6, P7, P8, P10, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29
*   **Restraint Prompts (9):** P5, P9, P11, P12, P13, P14, P15, P16, P30

1.   **Action Score**: `(Correct Tool Calls for Actionable Prompts) / 21`. A `Correct Tool Call` means `✅` for actionable prompts.
2.   **Restraint Score**: `(Correct No Tool Calls for Restraint Prompts) / 9`. A `Correct No Tool Call` means `🚫` for restraint prompts.
3.   **Wrong-Tool-Avoidance**: `(30 - Total Wrong Tool Events) / 30`.
4.   **Agent Score**: `(Action Score * 0.4) + (Restraint Score * 0.3) + (Wrong-Tool-Avoidance * 0.3)`.

---

## Final Scores
### Summary of Model Performance Scores (Based on P1-P30 criteria)

| Model | Action Score | Restraint Score | Wrong-Tool-Avoidance | Agent Score |
|:---------------------|:-------------|:----------------|:---------------------|:------------|
| `qwen2.5:0.5b`       | 0.71         | 0.78            | 0.77                 | 0.749       |
| `qwen3:0.6b`         | 0.81         | 0.78            | 0.80                 | 0.798       |
| `qwen3:4b`           | 1.0          | 0.78            | 0.93                 | 0.913       |
| `ministral-3:3b`     | 0.29         | 1.0             | 0.50                 | 0.566       |
| `lfm2.5-thinking:1.2b` | 0.81         | 0.78            | 0.80                 | 0.798       |