import os

from dotenv import load_dotenv
from github import Github
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)


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
    return render_template('projects.jinja2', repos=repos)


if __name__ == '__main__':
    app.run()
