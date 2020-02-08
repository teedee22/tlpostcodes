import geopy.distance
from pdc import Postcode


def postcodenearest(inCode, inFileName):
    code = Postcode(inCode)
    distances = []
    for row in inFileName:
        tempcode = Postcode(row)
        distances.append(
            (
                round(
                    geopy.distance.vincenty(
                        (tempcode.latitude, tempcode.longtitude),
                        (code.latitude, code.longtitude),
                    ).miles,
                    2,
                ),
                row,
            )
        )
    distances.sort()

    return (distances[0], distances[1], distances[2])


def main():
    pass


if __name__ == "__main__":
    main()
