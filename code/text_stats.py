#!/usr/bin/env python3
"""文本词频统计程序：读取一个文本文件，统计词频并输出前 N 个高频词。

用法:
    python text_stats.py <文件路径> [--top N]
"""

import sys
import re
from collections import Counter


def count_words(filepath: str, top_n: int = 10) -> list[tuple[str, int]]:
    """读取文件，分词并返回词频最高的 top_n 个词。"""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()
    # 提取英文单词（连续字母数字），中文按字拆分
    words = re.findall(r"[a-z0-9]+", text)
    if not words:
        # 尝试按中文字符统计
        words = re.findall(r"[\u4e00-\u9fff]", text)
    counter = Counter(words)
    return counter.most_common(top_n)


def main() -> None:
    if len(sys.argv) < 2:
        print("用法: python text_stats.py <文件路径> [--top N]")
        sys.exit(1)

    filepath = sys.argv[1]
    top_n = 10
    if "--top" in sys.argv:
        idx = sys.argv.index("--top")
        top_n = int(sys.argv[idx + 1])

    results = count_words(filepath, top_n)
    print(f"文件: {filepath}")
    print(f"词频统计 (前 {top_n} 名):")
    print("-" * 30)
    for word, count in results:
        print(f"  {word:<15} {count:>5}")


if __name__ == "__main__":
    main()
