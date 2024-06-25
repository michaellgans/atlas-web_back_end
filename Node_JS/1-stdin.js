// Task 1 - Using Process stdin

// Prints a prompt and answer goes on the next line
console.log('Welcome to Atlas School, what is your name?');

// Listen for standard input
process.stdin.on('data', (input) => {
  console.log(`Your name is: ${input}`);
  process.exit();
});

// Listen for "exit"
process.on('exit', () => {
  console.log('This important software is now closing...');
  console.log('Bye Tomas!');
});
