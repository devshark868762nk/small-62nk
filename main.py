"""Minimal responsive component library.

Provides helper functions to generate simple responsive HTML components.
"""

def responsive_div(content="", classes="", style=""):
    """Return a div with responsive classes."""
    return f'<div class="responsive {classes}" style="{style}">{content}</div>'

def responsive_img(src, alt="", width="100%", max_width="600px"):
    """Return an img tag that scales responsively."""
    return (
        f'<img src="{src}" alt="{alt}" '
        f'style="width: {width}; max-width: {max_width}; height: auto;" />'
    )

def responsive_grid(items, columns=2):
    """Return a responsive grid container with given items."""
    grid_style = f"display: grid; gap: 10px; grid-template-columns: repeat({columns}, 1fr);"
    items_html = "".join(f'<div>{item}</div>' for item in items)
    return f'<div style="{grid_style}">{items_html}</div>'

def main():
    print("Responsive Div:")
    print(responsive_div("Hello, world!", "my-class", "border:1px solid #000;"))
    print("\nResponsive Image:")
    print(responsive_img("https://example.com/image.jpg", "Example", "100%"))
    print("\nResponsive Grid:")
    print(responsive_grid([f"Item {i}" for i in range(1,5)], columns=3))

if __name__ == "__main__":
    main()