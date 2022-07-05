import os
import re

from dotenv import load_dotenv
from github import Github
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)


def get_readme_image(repo):
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


@app.route('/')
async def index():
    return render_template('index.jinja2')


@app.route('/projects')
async def project_page():
    git = Github(os.environ.get('GITHUB'))
    user = git.get_user('glitchchan')
    repos = []
    for repo in user.get_repos():
        if not repo.fork and not repo.name.lower() == "glitchchan":
            repos.append(repo)
    return render_template('projects.jinja2', repos=repos, get_readme_image=get_readme_image)


if __name__ == '__main__':
    app.run()
