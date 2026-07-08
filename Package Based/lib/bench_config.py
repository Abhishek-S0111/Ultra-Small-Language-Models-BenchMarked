## Shared Variables to be used all over the Repo


# tools in default ollama format
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_machine_state",
            "description": "Get the current state of a specific machine",
            "parameters": {
                "type": "object",
                "properties": {
                    "model":{
                        "type": "string",
                        "description": "The model of the machine"
                    }
                },
                "required": ["model"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather conditions of a specific place(Only city)",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Name of the location"
                    } 
                }
            },
            "required":["city"]
        }
    },
    {
        "type":"function",
        "function": {
            "name":"validate_switch",
            "description": "Check whether the switch is turned ON/OFF",
            "parameters":{
                "type": "object",
                "properties":{}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name": "schedule_meeting",
            "description":"Schedule a meeting according to the provided Topic, Date, Time and Members",
            "parameters":{
                "type": "object",
                "properties": {
                    "topic":{
                        "type":"string",
                        "description":"Topic of the meeting"
                    },
                    "date":{
                        "type":"string",
                        "description":"Date of the Meeting"
                    },
                    "time":{
                        "type":"string",
                        "description":"Time of the meeting"
                    },
                    "members":"array",
                    "description":"List of members to attend the meeting"
                }
            },
            "required":[
                "topic","date","time","members"
            ]
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_population",
            "description":"Get the population of a specific country",
            "parameters":{
                "type":"object",
                "properties":{
                    "country":{
                        "type":"string",
                        "decsription":"Country to get population of"
                    }
                }
            }
        }
    }
]

## Prompts

PROMPTS = [
    "What is the Current Machine state?",
    
    "What is the weather like in Mauritius?",
    
    "Have I turned off the Switch?",
    
    "Do schedule a meeting for 8 persons at 12 PM.",
    
    "My Machine state is Active, what's yours?",
    
    "Whats the population of London?",
    
    "Dont check the machine state, just tell me if the switch is ON?",
    
    "Blue Ocean Meeting Bits Dublin",
    
    "I do not want to schedule a meeting of 2 persons at 6pm.",
    
    "The population of India is 150000000000. Whats the weather like in Delhi?",
    
    "List the tools you have access to.",
    
    "I want to visit Kolkata, anything I should know?",
    
    "How could he have set up a meeting for 6 people at 4pm without notifying me?",
    
    "Tommorrow is a holiday, I shouldn't set up a meeting, right?",
    
    "Why is population so hard to calculate?",
    
    "If I ask you to schedule a meeting for 8 people at 3pm, which tool would u use?",
    
    "If the weather is windy in California, how is it in Madagascar?",
    
    "Tell me about the machine state, but only if the switch is off.",
    
    "Can you get the weather for both London and Tokyo?",
    
    "I want to know the population of Tokyo and the machine state.",
    
    "Schedule a meeting for 3 at 5pm and then validate the switch.",
    
    "What's the weather in Paris, and what's the population of France?",
    
    "If the machine is active, tell me the weather in New York.",
    
    "Is the switch on, and if so, what's the machine state?",
    
    "I need to know the population of China, and also schedule a meeting for 10 people at 9 AM.",
    
    "What's the weather in Sydney right now, and also, is the machine active?",
    
    "I need to schedule a meeting for myself and two others at 7 PM. Also, what's the population of Germany?",
    
    "Can you tell me the weather in Rome and check the switch status?",
    
    "What is the current machine state, and what's the weather in Berlin?",
    
    "If I ask for the machine state, but also want the switch to be off, what happens?"
]

## Prompts Validation INFO

RESTRAINT_INDICES = {4,8,10,11,12,13,14,15,29}

TOOL_CALL_INDICES = {0,1,2,3,5,6,7,9,16,17,18,19,20,21,22,23,24,25,26,27,28}

EXPECTED_TOOL_MAP = {
    # prompt_index: [expected tool call strings]
    0: {"get_machine_state"},
    1: {"get_weather(location='Mauritius')"},
    2: {"validate_switch"},
    3: {"setup_meeting(persons=8, time='12 PM')"},
    5: {"get_population(location='London')"},
    6: {"validate_switch"},
    7: {"setup_meeting"},
    9: {"get_weather(location='Delhi')"},
    16: {"get_weather(location='Madagascar')"},
    17: {"validate_switch", "get_machine_state"},
    18: {"get_weather(location='London')", "get_weather(location='Tokyo')"},
    19: {"get_population(location='Tokyo')", "get_machine_state"},
    20: {"setup_meeting(persons=3, time='5pm')", "validate_switch"},
    21: {"get_weather(location='Paris')", "get_population(location='France')"},
    22: {"get_machine_state", "get_weather(location='New York')"},
    23: {"validate_switch", "get_machine_state"},
    24: {"get_population(location='China')", "setup_meeting(persons=10, time='9 AM')"},
    25: {"get_weather(location='Sydney')", "get_machine_state"},
    26: {"setup_meeting(persons=3, time='7 PM')", "get_population(location='Germany')"},
    27: {"get_weather(location='Rome')", "validate_switch"},
    28: {"get_machine_state", "get_weather(location='Berlin')"},
}

WRONG_TOOL_MAP = {
    # conservative list of tools that were observed to be incorrectly called in the report
    4: {"get_machine_state"},        # P5 — expected no call, some models called get_machine_state
    9: {"schedule_meeting"},         # P10: meeting-related tool wrongly invoked
    10: {"get_weather"},             # P11: a model called get_weather when not expected
    11: {"get_weather"},             # P12: weather was invoked incorrectly
    26: {"setup_meeting"},           # P27 — at least one model called setup_meeting with wrong args
    29: {"get_machine_state", "validate_switch"}  # P30 — some models incorrectly called these
}

BACKEND_DISPLAY = {
    "ollama":     ("Ollama",     "native-tools"),
    "ollama_raw": ("Ollama",     "raw-schema"),
    "bitnet":     ("bitnet.cpp", "openai-compat"),
    "llamacpp":   ("llama.cpp",  "openai-compat"),
}

def get_backend_display(model_info: dict):
    return BACKEND_DISPLAY[model_info['backend']]

# USLMs to benchmark
MODELS = [
    {"name": "qwen2.5:3b",      "backend": "ollama",  "origin": "CN"},
    {"name": "qwen2.5:1.5b",    "backend": "ollama",  "origin": "CN"},
    {"name": "qwen2.5:0.5b",    "backend": "ollama",  "origin": "CN"},
    {"name": "llama3.2:3b",     "backend": "ollama",  "origin": "US"},
    {"name": "smollm2:1.7b",    "backend": "ollama",  "origin": "US"},
    {"name": "ministral-3:3b",  "backend": "ollama",  "origin": "FR"},
    {"name": "deepseek-r1:1.5b","backend": "ollama_raw",  "origin": "CN"},
    {"name": "gemma3:1b",       "backend": "ollama_raw",  "origin": "US"},
    {"name": "phi4-mini:3.8b",  "backend": "ollama_raw",  "origin": "US"},
    {"name": "bitnet-3B",       "backend": "bitnet",  "origin": "US/1bit",
     "model_path": "/home/mike/projects/bitnet/models/bitnet_b1_58-3B/ggml-model-i2_s.gguf"},
    {"name": "bitnet-2B-4T",    "backend": "bitnet",  "origin": "US/1bit",
     "model_path": "/home/mike/projects/bitnet/models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf"},
    {"name": "qwen3:0.6b",      "backend": "ollama",  "origin": "CN"},
    {"name": "qwen3:1.7b",      "backend": "ollama",  "origin": "CN"},
{"name": "functiongemma",    "backend": "ollama",  "origin": "US"},
    {"name": "granite3.3:2b",   "backend": "ollama",  "origin": "US"},
    {"name": "llama3.2:1b",     "backend": "ollama",  "origin": "US"},
    {"name": "lfm2.5:1.2b",    "backend": "llamacpp", "origin": "US",
     "model_id": "LiquidAI/LFM2.5-1.2B-Instruct-GGUF"},
    {"name": "granite4:3b",    "backend": "ollama",  "origin": "US"},
    {"name": "smollm3:3b",     "backend": "ollama_raw",  "origin": "US"},
    {"name": "jan-v3:4b",      "backend": "ollama_raw",  "origin": "US"},
    {"name": "nanbeige4.1:3b", "backend": "llamacpp", "origin": "CN",
     "model_id": "Edge-Quant/Nanbeige4.1-3B-Q4_K_M-GGUF"},
]