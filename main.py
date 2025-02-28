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

@app.post("/astrologydetails")
def astrology_report(details: BirthDetails):
    person = AstrologicalSubject(
        details.name, details.year, details.month, details.day, 
        details.hour, details.minute, lng=details.lng, lat=details.lat, 
        tz_str=details.tz_str, city=details.city, 
        zodiac_type="Sidereal", sidereal_mode="LAHIRI"
    )
    
    return {
        "planets": {
            "sun": vars(person.sun),
            "moon": vars(person.moon),
            "mercury": vars(person.mercury),
            "venus": vars(person.venus),
            "mars": vars(person.mars),
            "jupiter": vars(person.jupiter),
            "saturn": vars(person.saturn),
            "uranus": vars(person.uranus),
            "neptune": vars(person.neptune),
            "pluto": vars(person.pluto),
            "mean_node": vars(person.mean_node),
            "true_node": vars(person.true_node),
            "mean_south_node": vars(person.mean_south_node),
            "true_south_node": vars(person.true_south_node),
            "chiron": vars(person.chiron),
            "mean_lilith": vars(person.mean_lilith),
            "ascendant": vars(person.ascendant),
            "descendant": vars(person.descendant),
            "medium_coeli": vars(person.medium_coeli),
            "imum_coeli": vars(person.imum_coeli)
        },
        "houses_positions": {
            "first_house": vars(person.first_house),
            "second_house": vars(person.second_house),
            "third_house": vars(person.third_house),
            "fourth_house": vars(person.fourth_house),
            "fifth_house": vars(person.fifth_house),
            "sixth_house": vars(person.sixth_house),
            "seventh_house": vars(person.seventh_house),
            "eighth_house": vars(person.eighth_house),
            "ninth_house": vars(person.ninth_house),
            "tenth_house": vars(person.tenth_house),
            "eleventh_house": vars(person.eleventh_house),
            "twelfth_house": vars(person.twelfth_house)
        }
    }
