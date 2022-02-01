# split-manga-pages
`split-manga-pages` is a command line utility written in Python that
converts your double-page layout manga (or any images in double page layout)
to single-page layout. This can make it much easier to read said manga on
small screens, such as those found on mobile devices

## Installation
To install, you can download the newest executable
version for your operating system from the [Releases](https://github.com/christofferaakre/split_manga_pages/releases) section
(recommended for non-tech savvy people). Alterantively,
you can build it from source yourself, following the
[Build Instructions](#Build-instructions) section below. Or, you can follow the instructions just
below to download and run the Python script (cross-platform). The advantage of doing this
is that the executable takes can take 1-2 seconds to start up
while the Python script starts instantly, and you can also easily modify
    the script yourself without having to rebuild if you know some
    Python.
### Instructions for downloading python script
    *These steps are not requried if you download the executable from Releases or build from source*
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
Run the executable from the command line with the appropriate command line arguments
### Command line arguments
| Argument  |  Required | Description |
|:-:|---|---|
| `-d DIR, --directory DIR`  | yes |  Directory containing the image files |
| `-m, --mode`  | yes |  The mode to be used. See [Modes](#modes)|
| `-nk, --no-keep`  | no | Don't keep the original double page spreads when using detect mode |
| `-h, --help`  | no | Show help and options for the script |
### Modes
Support modes are `'all'` and `'detect'`.
#### `'all'`
Treats all images in the directory as double page spreads. Converts
them all to single page layouts, i.e. you get twice as many images as you had,
and these are put in a directory called `split_manga_pages`.
#### `'detect'`
Uses the resolutions of the images and some simple statistical analysis
to determine which images are single page spreads and which are double page. Then
splits only the double page images into single page images, and also keeps the
original double page image, so you get the original doble page image followed
by the two single page images. Images are placed in the orginal directory.

### Example
#### Mode 'all'
I have a folder called `manga` containing only double page images
with names `page001.png`, `page002.png`, etc.
I run `python3 split_manga_pages.py -d manga -m all`, and I get
a new folder called `split_manga_pages` containing files
`page001part1.png1`, `page001part2.png`, `page002part1.png`, `page002part2.png`, etc.

#### Mode 'detect'
I have a folder called `manga` containing mostly single page images,
but every so often there is a double page spread. For example,
there are files `page001.png`, `page002.png`, and `page003.png`.
`page002` is a double spread, whereas the other two are sinlge spread.
I run
`python3 split_manga_pages.py -d manga -m detect`, and now in the `manga` folder
I will find files
`page001.png`, `page002.png`, `page002part1.png`, `page002part2.png`, `page003.png`.

## Build instructions
1. Clone repository and `cd` into it
2. run `pyinstaller --onefile split-manga-pages.py`
3. The executable should be placed in the `dist` folder

Note that `pyinstaller` only builds executables for the current
operating system you are on.
