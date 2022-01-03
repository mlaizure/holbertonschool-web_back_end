import readDatabase from '../utils';

class StudentController {
  static getAllStudents(request, response) {
    response.status(200);
    readDatabase(process.argv[2])
      .then((data) => {
        response.write('This is the list of our students\n');
        response.write(`Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`);
        response.write(`Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`);
        response.end();
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    response.status(200);
    readDatabase(process.argv[2])
      .then((data) => {
        const { major } = request.params;
        if (major === 'CS') response.send(`List: ${data.csStudents.join(', ')}\n`);
        else if (major === 'SWE') response.send(`List: ${data.sweStudents.join(', ')}`);
        else {
          response.status(500);
          response.send('Major parameter must be CS or SWE');
        }
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }
}

export default StudentController;
