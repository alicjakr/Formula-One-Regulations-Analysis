import fastf1

def load_session(year: int, gp: str, session_type:str):
    session = fastf1.load_session(year, gp, session_type)
    session.load()
    return session