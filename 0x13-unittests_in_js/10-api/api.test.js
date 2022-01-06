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

  it('should return "Welcome to the payment system"', (done) => {
    request(homeRoute, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const goodId = 'http://localhost:7865/cart/123';
  const badId = 'http://localhost:7865/cart/nan';

  it('should return status 200', (done) => {
    request(goodId, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return "Payment methods for cart 123"', (done) => {
    request(goodId, (err, res, body) => {
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });

  it('should return status 404', (done) => {
    request(badId, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should return undefined', (done) => {
    request(badId, (err, res, body) => {
      expect(body).to.equal('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot GET /cart/nan</pre>\n</body>\n</html>\n');
      done();
    });
  });
});

describe('Available payments page', () => {
  const apRoute = 'http://localhost:7865/available_payments';

  it('should return status 200', (done) => {
    request (apRoute, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should equal payment methods object', (done) => {
    request(apRoute, (err, res, body) => {
      expect(body).to.deep.equal(JSON.stringify({
	payment_methods: {
	  credit_cards: true,
	  paypal: false,
	}
      }));
      done();
    });
  });
});

describe('Login page', () => {
  const goodUser = {
    url: 'http://localhost:7865/login',
    method: 'POST',
    json: { 'userName': 'Maddi' },
  };

  it('should return status 200', (done) => {
    request.post(goodUser, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return Welcome Maddi', (done) => {
    request.post(goodUser, (err, res, body) => {
      expect(body).to.equal('Welcome Maddi');
      done();
    });
  });
});
