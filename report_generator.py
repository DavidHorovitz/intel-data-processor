# report_generator.py
def generate_mission_summary(missions):
    """יצירת דוח סיכום משימות"""
    total = len(missions)
    active = len([m for m in missions if m["status"] == "Active"])
    complete = len([m for m in missions if m["status"] == "Complete"])
    report = f"""
=== MISSION INTELLIGENCE SUMMARY ===
Total Missions: {total}
Active Missions: {active}
Completed Missions: {complete}
Pending Missions: {total - active - complete}
==================================
"""
    return report.strip()

def generate_personnel_report(personnel):
    """יצירת דוח סיכום כוח אדם"""
    total = len(personnel)
    top_secret = len([p for p in personnel if p["clearance"] == "Top Secret"])
    report = f"""
=== PERSONNEL SUMMARY ===
Total Personnel: {total}
Top Secret Clearance: {top_secret}
Regular Clearance: {total - top_secret}
========================
"""
    return report.strip()

def export_data_to_file(data, filename):
    """ייצוא נתונים לקובץ"""
    with open(filename, 'w') as f:
        f.write(str(data))
    return f"Data exported to {filename}"
