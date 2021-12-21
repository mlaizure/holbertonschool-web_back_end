const createInt8TypedArray = (length, position, value) => {
  if (position >= length) {
    throw Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const int8 = new DataView(buffer);
  int8.setInt8(position, value);
  return int8;
};

export default createInt8TypedArray;
