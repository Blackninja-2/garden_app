"""
Garden Advice App (Python)

This program provides gardening tips based on the season and plant type.
Improvements made:
- Accepts user input instead of hardcoded values.
- Refactored advice logic into functions.
- Uses dictionaries to store advice (easier to expand).
- Added comments and docstrings for readability.
"""

def get_season_advice(season: str) -> str:
    """Return gardening advice based on the season."""
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
        "spring": "Plant new seeds and enjoy the fresh growth.\n",
        "autumn": "Collect fallen leaves for compost and prepare for winter.\n"
    }
    return season_advice.get(season.lower(), "No advice for this season.\n")


def get_plant_advice(plant_type: str) -> str:
    """Return gardening advice based on the plant type."""
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest regularly to promote new growth."
    }
    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")


def get_advice(season: str, plant_type: str) -> str:
    """Combine season and plant advice into a single message."""
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


if __name__ == "__main__":
    # Ask the user for input
    season = input("Enter the season (spring, summer, autumn, winter): ")
    plant_type = input("Enter the plant type (flower, vegetable, herb): ")

    # Generate and display advice
    print("\nYour Gardening Advice:")
    print(get_advice(season, plant_type))
