export default function createReportObject(employeesList) {
  /* Create empty object to return */
  let employeeReport = {};

  /* Store all VALUES from employeesList (like variadic) */
  employeeReport = Object.assign({}, ...Object.values(employeesList));

  employeeReport.getNumberOfDepartments = function () {
      /* returns number of departments */
      return Object.keys(employeesList).length;
  };

  return employeeReport;
}
