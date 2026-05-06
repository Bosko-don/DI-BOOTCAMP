const chalk = require('chalk');

function showMessage() {
  console.log(chalk.blue("🌍 Welcome to Daily Challenge"));
  console.log(chalk.green.bold("✔ Success is near!"));
  console.log(chalk.red("⚠ Keep pushing forward!"));
}

module.exports = showMessage;