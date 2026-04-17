from functools import lru_cache

import fastf1
import os

fastf1.Cache.enable_cache(os.path.join(os.path.dirname(__file__), '..', '..', 'cache'))

def get_common_events():
    season_2025 = fastf1.get_event_schedule(2025)
    season_2026 = fastf1.get_event_schedule(2026)

    events_2025 = set(season_2025['EventName'].values)
    events_2026 = set(season_2026['EventName'].values)
    events = events_2025.intersection(events_2026)

    return list(events)

def get_common_drivers(gp: str, session_type: str):
    try:
        session_2025 = load_session(2025, gp, session_type)
        session_2026 = load_session(2026, gp, session_type)
    except Exception as e:
        print(f"Failed to load session: {e}")
        return []

    drivers_2025 = set(session_2025.drivers)
    drivers_2026 = set(session_2026.drivers)

    if not drivers_2026:
        print(f"No drivers available for {gp} 2026")
        return []

    dvs_2025 = {session_2025.get_driver(d)['Abbreviation'] for d in drivers_2025}
    dvs_2026 = {session_2026.get_driver(d)['Abbreviation'] for d in drivers_2026}

    drivers = dvs_2025.intersection(dvs_2026)
    return list(drivers)


@lru_cache(maxsize=20)
def load_session(year: int, gp: str, session_type: str):
    session = fastf1.get_session(year, gp, session_type)
    session.load(weather=False, messages=False)
    return session