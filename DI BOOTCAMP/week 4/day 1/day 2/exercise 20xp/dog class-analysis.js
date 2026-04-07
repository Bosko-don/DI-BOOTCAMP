class Labrador extends Dog {
  constructor(name, size) {
    super(name);        // ✅ Must call super() before using 'this'
    this.size = size;   // ✅ Then can add new properties
  }
};