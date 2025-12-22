export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const result = [];
  for (const item of set) {
    if (typeof item === 'string' && item.startsWith(startString)) {
      result.push(item.slice(startString.length));
    }
  }
  return result.join('-');
}
