from fastapi import FastAPI
from pydantic import BaseModel
from kerykeion import AstrologicalSubject, Report, KerykeionChartSVG

app = FastAPI()

class BirthDetails(BaseModel):
    name: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lng: float
    lat: float
    tz_str: str
    city: str

@app.post("/astrology-report")
def astrology_report(details: BirthDetails):
    person = AstrologicalSubject(
        details.name, details.year, details.month, details.day, 
        details.hour, details.minute, lng=details.lng, lat=details.lat, 
        tz_str=details.tz_str, city=details.city, 
        zodiac_type="Sidereal", sidereal_mode="LAHIRI"
    )
    report = Report(person)
    chart = KerykeionChartSVG(person)
    
    return {
        "planets": {planet: vars(getattr(person, planet)) for planet in [
            "sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", 
            "uranus", "neptune", "pluto", "mean_node", "true_node", 
            "mean_south_node", "true_south_node", "chiron", "mean_lilith", 
            "ascendant", "descendant", "medium_coeli", "imum_coeli"
        ]},
        "houses_positions": {f"{house}_house": vars(getattr(person, f"{house}_house")) for house in [
            "first", "second", "third", "fourth", "fifth", "sixth", 
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
        ]}
    }
