color_prefix_by_role = {
    "system": "\033[0m",  # gray
    "user": "\033[0m",  # gray
    "assistant": "\033[34m",  # blue,
    "function": "\033[35m" # magenta
}


def print_messages(messages, color_prefix_by_role=color_prefix_by_role) -> None:
    """Prints messages sent to or from GPT."""
    for message in messages:
        role = message["role"]
        color_prefix = color_prefix_by_role[role]
        content = message["content"]
        print(f"{color_prefix}\n[{role}]\n{content}")
        
