import numpy as np

from . import loader

def get_telemetry(session, driver: str):
    lap = session.laps.pick_driver(driver).pick_fastest()
    return lap.get_telemetry()

def get_lap_telemetry(session, driver: str):
    tel = get_telemetry(session, driver)
    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return {
        'segments': segments,
        'telemetry': tel,
        'laps': session.laps.pick_driver(driver).pick_fastest(),
    }

