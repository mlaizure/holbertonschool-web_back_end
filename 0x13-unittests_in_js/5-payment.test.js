const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('#sendPaymentRequestToApi()', function () {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    expect(consoleSpy.calledOnce).to.be.true;
    consoleSpy.restore();
  });

  it('should log "The total is: 120" to the console', () => {
    sendPaymentRequestToApi(100,20);
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  });
  it('should log "The total is: 20" to the console', () => {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  });
});
