export default function updateStudentGradeByCity(students, city, newGrade) {
    return students
        .filter((student) => student.location === city)
        .map((student) => ({
            ...student,
            grade: newGrade,
        }));
}
