from stack import Stack
import re  # Importing at the top for better readability


def check_less_more_sign(html):
    """Check if the HTML has balanced less than and greater than signs."""
    less_than_count = 0
    greater_than_count = 0
    for char in html:
        if char == '<':
            less_than_count += 1
        elif char == '>':
            greater_than_count += 1
        # If at any point there are more '>' than '<', it's invalid
        if greater_than_count > less_than_count:
            return False
    # Final check for balance
    return less_than_count == greater_than_count


def extract_tags(html):
    """Extract tag names from the HTML."""
    return re.findall(r'<?([/a-zA-Z0-9-]+)?>', html)  # Updated regex


def check_valid_html(html):
    """Check if the HTML document has valid opening and closing tags."""
    stacks = Stack()
    self_closing_tags = {"br", "hr", "img", "input", "meta", "link", "base", "source", "track"}

    if not check_less_more_sign(html):
        raise ValueError("Unbalanced <> in HTML file")

    tags = extract_tags(html)
    print(tags)
    for tag in tags:
        if not tag.startswith('/'):  # Opening tags
            tag_name = tag
            if tag_name not in self_closing_tags:
                stacks.push(tag_name)
                print(f"Pushed: {tag_name} | Stack now: {stacks}")  # Debugging line
        else:
            tag_name = tag[1:]  # Remove '/'
            if stacks.is_empty() or stacks.peek() != tag_name:
                return False  # Mismatch or no opening tag
            stacks.pop()  # Proper match, pop from stack
            print(f"Popped: {tag_name} | Stack now: {stacks}")  # Debugging line

    return stacks.is_empty()  # Check if all opening tags were matched


if __name__ == '__main__':
    html_document = """
        <html>
            <head>
                <title>
                    Example
                </title>
            </head>
            <body>
                <h1>Hello, world</h1>
            </body>
        </html>
        """
    try:
        is_valid = check_valid_html(html_document)
        print("HTML is valid:", is_valid)
    except ValueError as e:
        print(e)
