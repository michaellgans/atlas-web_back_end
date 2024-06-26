// Task 8.3 - Students Controller

function getAllStudents(request):
    return status 200
    calls readDatabase from utils

    if database not available
    return 500
    error: 'Cannot load the database'

function getAllStudentsByMajor(request):
    return status 200

    console.log('Major parameter must be CS or SWE');
    calls function readDatabase from utils
    error: 'Canot load the database'