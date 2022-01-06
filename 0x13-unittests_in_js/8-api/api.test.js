const expect = require('chai').expect;
const request = require('request');

describe('Index page', () => {
  const homeRoute = 'http://localhost:7865';

  it('should return status 200', (done) => {
    request(homeRoute, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should log "Welcome to the payment system" to the console', (done) => {
    request(homeRoute, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
