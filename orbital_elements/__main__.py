import argparse
import orbital_elements as oe


def main():
    parser = argparse.ArgumentParser(prog=oe.APP_NAME,
                                     description=oe.APP_DESCRIPTION,
                                     allow_abbrev=False)
    parser.add_argument('tle_file',
                        type=str,
                        help='path to a TLE file to plot')
    args = parser.parse_args()
    print(args)
