#!/usr/bin/env python3
import argparse
import pathlib
import cv2

EXTENSIONS = {'.png', '.jpg', '.jpeg'}

def main():
    parser = argparse.ArgumentParser(description="Command line utility to split double page manga into single page")
    parser.add_argument('-d', '--directory', help="Directory containig image files to split")
    args =  parser.parse_args()

    directory = args.directory
    if not directory:
        parser.print_usage()
        exit(1)

    split_manga_pages(directory)


def split_manga_pages(directory: str) -> None:
    path = pathlib.Path(directory)
    save_directory = path / 'split_manga_pages'
    save_directory.mkdir(exist_ok=True)

    files = sorted(list(p for p in path.glob('**/*') if p.suffix in EXTENSIONS))
    for file in files:
        # get filename without suffix
        filename = file.stem
        img = cv2.imread(str(file))
        height, width = img.shape[0], img.shape[1]
        width_cutoff = width // 2
        print(img.shape)
        page1 = img[:, :width_cutoff]
        page2 = img[:, width_cutoff:]

        filename1 = f'{filename}_1{file.suffix}'
        filename2 = f'{filename}_2{file.suffix}'

        cv2.imwrite(str(save_directory / filename1), page1)
        cv2.imwrite(str(save_directory / filename2), page2)

        print(f'original filename: {filename}')
        print(f'filename 1: {filename1}')
        print(f'filename 2: {filename2}')



if __name__== '__main__':
    main()
