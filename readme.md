# split-manga-pages
`split-manga-pages` is a command line utility written in Python that
converts your double-page layout manga (or any images in double page layout)
to single-page layout. This can make it much easier to read said manga on
small screens, such as those found on mobile devices

## Installation
0. Make sure you have python installed:
    1. Open a terminal
    2. Try to run `python3` and `python`
    3. If either one of these give you a prompt saying
    something like `Python 3.8.10 (default, Nov 26 2021....`,
    then you are good to go
    4. If not, install Python
1. Clone repository: `git clone https://github.com/christofferaakre/split_manga_pages.git`
2. `cd` into directory: `cd split_manga_pages`
3. Install dependencies: `pip install -r requirements.txt`
4. Try to run the script: `python3 split_manga_pages.py` (If you are
on Windows you might need to type `python` instead of `python3`
5. If you get a message saying something like `usage: split_manga_pages.py [-h] [-d DIRECTORY]`,
it was installed correctly. Otherwise, you might need to install Python
or the dependencies
6. For convenience, put the script somewhere in your system path.

## Usage
Run the `split\_manga\_pages.py` script, supplying a directory of image files to convert
to single-page layout, for example:
`split-manga-pages -d /path/to/manga/name_of_manga`.
The script assumes your images are named with numbers at the end,
for example
`name_of_manga_0034.png`. That image will be split into two files named
`name_of_manga_0034_1.png` and `name_of_manga_0034_2.png`.
The files will be placed in a directory called `split_manga_pages`.
