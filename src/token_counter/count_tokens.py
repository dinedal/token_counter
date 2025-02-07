from transformers import AutoTokenizer
from typing import Optional


def count_tokens(
    text: str, model_name: str = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
) -> int:
    """
    Count the number of tokens in a text string using a specified model's tokenizer.

    Args:
        text: The input text to tokenize and count
        model_name: The name of the model whose tokenizer to use. Defaults to DeepSeek.

    Returns:
        The number of tokens in the input text
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text)
    return len(tokens)
