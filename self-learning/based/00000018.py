def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        cut_str = instructions.replace("Simon says", "").strip()
        return f"I {cut_str}"
    return "I won't do it!"    
    