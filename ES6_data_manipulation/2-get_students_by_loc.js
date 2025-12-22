export default function getStudentsByLoction(students, city) {
    return students.filter((student) => student.location === city);
}
