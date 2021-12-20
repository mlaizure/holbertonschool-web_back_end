const getListStudentIds = (studentArray) => {
  if (!Array.isArray(studentArray)) return [];
  return studentArray.map((student) => student.id);
};

export default getListStudentIds;
