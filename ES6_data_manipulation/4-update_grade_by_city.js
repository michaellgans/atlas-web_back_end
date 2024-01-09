/* Task 4 */

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const updatedStudentList = studentList.map((item) => ({
    ...item,
    grade: 'N/A'
  }));

  return updatedStudentList;
}
  