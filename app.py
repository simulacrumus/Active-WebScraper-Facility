from builder import build_active_facilities
from util import write_json_data

def run():
    facilities = build_active_facilities()
    write_json_data(facilities, "facilities.json")

if __name__ == '__main__':
    run()