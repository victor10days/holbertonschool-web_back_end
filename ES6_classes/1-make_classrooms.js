export default function initializeRooms() {
    const rooms = [19, 20, 34];
    const classRooms = rooms.map((size) => new ClassRoom(size));
    return classRooms;
}
