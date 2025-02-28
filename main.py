from fastapi import FastAPI
from kerykeion import AstrologicalSubject, Report, KerykeionChartSVG

app = FastAPI()

def generate_report():
    akshat = AstrologicalSubject(
        "Akshat", 2002, 9, 25, 0, 30, 
        lng=72.8777, lat=19.0760, 
        tz_str="Asia/Kolkata", city="Mumbai", 
        zodiac_type="Sidereal", sidereal_mode="LAHIRI"
    )
    report = Report(akshat)
    chart = KerykeionChartSVG(akshat)
    
    return {
      
        "planets": {
            "sun": vars(akshat.sun),
            "moon": vars(akshat.moon),
            "mercury": vars(akshat.mercury),
            "venus": vars(akshat.venus),
            "mars": vars(akshat.mars),
            "jupiter": vars(akshat.jupiter),
            "saturn": vars(akshat.saturn),
            "uranus": vars(akshat.uranus),
            "neptune": vars(akshat.neptune),
            "pluto": vars(akshat.pluto),
            "mean_node": vars(akshat.mean_node),
            "true_node": vars(akshat.true_node),
            "mean_south_node": vars(akshat.mean_south_node),
            "true_south_node": vars(akshat.true_south_node),
            "chiron": vars(akshat.chiron),
            "mean_lilith": vars(akshat.mean_lilith),
            "ascendant": vars(akshat.ascendant),
            "descendant": vars(akshat.descendant),
            "medium_coeli": vars(akshat.medium_coeli),
            "imum_coeli": vars(akshat.imum_coeli)
        },
        "houses_positions": {
            "first_house": vars(akshat.first_house),
            "second_house": vars(akshat.second_house),
            "third_house": vars(akshat.third_house),
            "fourth_house": vars(akshat.fourth_house),
            "fifth_house": vars(akshat.fifth_house),
            "sixth_house": vars(akshat.sixth_house),
            "seventh_house": vars(akshat.seventh_house),
            "eighth_house": vars(akshat.eighth_house),
            "ninth_house": vars(akshat.ninth_house),
            "tenth_house": vars(akshat.tenth_house),
            "eleventh_house": vars(akshat.eleventh_house),
            "twelfth_house": vars(akshat.twelfth_house)
        }
    }

@app.get("/astrology-report")
def astrology_report():
    return generate_report()