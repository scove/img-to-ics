import argparse

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Image to Calendar',
        description='Attempts to translate an image of a calendar to an ICS file.'
    )

    parser.add_argument(
        "-i", "--image",
        required=True,
        type=str,
        dest="image"
    )
    args = parser.parse_args()
    return args