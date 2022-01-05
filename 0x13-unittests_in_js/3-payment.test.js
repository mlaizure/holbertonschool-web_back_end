const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('#sendPaymentRequestToApi()', function () {
  it('should validate the usage of calculcateNumber from Utils', () => {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    expect(calcSpy.calledWith('SUM', 100, 20)).to.be.true;
    calcSpy.restore();
  });
});
