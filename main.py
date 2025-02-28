from kerykeion import AstrologicalSubject,KerykeionChartSVG,Report
import kerykeion


akshat = AstrologicalSubject(
    "Akshat", 2002, 9, 25, 0, 30, lng=72.8777, lat=19.0760, tz_str="Asia/Kolkata", city="Mumbai", zodiac_type="Sidereal", sidereal_mode="LAHIRI"
)

# akshat.moon.element
report = Report(akshat)
report.print_report()
