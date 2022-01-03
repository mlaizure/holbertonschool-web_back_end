import express from 'express';

const app = express();
const port = 1245;
const routes = require('./routes/index');

app.use('/', routes);
app.use('/students', routes);
app.use('/students/:major', routes);

app.listen(port);

export default app;
