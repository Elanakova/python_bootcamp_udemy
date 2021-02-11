# function that computes the volume of a sphere given its radius
# sphere volume formula: 4/3 * pi * rad ^ 3

from math import pi
from math import pow


def compute_sphere_volume(rad):
    return (4 / 3) * pi * pow(rad, 3)


r = compute_sphere_volume(2)
print(str(r))

r = compute_sphere_volume(3)
print(str(r))