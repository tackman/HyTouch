import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hytouch",
    version="0.0.1",
    author="tackman",
    author_email="tackman@tackman.info",
    description="Local python module managing frontend for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tackman/HyTouch/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['hy'],
    python_requires='>=3.7',
    scripts=['src/hytouch'],
)
