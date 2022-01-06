const should = require('chai').should();
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('#getPaymentTokenFromAPI()', () => {
  it('should return "Successful response from the API" when true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((val) => {
        val.data.should.equal("Successful response from the API");
        done();
      });
  });
});
