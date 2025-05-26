def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdowns = markdown.split("\n\n")
    blocks = []
    for split_markdown in split_markdowns:
        if split_markdown == "":
          continue
        else:
          blocks.append(split_markdown.strip())
    return blocks