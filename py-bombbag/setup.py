import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bombbag", # Replace with your own username
    version="0.0.1",
    author="Weihong Xu",
    author_email="xuweihong.cn@gmail.com",
    description="personal toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/link89/bomb-bag",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'fire',
        'opencv-python-headless == 3.4.2.16',
        'opencv-contrib-python-headless == 4.1.2.30',
        'numpy',
        'matplotlib',
    ],
)
