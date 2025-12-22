export default function createInt8TypedArray(length, position, value) {
    const int8Array = new Int8Array(length);
    int8Array[position] = value;
    return int8Array;
    if (position < 0 || position >= length) {
        throw new Error('Position outside range');
    }
}
