# split-manga-pages
`split-manga-pages` is a command line utility written in Python that
converts your double-page layout manga (or any images in double page layout)
to single-page layout. This can make it much easier to read said manga on
small screens, such as those found on mobile devices

## Usage
Run the `split\_manga\_pages`, supplying a directory of image files to convert
to single-page layout, for example:
`split-manga-pages -d /path/to/manga/name_of_manga`.
The script assumes your images are named with numbers at the end,
for example
`name_of_manga_0034.png`. That image will be split into two files named
`name_of_manga_0034_1.png` and `name_of_manga_0034_2.png`.
The files will be placed in a directory called `split_manga_pages`.
