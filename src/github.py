import os
import re

from dotenv import load_dotenv
from github import Github

load_dotenv()
git = Github(os.environ.get('GITHUB'))
user = git.get_user('glitchchan')


def get_readme_image(repo) -> str | None:
    try:
        readme = repo.get_contents("README.md")
    except:
        return None

    images = re.findall(r'src="([^"]+)"', str(readme.decoded_content))
    if len(images) >= 1:
        img_url = repo.get_contents(images[0]).download_url
    else:
        return None

    return img_url


def get_repos() -> list:
    repos = []
    for repo in user.get_repos():
        if not repo.fork and not repo.name.lower() == "glitchchan":
            repos.append(repo)

    return repos
