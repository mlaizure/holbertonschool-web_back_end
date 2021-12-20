const updateStudentGradeByCity = (studentArray, city, grades) => studentArray.filter(
  (student) => student.location === city,
).map((student) => {
  let studentGrade = 'N/A';
  grades.forEach((grade) => {
    if (grade.studentId === student.id) studentGrade = grade.grade;
  });
  return { ...student, grade: studentGrade };
});

export default updateStudentGradeByCity;
