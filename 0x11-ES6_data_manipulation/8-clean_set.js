const cleanSet = (set, startString) => {
  if (startString === '' || typeof startString !== 'string') return '';
  return [...set]
    .filter((item) => typeof item === 'string' && item.startsWith(startString))
    .map((item) => item.substring(startString.length))
    .join('-');
};

export default cleanSet;
