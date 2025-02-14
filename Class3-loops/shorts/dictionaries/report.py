def main():
    spacecraft = {"name": "James Webb Space Telescope"}  #spacecraft is the dictionary
    spacecraft["distance"] = 0.01
    print(create_report(spacecraft))
    
def create_report(spacecraft):
    return f"""
    REPORT
    name: {spacecraft.get("name", "unknown")}
    distance: {spacecraft.get("distance", "unknown")} AU
    
    """
    
#########################

def main():
    spacecraft = {"name": "James Webb Space Telescope"}  #spacecraft is the dictionary
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))
    
def create_report(spacecraft):
    return f"""
    REPORT
    Name: {spacecraft.get("name", "unknown")}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit: {spacecraft.get ("orbit", "unknown")}
    
    """
