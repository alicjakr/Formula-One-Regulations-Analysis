import numpy as np

from . import loader

def get_telemetry(year: int, gp: str, session_type: str, driver: str):
    session = loader.load_session(year, gp, session_type)
    lap = session.laps.pick_driver(driver).pick_fastest()
    tel = lap.get_telemetry()

    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return {
        'segments': segments,
        'telemetry': tel,
        'laps': lap,
    }

# def get_lap_telemetry(driver: str, session: str):
