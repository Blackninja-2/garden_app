/*
Garden Advice App (JavaScript)

This program provides gardening tips based on the season and plant type.
Improvements made:
- Accepts user input using prompt() instead of hardcoded values.
- Refactored advice logic into functions.
- Uses objects to store advice (easier to expand).
- Added comments for clarity.
*/

// Function to get advice based on the season
function getSeasonAdvice(season) {
    const seasonAdvice = {
        summer: "Water your plants regularly and provide some shade.\n",
        winter: "Protect your plants from frost with covers.\n",
        spring: "Plant new seeds and enjoy the fresh growth.\n",
        autumn: "Collect fallen leaves for compost and prepare for winter.\n"
    };
    return seasonAdvice[season.toLowerCase()] || "No advice for this season.\n";
}

// Function to get advice based on the plant type
function getPlantAdvice(plantType) {
    const plantAdvice = {
        flower: "Use fertiliser to encourage blooms.",
        vegetable: "Keep an eye out for pests!",
        herb: "Harvest regularly to promote new growth."
    };
    return plantAdvice[plantType.toLowerCase()] || "No advice for this type of plant.";
}

// Function that combines season and plant advice
function getAdvice(season, plantType) {
    return getSeasonAdvice(season) + getPlantAdvice(plantType);
}

// --- Main Program ---
// Ask the user for input
let season = prompt("Enter the season (spring, summer, autumn, winter):");
let plantType = prompt("Enter the plant type (flower, vegetable, herb):");

// Display the generated advice
console.log("\nYour Gardening Advice:");
console.log(getAdvice(season, plantType));
