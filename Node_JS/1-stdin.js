// Task 1 - Using Process stdin

// Prints a prompt and answer goes on the next line
console.log('Welcome to Atlas School, what is your name?');

// Listen for standard input
process.stdin.on('data', (input) => {
  console.log(`\nYour name is: ${input}`);

  // Makes exit process wait for better UX
  setTimeout(() => {
    process.exit();
  }, 1000);
});

// Listen for "exit"
process.on('exit', () => {
  console.log('This important software is now closing...');
  console.log('Bye Tomas!');
});
