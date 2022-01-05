const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('#calculateNumber() with type SUM', function () {
  it('should return 3 when adding 1 and 2', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 2), 3);
  });
  it('should return 4 when adding 2 and 2.1', function () {
    assert.strictEqual(calculateNumber('SUM', 2, 2.1), 4);
  });
  it('should return 5 when adding 2 and 2.8', function () {
    assert.strictEqual(calculateNumber('SUM', 2, 2.8), 5);
  });
  it('should return 4 when adding 1.7 and 2', function () {
    assert.strictEqual(calculateNumber('SUM', 1.7, 2), 4);
  });
  it('should return 1 when adding 0.9 and 0.2', function () {
    assert.strictEqual(calculateNumber('SUM', 0.9, 0.2), 1);
  });
  it('should return -2 when adding -7.1 and 5', function () {
    assert.strictEqual(calculateNumber('SUM', -7.1, 5), -2);
  });
  it('should return -9 when adding -6.4 and -2.6', function () {
    assert.strictEqual(calculateNumber('SUM', -6.4, -2.6), -9);
  });
});

describe('#calculateNumber() with type SUBTRACT', function () {
  it('should return -2 when subtracting 1 from 3', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('should return -1 when subtracting 4.1 from 3', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 4.1), -1);
  });
  it('should return 6 when subtracting 4 from 9.9', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 9.9, 4), 6);
  });
  it('should return 0 when subtracting 0.7 from 0.6', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 0.6, 0.7), 0);
  });
  it('should return 1 when subtracting -3.8 from -3.2', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', -3.2, -3.8), 1);
  });
  it('should return -4 when subtracting 2.4 from -2', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', -2, 2.4), -4);
  });
  it('should return 1 when subtracting -0.4 from 1.1', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.1, -0.4), 1);
  });
});

describe('#calculateNumber() with type DIVIDE', function () {
  it('should return 2 when dividing 4 with 2', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
  });
    it('should return 6 when dividing 6 with 1.1', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 6, 1.1), 6);
  });
  it('should return 0.2 when dividing 1.4 with 4.5', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('should return -1 when dividing -0.9 with 0.8', function () {
    assert.strictEqual(calculateNumber('DIVIDE', -0.9, 0.8), -1);
  });
  it('should return "Error" when dividing 7.7 with 0.2', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 7.7, 0.2), 'Error');
  });
  it('should return 3 when dividing -3.3 with -0.7', function () {
    assert.strictEqual(calculateNumber('DIVIDE', -3.3, -0.7), 3);
  });
  it('should return 7 when dividing 49 with 7.2', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 49, 7.2), 7);
  });
});
