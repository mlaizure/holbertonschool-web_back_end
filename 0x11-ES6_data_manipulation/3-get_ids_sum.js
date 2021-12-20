const getStudentIdsSum = (studentArray) => studentArray.reduce(
  (prev, current) => prev + current.id, 0,
);

export default getStudentIdsSum;
