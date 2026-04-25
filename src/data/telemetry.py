import numpy as np

def get_telemetry(session, driver: str):
    lap = session.laps.pick_drivers(driver).pick_fastest()
    if lap is None:
        return None
    return lap.get_telemetry(frequency=50)

def get_lap_telemetry(session, driver: str):
    tel = get_telemetry(session, driver)
    if tel is None:
        return None
    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return {
        'segments': segments,
        'telemetry': tel,
        'lap': session.laps.pick_drivers(driver).pick_fastest(),
        'year': str(session.date)[:4],
        'session': session,
    }