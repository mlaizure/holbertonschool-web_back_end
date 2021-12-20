const getStudentsByLocation = (studentArray, city) => studentArray.filter(
  (student) => student.location === city,
);

export default getStudentsByLocation;
