export default function appendToEachArrayValue(array, appendString) {
  const resArray = [];
  for (const value of array) {
    resArray.push(appendString + value);
  }

  return resArray;
}
