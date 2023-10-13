from numpy import sqrt, pi, cos, deg2rad

def create_orbit_param(body_radius: float, r: float, rmax: float, rmin: float, i: float) -> list:
    """Create a list of orbit parameters for a given body.
    
    Args:
        body_radius (float): Radius of the celestial body (in meters).
        r (float): Current radial distance from the body's center (in meters).
        rmax (float): Maximum radial distance (apoapsis) from the body's center (in meters).
        rmin (float): Minimum radial distance (periapsis) from the body's center (in meters).
        i (float): Inclination of the orbit (in degrees).

    Returns:
        list: List of orbit parameters [r, rmax, rmin, i] with distances in meters and inclination in degrees.
    """
    return [r + body_radius, rmax + body_radius, rmin + body_radius, i]

def vis_viva(mu: float, orbit_param: list) -> float:
    """Calculate the orbital velocity using the vis-viva equation.

    Args:
        mu (float): Gravitational parameter of the celestial body.
        orbit_param (list): List of orbit parameters [r, rmax, rmin, i].

    Returns:
        float: The orbital velocity (in meters per second).
    """
    r, rmax, rmin, i = orbit_param
    a = (rmax + rmin) / 2  # Semi-major axis (m)
    orbit_type = "circular" if rmax == rmin else "elliptical"
    v = sqrt(mu / a) if orbit_type == "circular" else sqrt(mu * (2 / r - 1 / a))
    return round(v, 2)

def hohmann(mu: float, orbit_param1: list, orbit_param2: list) -> dict:
    """Perform a Hohmann transfer between two orbits.

    Args:
        mu (float): Gravitational parameter of the celestial body.
        orbit_param1 (list): List of orbit parameters for the initial orbit.
        orbit_param2 (list): List of orbit parameters for the target orbit.

    Returns:
        dict: A dictionary containing Hohmann transfer information:
            - 'dV1': Delta-V for the first burn (in meters per second).
            - 'dV2': Delta-V for the second burn (in meters per second).
            - 'dV_total': Total Delta-V for the transfer (in meters per second).
            - 'time_taken': Time taken for the transfer (in seconds).
    """
    r1, rmax1, rmin1, i1 = orbit_param1
    r2, rmax2, rmin2, i2 = orbit_param2
    i = i2 - i1
    v1 = vis_viva(mu, orbit_param1)
    v2 = vis_viva(mu, orbit_param2)

    if rmax1 < rmax2 and rmax2 == rmin2:
        orbit_param_injection = [r2, r2, r1, i1]
        vea = vis_viva(mu, orbit_param_injection)
        dV1 = vea - v1  # Injection burn
        if i == 0:
            dV2 = vep - v2  # Circularization burn
        else:
            dV2 = sqrt(v1 ** 2 + vea ** 2 - 2 * v1 * vea * cos(deg2rad(i)))
    elif rmax1 > rmax2 and rmax2 == rmin2:
        orbit_injection_apoapsis = [rmax1, rmax1, rmax2, i2]
        orbit_injection_periapsis = [rmax2, rmax1, rmax2, i2]
        vea = vis_viva(mu, orbit_injection_apoapsis)
        if i == 0:
            dV1 = vea - v1
        else:
            dV1 = sqrt(v1 ** 2 + vea ** 2 - 2 * v1 * vea * cos(deg2rad(i)))
        vep = vis_viva(mu, orbit_injection_periapsis)
        dV2 = vep - v2

    dV_total = dV1 + dV2
    time_taken = pi * sqrt((r1 + r2) ** 3 / (8 * mu))  # Time to transfer in seconds

    hohmann_info = {
        "dV1": round(dV1, 2),
        "dV2": round(dV2, 2),
        "dV_total": round(dV_total, 2),
        "time_taken": round(time_taken, 2),
    }
    return hohmann_info

# Example orbit parameters and Hohmann transfer calculation
orbit1 = create_orbit_param(6.3781e6, 9e7, 9e7, 290000, 0)
orbit2 = create_orbit_param(6.3781e6, 3.5786e7, 3.5786e7, 3.5786e7, 22.5)
hohmann_result = hohmann(3.98e14, orbit1, orbit2)

print(hohmann_result)

