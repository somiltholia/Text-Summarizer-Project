import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "somiltholia"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "somiltholia01@gmail.com"



setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,           # Initial version
    author=AUTHOR_USER_NAME,        # Your name
    author_email=AUTHOR_EMAIL,  # Your email
    description="A small python package for CNN app",  # Short description
    long_description=long_description,  # Long description from README
    long_description_content="text/markdown",  # Markdown format for long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repo
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  # Automatically find and include all packages in the project
)