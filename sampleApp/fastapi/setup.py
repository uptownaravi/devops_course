from setuptools import setup

setup(
    name="uptowngithubstars",  # The name of your project
    version="0.1",  # The version of your project
    author="uptownaravi",
    author_email="uptownaravi@gmail.com",
    description="get github stats based on username",
    # py_modules=["github-stars"],  # The name of your code file
    # package_dir={"": "githubStars"},
    install_requires=["requests"],  # The dependencies of your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
