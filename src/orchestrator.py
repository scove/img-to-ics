from PIL import Image
import pytesseract
import logging
from src.parse import arg_parser


def main():
    cli_input = arg_parser()
    logging.warning(cli_input)


main()