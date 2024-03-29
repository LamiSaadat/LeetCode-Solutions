/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    pattern = pattern.split('')
    s = s.split(' ')
    
    let map = {}

    if (pattern.length !== s.length) {
        return false
    }

    if ((new Set(pattern)).size !== (new Set(s)).size) {
        return false
    }

    for (let i=0; i<pattern.length; i++) {
        if (!(pattern[i] in map)) {
            map[pattern[i]] = s[i]
        } else if (map[pattern[i]] !== s[i]) {
            return false
        }
    }

    return true
};
