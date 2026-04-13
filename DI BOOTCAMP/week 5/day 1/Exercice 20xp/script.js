// Star Wars Character Explorer - Using Fetch API with async/await

// DOM Elements
const elements = {
    characterName: document.getElementById('characterName'),
    cardBody: document.getElementById('cardBody'),
    loadingMessage: document.getElementById('loadingMessage'),
    errorMessage: document.getElementById('errorMessage'),
    randomBtn: document.getElementById('randomBtn')
};

// API Configuration
const API_BASE_URL = 'https://www.swapi.tech/api';
const TOTAL_CHARACTERS = 83; // API contains 83 different characters (UIDs 1-83)

/**
 * Get a random character ID between 1 and TOTAL_CHARACTERS
 * @returns {number} Random character ID
 */
function getRandomCharacterId() {
    return Math.floor(Math.random() * TOTAL_CHARACTERS) + 1;
}

/**
 * Fetch character data from the API
 * @param {number} id - Character ID
 * @returns {Promise<Object>} Character data
 */
async function fetchCharacter(id) {
    const response = await fetch(`${API_BASE_URL}/people/${id}`);
    
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.message !== 'ok' || !data.result) {
        throw new Error('Character not found');
    }
    
    return data.result.properties;
}

/**
 * Fetch homeworld name from the API
 * @param {string} url - Homeworld API URL
 * @returns {Promise<string>} Homeworld name
 */
async function fetchHomeworld(url) {
    const response = await fetch(url);
    
    if (!response.ok) {
        return 'Unknown';
    }
    
    const data = await response.json();
    return data.result?.properties?.name || 'Unknown';
}

/**
 * Display loading state
 */
function showLoading() {
    elements.characterName.textContent = 'Loading...';
    elements.cardBody.style.display = 'none';
    elements.errorMessage.style.display = 'none';
    elements.loadingMessage.style.display = 'block';
    elements.randomBtn.disabled = true;
}

/**
 * Display error state
 */
function showError() {
    elements.characterName.textContent = 'Error';
    elements.cardBody.style.display = 'none';
    elements.loadingMessage.style.display = 'none';
    elements.errorMessage.style.display = 'block';
    elements.randomBtn.disabled = false;
}

/**
 * Display character data on the DOM
 * @param {Object} character - Character data object
 */
async function displayCharacter(character) {
    // Get homeworld name
    const homeworldName = await fetchHomeworld(character.homeworld);
    
    // Update character name
    elements.characterName.textContent = character.name;
    
    // Create info grid HTML
    const infoHTML = `
        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">Height</div>
                <div class="info-value">${character.height !== 'unknown' ? character.height + ' cm' : 'Unknown'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Gender</div>
                <div class="info-value">${character.gender !== 'n/a' ? character.gender.charAt(0).toUpperCase() + character.gender.slice(1) : 'N/A'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Birth Year</div>
                <div class="info-value">${character.birth_year !== 'unknown' ? character.birth_year : 'Unknown'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Homeworld</div>
                <div class="info-value">${homeworldName}</div>
            </div>
        </div>
    `;
    
    // Update card body
    elements.cardBody.innerHTML = infoHTML;
    elements.cardBody.style.display = 'block';
    
    // Hide loading and enable button
    elements.loadingMessage.style.display = 'none';
    elements.randomBtn.disabled = false;
}

/**
 * Main function to get and display random character
 */
async function getRandomCharacter() {
    showLoading();
    
    try {
        const randomId = getRandomCharacterId();
        const character = await fetchCharacter(randomId);
        await displayCharacter(character);
    } catch (error) {
        console.error('Error fetching character:', error);
        showError();
    }
}

/**
 * Initialize event listeners
 */
function init() {
    elements.randomBtn.addEventListener('click', getRandomCharacter);
}

// Start the app
init();