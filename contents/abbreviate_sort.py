import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def parse_items(contents):
    items = re.findall(r"\\item\[(.*?)\] (.*?)\\hspace\{1em\} (.*?)\n", contents)
    return items

def generate_sorted_content(sorted_items, original_contents):
    sorted_items_str = "".join([f"\\\\item[{item[0]}] {item[1]}\\\\hspace{{1em}}{item[2]}\n" for item in sorted_items])
    sorted_contents = re.sub(r"(\\begin{abbreviate}\[.*?\]\[.*?\]\n)(.*)(\\end{abbreviate})", f"\\1{sorted_items_str}\\3", original_contents, flags=re.MULTILINE | re.DOTALL)

    return sorted_contents


def write_file(file_path, contents):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)
        
def sort_items(items):
    return sorted(items, key=lambda x: x[0].lower())

def extract_items(contents):
    pattern = r"\\item\[(.*?)\] (.*?)\\hspace{1em}(.*?)\n"
    items = re.findall(pattern, contents)
    return items

def main():
    file_path = "/Users/neardws/Documents/GitHub/My-Doctoral-Dissertation/contents/abbreviate copy.tex"
    original_contents = read_file(file_path)

    sorted_items = sort_items(extract_items(original_contents))
    sorted_contents = generate_sorted_content(sorted_items, original_contents)

    output_path = "/Users/neardws/Documents/GitHub/My-Doctoral-Dissertation/contents/abbreviate sorted.tex"
    write_file(output_path, sorted_contents)

if __name__ == "__main__":
    main()

