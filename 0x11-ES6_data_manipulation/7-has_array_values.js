const hasValuesFromArray = (set, array) => array.every(
  (e) => set.has(e),
);

export default hasValuesFromArray;
