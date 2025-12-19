export default function getListStudentsIds(students) {
    if (!Array.isArray(students)) {
        return [];
    }
    class student {
        constructor(id, firstName, location) {
            this.id = id;
            this.firstName = firstName;
            this.location = location;
        }
    }
    const listStudents = [];
    for (const obj of students) {
        const { id, firstName, location } = obj;
        listStudents.push(new student(id, firstName, location));
    }
    return listStudents;
}
