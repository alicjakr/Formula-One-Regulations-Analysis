import fastf1
import os

fastf1.Cache.enable_cache(os.path.join(os.path.dirname(__file__), '..', '..', 'cache'))

def get_common_events():
    season_2025 = fastf1.get_event_schedule(2025)
    season_2026 = fastf1.get_event_schedule(2026)

    events_2025 = set(season_2025['EventName'].values)
    events_2026 = set(season_2026['EventName'].values)
    events = events_2025.intersection(events_2026)

    return sorted(list(events))

def get_common_drivers(gp: str, session_type: str):
    session_2025 = load_session(2025, gp, session_type)
    session_2026 = load_session(2026, gp, session_type)

    drivers_2025 = set(session_2025.drivers)
    drivers_2026 = set(session_2026.drivers)

    drivers = drivers_2025.intersection(drivers_2026)
    return sorted(list(drivers))

def load_session(year: int, gp: str, session_type:str):
    session = fastf1.load_session(year, gp, session_type)
    session.load()
    return session