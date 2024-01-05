export default function createReportObject(employeesList) {
  /* Create object to return */
  let employeeReport = {
    allEmployees: {
      ...employeesList,
    },
    /* Second thing to be stored in the object */
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };

  return employeeReport;
}
