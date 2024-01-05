export default function createEmployeesObject(departmentName, employees) {
  const employeeList = employees.join(', ');
  return `${departmentName}: ${employeeList}`;
}
