from src import get_readme_image, get_repos
from quart import Quart, render_template

app = Quart(__name__)


@app.route('/')
async def index():
    return await render_template('index.jinja2')


@app.route('/about')
async def about_page():
    return await render_template('about.jinja2')


@app.route('/projects')
async def project_page():
    repos = get_repos()
    return await render_template('projects.jinja2', repos=repos, get_readme_image=get_readme_image)


if __name__ == '__main__':
    app.run(debug=True)
