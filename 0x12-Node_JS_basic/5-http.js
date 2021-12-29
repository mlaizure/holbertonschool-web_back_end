const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer((req, res) => {
  const { url } = req;
  if (url === '/') res.end('Hello Holberton School!');
  if (url === '/students') {
    countStudents(process.argv[2])
      .then((data) => {
        res.write('This is the list of our students\n');
        res.write(`Number of students: ${data.students.length}\n`);
        res.write(`Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`);
        res.write(`Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`);
        res.end();
      })
      .catch((err) => {
        res.write('This is the list of our students\n');
        res.end(err.message);
      });
  }
});

app.listen(port);

module.exports = app;
