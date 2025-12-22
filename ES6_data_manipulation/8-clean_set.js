export default function cleanSet(set, startString) {
    if (typeof startString !== 'string' || startString.length === 0) {
        return '';
    }
    let result = '';
    for (const item of set) {
        if (item.startsWith(startString)) {
            result += item.slice(startString.length);
        }
    }
    return result;
}
