# split-manga-pages
`split-manga-pages` is a command line utility written in Python that
converts your double-page layout manga (or any images in double page layout)
to single-page layout. This can make it much easier to read said manga on
small screens, such as those found on mobile devices

## Installation
Install from pypi: `pip install split_manga_pages`
You can then run the script: `split_manga_pages -h`

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
