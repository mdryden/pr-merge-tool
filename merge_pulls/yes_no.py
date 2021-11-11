from merge_pulls.output import print_highlight


def yes_no(question, default_yes=False):
    prompt = "(Y/n)" if default_yes else "(y/N)"
    choices = {"y": True, "n": False}

    while True:
        print_highlight(f"{question} {prompt}")
        choice = input().lower()

        if not choice and default_yes:
            choice = "y"

        if not choice and not default_yes:
            choice = "n"

        if choice in choices:
            return choices[choice]
