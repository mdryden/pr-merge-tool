import requests
import merge_pulls
from merge_pulls.config import Config

config = Config.load_from_args()
merge_pulls.display_warning()

# TODO:
# run checks
# reset test
# update local working copy
# pull
# delete local copy of test branch first
