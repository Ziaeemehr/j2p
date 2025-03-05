from setuptools import setup, find_packages

setup(
    name="j2p",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["nbformat", "nbconvert"],
    entry_points={
        "console_scripts": [
            "j2p=j2p.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple tool to convert Jupyter notebooks to Python scripts.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/j2p",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
