import argparse
import orbital_elements as oe
from .tle import Tle
from .orbital_graph import plot_orbit


def main():
    parser = argparse.ArgumentParser(prog=oe.APP_NAME,
                                     description=oe.APP_DESCRIPTION,
                                     allow_abbrev=False)
    parser.add_argument('tle_filepath',
                        type=str,
                        help='path to a TLE file to plot')
    args = parser.parse_args()

    # Parse the file
    with open(args.tle_filepath, 'r') as file:
        lines = file.read().split('\n')[:-1]
    tle = Tle(lines)

    # print(f'TLE for {tle.norad_id}')
    # for k, v in tle.__dict__.items():
    #     print(f'\t{k}: {v}')
    plot_orbit(str(tle.norad_id), tle)
