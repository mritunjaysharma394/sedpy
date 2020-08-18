# sedpy 
[![Build Status](https://travis-ci.com/mritunjaysharma394/sedpy.svg?branch=master)](https://travis-ci.com/mritunjaysharma394/sedpy)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mritunjaysharma394/sedpy/graphs/commit-activity) 
[![GitHub issues](https://img.shields.io/github/issues/mritunjaysharma394/sedpy)](https://github.com/mritunjaysharma394/sedpy/issues)
[![GitHub forks](https://img.shields.io/github/forks/mritunjaysharma394/sedpy?style=social)](https://github.com/mritunjaysharma394/sedpy/network)
[![GitHub stars](https://img.shields.io/github/stars/mritunjaysharma394/sedpy?style=social)](https://github.com/mritunjaysharma394/sedpy/stargazers) 
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


`sedpy` is a basic cross-platform alternative of `sed` built for easier and more flexible stream line editing across BSD and GNU systems.

# What is sed and what is sedpy?

The `sed` command, short for stream editor, performs editing operations on text coming from standard input or a file. sed edits line-by-line and in a non-interactive way.

This means that you make all of the editing decisions as you are calling the command, and sed executes the directions automatically. This may seem confusing or unintuitive, but it is a very powerful and fast way to transform text, especially as part of a script or automated workflow.

The problem with `sed` is that it's not purely cross-platform. Linux uses GNU-based `sed` while macOS has the BSD version of `sed`.As a result - both have quite important sytnatic and usage difference. At the same time, `sed` though exteremly powerful is quite complex to use. 

The `sedpy` project exactly tries to solve both these problems. The `sedpy` project intially supports only stream text replacement (supports regex). The future scope of the project is huge and requires continuous feedback and support from all of you amazing folks out there!

## Installation

1. Clone the repo:

        git clone https://github.com/mritunjaysharma394/sedpy.git

2. Enter the `sedpy` directory:

        cd sedpy

3. Install using:

        pip3 install -e .

This should successfully install the `sedpy` cli package.

There's a script for Step 3. To use it:

Change the access rights of `install.sh`(Required only once):

    sudo chmod a+x install.sh

and Enter:

    ./install.sh

## How to use

The project comes with a `test.txt` file. We can play with it to learn
about it's very basic usage:

The contents of `test.txt` file as of now reads:

    7 + 4 = 13

We will use `sedpy` cli to change the '4' to '6' without opening the `test.txt` file.Just enter below command and see the magic:

    sedpy "4" "6" test.txt

Now when you open `test.txt`, file will now read as:

    7 + 6 = 13

Thank you so much for having fun with this!
More updates on the project and Documentation to follow soon.
Stay Tuned!
