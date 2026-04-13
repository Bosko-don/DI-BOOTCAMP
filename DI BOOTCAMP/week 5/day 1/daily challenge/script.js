/**
 * Currency Converter Application
 * Using ExchangeRate-API with Fetch API and async/await
 */

// ==========================================
// CONFIGURATION - Replace with your API key
// ==========================================
const API_KEY = 'YOUR_API_KEY_HERE'; // Get free key from https://www.exchangerate-api.com/
const API_BASE_URL = `https://v6.exchangerate-api.com/v6/${API_KEY}`;

// ==========================================
// DOM ELEMENTS
// ==========================================
const elements = {
    amount: document.getElementById('amount'),
    fromCurrency: document.getElementById('fromCurrency'),
    toCurrency: document.getElementById('toCurrency'),
    fromSymbol: document.getElementById('fromSymbol'),
    switchBtn: document.getElementById('switchBtn'),
    convertBtn: document.getElementById('convertBtn'),
    btnSpinner: document.getElementById('btnSpinner'),
    resultSection: document.getElementById('resultSection'),
    resultValue: document.getElementById('resultValue'),
    resultCurrency: document.getElementById('resultCurrency'),
    rateInfo: document.getElementById('rateInfo'),
    lastUpdated: document.getElementById('lastUpdated'),
    errorMessage: document.getElementById('errorMessage'),
    errorText: document.getElementById('errorText')
};

// Currency symbols mapping
const currencySymbols = {
    USD: '$', EUR: '€', GBP: '£', JPY: '¥', CNY: '¥', 
    KRW: '₩', INR: '₹', RUB: '₽', BRL: 'R$', 
    CAD: 'C$', AUD: 'A$', CHF: 'Fr', SEK: 'kr',
    NOK: 'kr', DKK: 'kr', PLN: 'zł', THB: '฿',
    VND: '₫', IDR: 'Rp', MYR: 'RM', PHP: '₱',
    SGD: 'S$', NZD: 'NZ$', MXN: '$', ZAR: 'R',
    TRY: '₺', AED: 'د.إ', SAR: '﷼', ILS: '₪',
    EGP: '£', NGN: '₦', PKR: '₨', BDT: '৳',
    LKR: 'Rs', NPR: '₨', KWD: 'د.ك', QAR: 'ر.ق',
    OMR: 'ر.ع.', BHD: 'د.ب', JOD: 'د.ا', LBP: 'ل.ل',
    default: ''
};

// ==========================================
// API FUNCTIONS
// ==========================================

/**
 * Fetch all supported currency codes from the API
 * Uses the Supported Codes Endpoint [^35^]
 * @returns {Promise<Array>} Array of [code, name] pairs
 */
async function fetchSupportedCurrencies() {
    const response = await fetch(`${API_BASE_URL}/codes`);
    
    if (!response.ok) {
        throw new Error('Failed to fetch supported currencies');
    }
    
    const data = await response.json();
    
    if (data.result === 'error') {
        throw new Error(data['error-type'] || 'Unknown API error');
    }
    
    return data.supported_codes;
}

/**
 * Convert currency using the Pair Conversion API [^31^]
 * @param {string} fromCode - Base currency code
 * @param {string} toCode - Target currency code
 * @param {number} amount - Amount to convert
 * @returns {Promise<Object>} Conversion result
 */
async function convertCurrency(fromCode, toCode, amount) {
    // Using the Pair Conversion endpoint with optional AMOUNT parameter
    const url = `${API_BASE_URL}/pair/${fromCode}/${toCode}/${amount}`;
    
    const response = await fetch(url);
    
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.result === 'error') {
        throw new Error(data['error-type'] || 'Conversion failed');
    }
    
    return data;
}

// ==========================================
// UI FUNCTIONS
// ==========================================

/**
 * Populate currency dropdowns with fetched codes
 * @param {Array} currencies - Array of [code, name] pairs
 */
function populateDropdowns(currencies) {
    const optionsHTML = currencies.map(([code, name]) => 
        `<option value="${code}">${code} - ${name}</option>`
    ).join('');
    
    elements.fromCurrency.innerHTML = optionsHTML;
    elements.toCurrency.innerHTML = optionsHTML;
    
    // Set default values
    elements.fromCurrency.value = 'USD';
    elements.toCurrency.value = 'EUR';
    
    updateCurrencySymbol();
}

/**
 * Update the currency symbol displayed in the amount input
 */
function updateCurrencySymbol() {
    const code = elements.fromCurrency.value;
    const symbol = currencySymbols[code] || currencySymbols.default;
    elements.fromSymbol.textContent = symbol;
}

/**
 * Display conversion result on the DOM
 * @param {Object} data - API response data
 * @param {string} toCode - Target currency code
 */
function displayResult(data, toCode) {
    // Hide error if visible
    elements.errorMessage.classList.add('hidden');
    
    // Update result values
    elements.resultValue.textContent = formatNumber(data.conversion_result);
    elements.resultCurrency.textContent = toCode;
    elements.rateInfo.textContent = `1 ${data.base_code} = ${data.conversion_rate} ${data.target_code}`;
    
    // Format last updated time
    const updateDate = new Date(data.time_last_update_utc);
    elements.lastUpdated.textContent = `Updated: ${updateDate.toLocaleTimeString()}`;
    
    // Show result section with animation
    elements.resultSection.classList.remove('hidden');
    
    // Scroll to result on mobile
    if (window.innerWidth <= 480) {
        elements.resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

/**
 * Display error message
 * @param {string} message - Error message to display
 */
function displayError(message) {
    elements.errorText.textContent = message;
    elements.errorMessage.classList.remove('hidden');
    elements.resultSection.classList.add('hidden');
    
    // Auto-hide error after 5 seconds
    setTimeout(() => {
        elements.errorMessage.classList.add('hidden');
    }, 5000);
}

/**
 * Format number with appropriate decimal places
 * @param {number} num - Number to format
 * @returns {string} Formatted number
 */
function formatNumber(num) {
    if (num >= 1000000) {
        return num.toLocaleString('en-US', { maximumFractionDigits: 2 });
    }
    return num.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

/**
 * Set loading state on convert button
 * @param {boolean} isLoading - Whether button is loading
 */
function setLoading(isLoading) {
    elements.convertBtn.disabled = isLoading;
    elements.convertBtn.classList.toggle('loading', isLoading);
    
    if (isLoading) {
        elements.btnSpinner.classList.remove('hidden');
    } else {
        elements.btnSpinner.classList.add('hidden');
    }
}

// ==========================================
// EVENT HANDLERS
// ==========================================

/**
 * Handle convert button click
 */
async function handleConvert() {
    const amount = parseFloat(elements.amount.value);
    const fromCode = elements.fromCurrency.value;
    const toCode = elements.toCurrency.value;
    
    // Validation
    if (!amount || amount <= 0) {
        displayError('Please enter a valid amount greater than 0');
        return;
    }
    
    if (!fromCode || !toCode) {
        displayError('Please select both currencies');
        return;
    }
    
    setLoading(true);
    
    try {
        const data = await convertCurrency(fromCode, toCode, amount);
        displayResult(data, toCode);
    } catch (error) {
        console.error('Conversion error:', error);
        
        // Handle specific error types from API [^31^]
        let errorMessage = 'Failed to convert currency. Please try again.';
        
        if (error.message.includes('unsupported-code')) {
            errorMessage = 'One or more currency codes are not supported.';
        } else if (error.message.includes('invalid-key')) {
            errorMessage = 'Invalid API key. Please check your configuration.';
        } else if (error.message.includes('quota-reached')) {
            errorMessage = 'API quota exceeded. Please try again later.';
        } else if (error.message.includes('inactive-account')) {
            errorMessage = 'Please confirm your email address to activate the API key.';
        }
        
        displayError(errorMessage);
    } finally {
        setLoading(false);
    }
}

/**
 * Handle switch button click - swaps currencies and converts
 */
async function handleSwitch() {
    const fromValue = elements.fromCurrency.value;
    const toValue = elements.toCurrency.value;
    
    // Swap values
    elements.fromCurrency.value = toValue;
    elements.toCurrency.value = fromValue;
    
    // Update symbol
    updateCurrencySymbol();
    
    // Trigger conversion if we have a result displayed
    if (!elements.resultSection.classList.contains('hidden')) {
        await handleConvert();
    }
}

/**
 * Initialize the application
 */
async function init() {
    try {
        // Fetch supported currencies on load
        const currencies = await fetchSupportedCurrencies();
        populateDropdowns(currencies);
        
        // Add event listeners
        elements.convertBtn.addEventListener('click', handleConvert);
        elements.switchBtn.addEventListener('click', handleSwitch);
        elements.fromCurrency.addEventListener('change', updateCurrencySymbol);
        
        // Allow Enter key to convert
        elements.amount.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                handleConvert();
            }
        });
        
    } catch (error) {
        console.error('Initialization error:', error);
        displayError('Failed to load currencies. Please check your API key and refresh the page.');
    }
}

// Start the app
init();