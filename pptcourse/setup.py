from setuptools import setup, find_packages

setup(
    name="pptcourse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-webserver",
        "requests",
        "openai",
        "python-pptx"
    ],
    extras_require={
        "dev": ["pytest"]  # Development dependencies
    },
    entry_points={
        "console_scripts": [
            "pptcourse-run=pptcourse.main:run_pipeline",
        ]
    },
    author="Vikrant Bhosale",
    description="A workflow for generating PowerPoint presentations using APIs like DeepSeek and OpenAI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vikrantb/pptcourse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)