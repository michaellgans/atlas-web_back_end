export default function createReportObject(employeesList) {
  /* Create object to return */
  const employeeReport = {
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
