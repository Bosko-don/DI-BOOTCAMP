// ============================================
// DAILY CHALLENGE: CREATING OBJECTS
// Complete Single Code File
// ============================================

// Create Video class
class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    
    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}

// ============================================
// REQUIRED: Instantiate first Video and call watch()
// ============================================
const video1 = new Video("JavaScript Tutorial", "John", 300);
video1.watch();

// ============================================
// REQUIRED: Instantiate second Video with different values
// ============================================
const video2 = new Video("Python Basics", "Sarah", 450);
video2.watch();

// ============================================
// BONUS: Array of data for five Video instances
// Best data structure: array of objects
// ============================================
const videoData = [
    { title: "JavaScript Basics", uploader: "Alice", time: 240 },
    { title: "CSS Flexbox Guide", uploader: "Bob", time: 180 },
    { title: "React Tutorial", uploader: "Charlie", time: 600 },
    { title: "Node.js Intro", uploader: "Diana", time: 420 },
    { title: "HTML5 Overview", uploader: "Eve", time: 300 }
];

// ============================================
// BONUS: Loop through array to instantiate instances
// ============================================
const videos = [];

videoData.forEach(data => {
    const video = new Video(data.title, data.uploader, data.time);
    videos.push(video);
});

// Call watch() on all bonus videos
videos.forEach(video => video.watch());