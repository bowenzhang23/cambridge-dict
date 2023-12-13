#!/usr/bin/env python

import argparse
import time
from query import *
from pprint import pprint


def audio_html(src):
    return f"""
<audio id="audio" controls="" preload="none">
    <source id="mp3" src="{src}">
</audio>
    """


def writeline(f, content):
    f.write(f"{content}\n\n")


def execute(f, v):
    result = query(v)
    
    title: list = result["title"]
    explain: list = result["explain"]
    explain_cn: list = result["explain_cn"]
    example: list = result["example"]
    example_cn: list = result["example_cn"]
    phrase: list = result["phrase"]
    audio_src: list = result["audio_src"]

    if len(title) < 1 and len(explain) < 1:
        return False
    elif len(title) < 1:
        title = [v.replace("-", " ")]
        
    writeline(f, f"### {title[0]}")
    for src in audio_src:
        if "uk" in src:
            writeline(f, f"{audio_html(src)}")
    for i, e in enumerate(explain):
        writeline(f, f"`Meaning:` {e}")
        writeline(f, f"`释义：` {explain_cn[i]}")
    for i, e in enumerate(example):
        writeline(f, f"*{e}*")
        writeline(f, f"*{example_cn[i]}*")
    for p in phrase:
        writeline(f, f"**{p}**")
    return True


def note(args):
    vocabularies = list()
    with open(args.input, "r") as f:
        vocabularies = [l.strip() for l in f.readlines()]
        vocabularies = [v for v in vocabularies if v != "" and not v.startswith("#")]
    with open(args.output, "w") as f:
        writeline(f, f"## {args.tag}")  # title
        for v in vocabularies:
            status = execute(f, v)
            print(f"Processed {v:20} ==> Status {status}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=str,
        default="input.txt",
        help="input text file, one vocabulary each line",
    )
    parser.add_argument(
        "output", type=str, default="output.md", help="output markdown file"
    )
    parser.add_argument(
        "-t", "--tag", type=str, default=time.asctime(), help="title/tag of the markdown"
    )
    args = parser.parse_args()
    note(args)
