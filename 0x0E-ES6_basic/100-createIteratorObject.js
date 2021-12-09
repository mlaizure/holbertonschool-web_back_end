export default function createIteratorObject(report) {
  const employees = [];
  for (const itr of Object.keys(report.allEmployees)) {
    employees.push(...report.allEmployees[itr]);
  }
  const customItr = {
    [Symbol.iterator]() {
      let counter = 0;
      return {
        next() {
          if (counter < employees.length) {
            counter += 1;
            return { done: false, value: employees[counter - 1] };
          }
          return { done: true, value: undefined };
        },
      };
    },
  };
  return customItr;
}
