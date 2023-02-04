from scraper import *

def build_active_facilities():
    all_facilities = scrape_all_facilities()
    active_facilities = []
    for facility in all_facilities:
        facility_info = scrape_facility_details(facility["url"])
        if facility_info is not None and len(facility_info["reservations"]) > 0:
            facility["phone"] = facility_info["phone"]
            facility["email"] = facility_info["email"]
            facility["longitude"] = 0.0
            facility["latitude"] = 0.0
            facility["reservations"] = facility_info["reservations"]
            active_facilities.append(facility)
    return active_facilities