# token-counter

A simple Python CLI tool for counting tokens in text using model tokenizers from Hugging Face transformers.

Useful for checking if your input will fit in your context window.

## Installation

```bash
pip install token-counter
```

## Usage

Count tokens from stdin:
```bash
echo "Hello, world!" | token-counter
```

Count tokens from a file:
```bash
token-counter input.txt
```

Use a specific model's tokenizer:
```bash
token-counter input.txt --model-name gpt2
```

## Options

- `file`: Input file (default: stdin)
- `-m, --model-name`: Model name from Hugging Face Hub (default: deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)

## Requirements

- Python >= 3.10
- transformers >= 4.48.3

## License

MIT - See LICENSE file for details.
