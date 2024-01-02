export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var newTask = true;
    var newTask2 = false;
  }

  return [task, task2];
}
