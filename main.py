from transformers import AutoTokenizer
import sys
import argparse


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

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    text = args.file.read()
    tokens = tokenizer.encode(text)
    print(len(tokens))


if __name__ == "__main__":
    main()
