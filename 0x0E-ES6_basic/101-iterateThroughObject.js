export default function iterateThroughObject(reportWithIterator) {
  let employeeStr = '';
  for (const name of reportWithIterator) {
    employeeStr += `${name} | `;
  }
  return employeeStr.substring(0, employeeStr.length - 3);
}
