from setuptools import setup, find_packages

with open("README.md") as fh:
    README = fh.read()

setup(
    name="Xplique",
    version="0.0.1",
    description="Fast generation of explanations for Tensorflow",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Thomas FEL",
    author_email="thomas.fel@irt-saintexupery.com",
    # url="https://github.com/napolar",
    license="MIT",
    install_requires=['tensorflow>=2.1.0', 'numpy', 'opencv-python>=4.1.0'],
    extras_require={
        "tests": ["pytest", "pylint"],
        "docs": ["mkdocs", "mkdocs-material", "numkdoc"],
    },
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)