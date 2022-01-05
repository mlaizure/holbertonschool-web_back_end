const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('#calculateNumber()', function () {
  it('should return 3 when adding 1 and 2', function () {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });
  it('should return 4 when adding 2 and 2.1', function () {
    assert.strictEqual(calculateNumber(2, 2.1), 4);
  });
  it('should return 5 when adding 2.1 and 2', function () {
    assert.strictEqual(calculateNumber(2.1, 2), 4);
  });
  it('should return 4 when adding 1.7 and 2', function () {
    assert.strictEqual(calculateNumber(1.7, 2), 4);
  });
  it('should return 1 when adding 0.9 and 0.2', function () {
    assert.strictEqual(calculateNumber(0.9, 0.2), 1);
  });
  it('should return -2 when adding -7.1 and 5', function () {
    assert.strictEqual(calculateNumber(-7.1, 5), -2);
  });
  it('should return -9 when adding -6.4 and -2.6', function () {
    assert.strictEqual(calculateNumber(-6.4, -2.6), -9);
  });
});
