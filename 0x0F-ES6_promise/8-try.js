export default function divideFunction(numerator, denominator) {
  let res = 0;
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  try {
    res = numerator / denominator;
  } catch (e) {
    console.log(e);
  }
  return res;
}
