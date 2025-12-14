export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const value of array) {
    array[idx] = appendString + value;
    idx += 1;
  }

  return array;
}
