from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(rides):
    """Build a compact dictionary with headline statistics."""
    summary = {
        "ride_count": len(rides),
        "average_duration": average_duration(rides),
        "rider_types": count_by_rider_type(rides),
    }
    if rides:
        summary["busiest_start_station"] = busiest_start_station(rides)
    else:
        summary["busiest_start_station"] = None
    return summary


def format_summary(summary):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    ride_count_line = f"Rides: {summary['ride_count']}"
    average_duration_line = f"Average duration: {summary['average_duration']:.1f} min"
    busiest_station_line = f"Busiest start: {summary['busiest_start_station']}"
    return (
        title + "\n" + ride_count_line + "\n" + average_duration_line + "\n" + busiest_station_line
    )
