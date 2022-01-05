const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('#sendPaymentRequestToApi()', function () {
  it('should validate the usage of calculcateNumber from Utils', () => {
    const consoleSpy = sinon.spy(console, 'log');
    const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);

    expect(calcStub.calledWith('SUM', 100, 20)).to.be.true;
    expect(calcStub.alwaysReturned(10)).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    consoleSpy.restore();
    calcStub.restore();
  });
});
