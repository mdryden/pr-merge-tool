import argparse


class Config:
    def __init__(self, no_checks: bool, main_branch: str, target_branch: bool):
        self.no_checks = no_checks
        self.main_branch = main_branch
        self.target_branch = target_branch

    @staticmethod
    def load_from_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--no_checks", type=int, default=0, required=False, help="Disable pre-run checks (not recommended)")
        parser.add_argument("-m", "--main_branch", type=str, default="main", required=False, help="Main branch name (default = main)")
        parser.add_argument("-t", "--target_branch", type=str, default="test", required=False, help="Target branch name (default = test)")

        args = parser.parse_args()

        return Config(
            no_checks=args.no_checks > 0,
            main_branch=args.main_branch,
            target_branch=args.target_branch,
        )

    def __str__(self):
        display = f"main_branch={self.main_branch}\n" \
            f"target_branch={self.target_branch}\n" \
            f"no_checks={self.no_checks}"
        return display
