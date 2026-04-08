const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`;

function toJs() {
    return new Promise((resolve, reject) => {
        const morseJS = JSON.parse(morse);
        
        if (Object.keys(morseJS).length === 0) {
            reject('Error: Morse object is empty');
        } else {
            resolve(morseJS);
        }
    });
}

function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const userInput = prompt('Enter a word or sentence:');
        
        if (!userInput) {
            reject('Error: No input provided');
            return;
        }
        
        const morseTranslation = [];
        
        for (let char of userInput.toLowerCase()) {
            if (char === ' ') continue; // Skip spaces
            
            if (morseJS[char]) {
                morseTranslation.push(morseJS[char]);
            } else {
                reject(`Error: Character "${char}" not found in Morse code`);
                return;
            }
        }
        
        resolve(morseTranslation);
    });
}

function joinWords(morseTranslation) {
    const result = morseTranslation.join('<br>');
    document.body.innerHTML += `<pre>${result}</pre>`;
    return result;
}

// Chain the functions
toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.log(error));