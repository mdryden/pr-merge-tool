import os
from rich import print
from merge_pulls.output import print_error

from merge_pulls.yes_no import yes_no


def display_warning():
    has_accepted = os.path.isfile(".accepted_warning")

    if not has_accepted:
        print(":police_car_light: [bold red]WARNING![/bold red] :police_car_light:")
        print("This tool performs some steps which are potentially destructive.\n")
        print("Please ensure you understand what happens before using this tool.")
        print("")
        print("Steps:")
        print("1. Checkout the main branch of the repository")
        print("2. Pull from origin")
        print("3. If a local copy of the target branch already exists, remove it")
        print("4. Show a list of pull requests for the repository")
        print("5. Squash each selected pull into the new local target branch")
        print("6. Force push the local target branch up to origin")
        print("")
        print("Please confirm you understand and wish to continue.")
        confirmed = yes_no("Continue?")

        if confirmed:
            with open(".accepted_warning", "w") as writer:
                writer.write("")
        else:
            print_error("Aborted", should_exit=True)
