def solar_estimator(daily_kwh, panel_watt=330, sunlight_hours=5):
    panels = daily_kwh * 1000 / (panel_watt * sunlight_hours)
    return f"You need approximately {int(panels+1)} panels of {panel_watt}W for {daily_kwh} kWh/day."
