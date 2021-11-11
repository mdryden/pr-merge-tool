from rich import print


def print_error(message, should_exit=True):
    print(f"[bold red]{message}[/bold red]")
    if should_exit:
        exit(1)


def print_highlight(message):
    print(f"[bold yellow]{message}[/bold yellow]")
