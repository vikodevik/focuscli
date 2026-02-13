from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="focuscli",
    version="0.1.0",
    author="Enes",
    author_email="pypi.dole284@passinbox.com",
    description="A productivity CLI tool for developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eneswritescode/focuscli",
    project_urls={
        "Bug Reports": "https://github.com/eneswritescode/focuscli/issues",
        "Source": "https://github.com/eneswritescode/focuscli",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    keywords="productivity cli pomodoro task-manager todo timer focus",
    python_requires=">=3.7",
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "focuscli=focuscli.main:main",
        ],
    },
)

