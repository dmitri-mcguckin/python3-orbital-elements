from __future__ import annotations
import enum
import math
import pytz
import datetime as dt

_GM = 398600.4418
_SEC_PER_DAY = 86400
_2PI = 2 * math.pi
_RAD = float(math.pi / 180)
_DEG = float(180 / math.pi)
_MAX_ITTERATIONS = 500
_MAX_ACCURACY = 1e-4


class Classification(enum.Enum):
    UNCLASSIFIED = 'U'
    CLASSIFIED = 'C'
    SECRET = 'S'


class Tle:
    def __init__(self: Tle, lines: [str]):
        # Both Lines
        self.norad_id = lines[0][2:7]
        self.checksums = (Tle.checksum(lines[0]), Tle.checksum(lines[1]))

        # Line 1
        self.classification = Classification(lines[0][7])
        self.designator_year = int(lines[0][9:11])
        self.launch_number = int(lines[0][11:14])
        self.launch_piece = lines[0][14]
        self.epoch_year = int(lines[0][18:20])
        self.epoch_day = float(lines[0][20:32])
        self.ballistic_coefficient = float(lines[0][33:43])
        self.dx_ballistic_coefficient = Tle.dpa_to_float(lines[0][44:52])
        self.radiation_pressure_coefficient = Tle.dpa_to_float(lines[0][53:61])
        self.ephemeris_type = int(lines[0][62])
        self.element_set_number = int(lines[0][64:68])

        # Line 2
        self.inclination = float(lines[1][8:16])
        self.right_of_ascension = float(lines[1][17:25])
        self.eccentricity = float(lines[1][26:33]) * 0.0000001
        self.perigee = float(lines[1][34:42])
        self.mean_anomaly = float(lines[1][43:51])
        self.mean_motion = float(lines[1][52:63])
        self.revolutions = int(lines[1][63:68])

        # Calculations
        base_year = 2000 if(self.epoch_year < 70) else 1900
        year = base_year + self.epoch_year

        date = dt.datetime(year=year, month=1, day=1, tzinfo=pytz.utc) \
            + dt.timedelta(days=self.epoch_day - 1)

        self.elapsed_time = dt.datetime.now(pytz.utc) - date
        elapsed_sec = self.elapsed_time.days * _SEC_PER_DAY \
            + self.elapsed_time.seconds \
            + (math.pow(10, -6) * self.elapsed_time.microseconds)

        self.motion_per_second = self.mean_motion \
            * (_2PI * _SEC_PER_DAY)
        self.mean_anomaly += elapsed_sec * self.motion_per_second
        self.period = _SEC_PER_DAY * (1 / self.mean_motion)
        self.semi_major_axis = (((self.period / _2PI) ** 2) * _GM) ** (1/3)

        # Eccentric Anomaly
        e0 = self.mean_anomaly * _RAD
        for x in range(_MAX_ITTERATIONS):
            self.eccentric_anomaly = e0 - \
                ((e0 - self.eccentricity * math.sin(e0) - self.mean_anomaly)
                    / float(1 - self.eccentricity * math.cos(e0)))
            diff = math.fabs(self.eccentric_anomaly - e0)
            if(diff < _MAX_ACCURACY):
                break

        self.eccentric_anomaly *= _DEG

        # True anomaly
        upper = math.sqrt(1 + self.eccentricity) \
            * math.sin(self.eccentric_anomaly / 2.0)
        lower = math.sqrt(1 - self.eccentricity) \
            * math.cos(self.eccentric_anomaly / 2.0)

        self.true_anomaly = 2 * math.atan2(upper, lower)
        self.true_anomaly *= _DEG

    # Static functions
    def dpa_to_float(val: str) -> float:
        base = float(f'0.{val[1:6]}')
        if(val[0] == '-'):
            base *= -1
        exponent = math.pow(10, int(val[-2:]))
        return base * exponent

    def checksum(line: str) -> int:
        sum = 0
        for c in line[:-1]:
            if(c.isnumeric()):
                sum += int(c)
            elif(c == '-'):
                sum += 1
        return sum % 10
