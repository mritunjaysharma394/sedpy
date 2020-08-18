from setuptools import setup

# The text of the README file
with open("README.md", 'r') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(name="sedpy",
      version="1.0.0",
      description="Cross-platform stream-line editing tool",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/mritunjaysharma394/sedpy",
      author="Mritunjay Sharma",
      author_email="mritunjaysharma394@gmail.com",
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8"
      ],
      packages=["sedpy"],
      include_package_data=True,
      entry_points={'console_scripts': ['sedpy = sedpy.__main__:main']})
