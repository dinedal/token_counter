import sys
import argparse
from token_counter import count_tokens


def main():
    parser = argparse.ArgumentParser(
        description="Count tokens in text using model's tokenizer"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="input file (default: stdin)",
    )
    parser.add_argument(
        "-m", "--model-name", default="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
    )
    args = parser.parse_args()

    text = args.file.read()
    num_tokens = count_tokens(text, model_name=args.model_name)
    print(num_tokens)


if __name__ == "__main__":
    main()
