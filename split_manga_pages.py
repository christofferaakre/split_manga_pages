#!/usr/bin/env python3
import sys
import argparse
import pathlib
import statistics
import cv2
from enum import Enum, auto
from collections import Counter
from utils import is_double_page_spread
from time import perf_counter

EXTENSIONS = {'.png', '.jpg', '.jpeg'}
MODE_ALL = 'all'
MODE_DETECT = 'detect'
MODE_HELP = """Which mode the script should use. 'all' assumes all images are
double page spreads and splits them all into two single page images each, and
saves the new images in a new directory called split_manga_pages, i.e. does not modify the original directory.
This mode should be used when you have a manga formatted as all double page images
and you want to convert them all to single page.
specified. 'detect' uses the resolution of the images provided to detect double page spreads, and splits them into
two single page spreads each, preserving the original two page spreads as well.
Both modes name the split pages such that they sort correctly with the other
pages, for example page0034.png will get split into page0034_1.png and page0034_2.png.
This mode should be used when you have some single page and some double page
images and you want to have single page versions fo the doble page spreads
directly following the double page version"""

def main():
    parser = argparse.ArgumentParser(description="Command line utility to split double page manga into single page")
    parser.add_argument('-d', '--directory', help="Directory containig image files to split")
    parser.add_argument('-m', '--mode', help=MODE_HELP, choices=[MODE_ALL, MODE_DETECT])
    parser.add_argument('-nk', '--no-keep', help="When using the 'detect' mode, do not keep the double page spreads", action='store_true', dest="no_keep")
    args =  parser.parse_args()

    directory = args.directory
    mode = args.mode
    no_keep = args.no_keep
    if not directory or not mode:
        parser.print_usage()
        sys.exit(1)

    split_manga_pages(directory, mode, no_keep)

def split_manga_pages(directory: str, mode: str, no_keep: bool) -> None:
    f"""
    Given a directory, converts the images contained in that directory
    from double page layout to single page layout.
    Arguments:
    directory: str -  The directory containing the image files
    mode: {MODE_HELP}
    no_keep: bool - If True, do not keep double page spreads when using detect mode
    """

    path = pathlib.Path(directory)
    save_directory: pathlib.Path
    if mode == MODE_ALL:
        save_directory = path / 'split_manga_pages'
        save_directory.mkdir(exist_ok=True)
    elif mode == MODE_DETECT:
        save_directory = path

    files = sorted(list(p for p in path.glob('**/*') if p.suffix in EXTENSIONS and (p.parents[0] != save_directory or mode == MODE_DETECT)))
    print(f"Found {len(files)} images")
    mean, std = 0, 0
    if mode == MODE_DETECT:
        print("Calculating mean and standard deviations of image widths..")
        images = [cv2.imread(str(file)) for file in files]
        widths = Counter([img.shape[1] for img in images])
        mean = statistics.mean(widths.elements())
        std = statistics.stdev(widths.elements())
        print(f"Mean width in pixels is {mean} and standard deviation is {std}")

    n_split = 0
    n_delete = 0
    for file in files:
        # get filename without suffix
        filename = file.stem
        img = cv2.imread(str(file))
        height, width = img.shape[0], img.shape[1]
        if mode != MODE_ALL:
            if is_double_page_spread(width, mean ,std):
                print(f"Detected double page spread (width {width}): {str(file)}")
            else:
                continue
        width_cutoff = width // 2
        page1 = img[:, width_cutoff:]
        page2 = img[:, :width_cutoff]

        filename1 = f'{filename}part1{file.suffix}'
        filename2 = f'{filename}part2{file.suffix}'

        save_path1: pathlib.Path = save_directory / filename1
        save_path2: pathlib.Path = save_directory / filename2

        if save_path1.exists() or save_path2.exists():
            print(f"A file named {str(save_path1)} or {str(save_path2)} already exists. Not overwriting\n")
            continue

        cv2.imwrite(str(save_path1), page1)
        cv2.imwrite(str(save_path2), page2)
        if mode == MODE_DETECT and no_keep:
            print(f"""Deleting double page spread {str(file)}
                    since it has been split into single page files and the --no-keep flag was used""")
            file.unlink()
            n_delete += 1

        n_split += 1

    print(f"Done! Split {n_split} double page spreads into {2 * n_split} single page images.")
    if mode == MODE_ALL:
        print(f"Your single page layed-out manga can be found in the directory called split_manga_pages")
    if mode == MODE_DETECT:
        print(f"The split pages were placed in the same folder as your original manga. {n_delete} files were deleted.")

if __name__== '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Ran in {end - start} seconds")
