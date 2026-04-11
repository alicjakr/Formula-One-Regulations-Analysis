import fastf1
import loader

def get_speed(year: int, gp: str, session_type: str, driver: str):
    session = loader.load_session(year, gp, session_type)
    lap = session.laps.pick_driver(driver).pick_fastest()
    tel = lap.get_telemetry()
    speed = tel['Speed'].to_numpy().astype(float)

