// ============================================
// SOLAR SYSTEM - DOM Manipulation Exercise
// Creates planets and their moons dynamically
// ============================================

// Wait for DOM to load before executing
document.addEventListener('DOMContentLoaded', function() {
    
    // Get the section where we'll append planets
    const section = document.querySelector('.listPlanets');
    
    // ==========================================
    // ARRAY OF OBJECTS: Planets with their moons
    // Using objects allows us to store multiple
    // properties: name, color, and moons array
    // ==========================================
    
    const solarSystem = [
        {
            name: 'Mercury',
            color: '#A5A5A5',  // Gray
            moons: 0
        },
        {
            name: 'Venus',
            color: '#E3BB76',  // Yellowish-brown
            moons: 0
        },
        {
            name: 'Earth',
            color: '#6B93D6',  // Blue
            moons: 1
        },
        {
            name: 'Mars',
            color: '#C1440E',  // Red-orange
            moons: 2
        },
        {
            name: 'Jupiter',
            color: '#D8CA9D',  // Beige with bands
            moons: 79
        },
        {
            name: 'Saturn',
            color: '#F4D298',  // Pale gold
            moons: 82
        },
        {
            name: 'Uranus',
            color: '#D1E7E7',  // Light blue
            moons: 27
        },
        {
            name: 'Neptune',
            color: '#5B5DDF',  // Deep blue
            moons: 14
        }
    ];
    
    // ==========================================
    // FUNCTION: Create a planet element
    // ==========================================
    
    function createPlanet(planetData, index) {
        // Create the planet div
        const planetDiv = document.createElement('div');
        
        // Add the planet class
        planetDiv.classList.add('planet');
        
        // Add a unique class for specific styling (planet-0, planet-1, etc.)
        planetDiv.classList.add(`planet-${index}`);
        
        // Set the background color directly via style
        planetDiv.style.backgroundColor = planetData.color;
        
        // Add planet name as text
        planetDiv.textContent = planetData.name;
        
        // Style the text for visibility
        planetDiv.style.color = 'white';
        planetDiv.style.fontFamily = 'Arial, sans-serif';
        planetDiv.style.fontWeight = 'bold';
        planetDiv.style.display = 'flex';
        planetDiv.style.alignItems = 'center';
        planetDiv.style.justifyContent = 'center';
        planetDiv.style.margin = '20px';
        planetDiv.style.boxShadow = `0 0 20px ${planetData.color}`;
        
        // ==========================================
        // BONUS: Create moons for this planet
        // ==========================================
        
        if (planetData.moons > 0) {
            // We'll display up to 4 moons visibly (so it doesn't get crowded)
            // In reality, Jupiter and Saturn have 79+ moons!
            const moonsToDisplay = Math.min(planetData.moons, 4);
            
            for (let i = 0; i < moonsToDisplay; i++) {
                const moonDiv = document.createElement('div');
                moonDiv.classList.add('moon');
                
                // Position moons around the planet in a circle
                const angle = (i / moonsToDisplay) * 2 * Math.PI;
                const distance = 70; // Distance from planet center
                const x = Math.cos(angle) * distance;
                const y = Math.sin(angle) * distance;
                
                moonDiv.style.left = `calc(50% + ${x}px - 15px)`;
                moonDiv.style.top = `calc(50% + ${y}px - 15px)`;
                
                // Add tooltip showing moon number
                moonDiv.title = `Moon ${i + 1} of ${planetData.moons}`;
                
                planetDiv.appendChild(moonDiv);
            }
            
            // Add moon count label if there are many moons
            if (planetData.moons > 4) {
                const moonLabel = document.createElement('span');
                moonLabel.textContent = `+${planetData.moons - 4} more`;
                moonLabel.style.position = 'absolute';
                moonLabel.style.bottom = '-20px';
                moonLabel.style.fontSize = '10px';
                moonLabel.style.color = '#aaa';
                planetDiv.appendChild(moonLabel);
            }
        }
        
        return planetDiv;
    }
    
    // ==========================================
    // CREATE AND DISPLAY ALL PLANETS
    // ==========================================
    
    // Style the section to display planets in a row
    section.style.display = 'flex';
    section.style.flexWrap = 'wrap';
    section.style.justifyContent = 'center';
    section.style.alignItems = 'center';
    section.style.minHeight = '100vh';
    
    // Loop through each planet and create it
    solarSystem.forEach((planet, index) => {
        const planetElement = createPlanet(planet, index);
        section.appendChild(planetElement);
    });
    
    // Add a title
    const title = document.createElement('h1');
    title.textContent = 'Our Solar System';
    title.style.color = 'white';
    title.style.textAlign = 'center';
    title.style.width = '100%';
    title.style.fontFamily = 'Arial, sans-serif';
    title.style.textShadow = '0 0 10px white';
    document.body.insertBefore(title, section);
    
    console.log('Solar system created successfully! 🪐');
    console.log(`Created ${solarSystem.length} planets`);
});




