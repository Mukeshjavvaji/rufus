from setuptools import setup, find_packages

setup(
    name="chima_rufus",  # Package name
    version="0.1",  # Version number
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[  # Required dependencies
        "requests",
        "beautifulsoup4",
        "fastapi",
        "uvicorn"
    ],
    entry_points={  # Command-line entry point
        "console_scripts": [
            "mycrawler-api = mycrawler.api:app"
        ]
    },
)
