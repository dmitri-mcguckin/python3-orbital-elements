import argparse
import orbital_elements as oe
from .tle import Tle
# from .orbital_graph import plot_orbit


def main() -> None:
    parser = argparse.ArgumentParser(prog=oe.APP_NAME,
                                     description=oe.APP_DESCRIPTION,
                                     allow_abbrev=False)
    parser.add_argument('tle_filepath',
                        type=str,
                        help='path to a TLE file to plot')
    parser.add_argument('-c', '--checksum',
                        dest='checksum',
                        action='store_true',
                        default=False,
                        help='Run the checksum on both lines in the TLE and'
                        ' display the vailidity.')
    args = parser.parse_args()

    # Parse the file
    with open(args.tle_filepath, 'r') as file:
        lines = file.read().split('\n')[:-1]
    tle = Tle(lines)

    if(args.checksum):
        vaild = [
            tle.checksums[0] == int(lines[0][-1]),
            tle.checksums[1] == int(lines[1][-1])
        ]

        for i, is_valid in enumerate(vaild):
            print(f'Line {i + 1}: {"VALID" if is_valid else "INVALID"}')

            if(not is_valid):
                print(f'\tExpected {tle.checksums[i]},'
                      f' but got: {lines[i][-1]}')

    # Print all the orbital details
    print(f'TLE for {tle.norad_id}')
    for k, v in tle.__dict__.items():
        print(f'\t{k}: {v}')

    # Plot orbit with matplotlib
    # plot_orbit(str(tle.norad_id), tle)
