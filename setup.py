import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"

REPO_NAME = "Chicken_Disease_Project_Deployment"
AUTHOR_USER_NAME = "amitkumar47"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "amits4787@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    versin = __version__,
    author= AUTHOR_USER_NAME, 
    author_email= AUTHOR_EMAIL, 
    description=" "
    long_description= long_description,
    long_description_content ="text/markdown"
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")


)