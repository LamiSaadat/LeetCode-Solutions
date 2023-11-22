/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let mapS = {}
    let mapT = {}

    for (let i=0; i<s.length; i++) {
        if (!(s[i] in mapS)) {
            mapS[s[i]] = t[i]
        } else if (t[i] !== mapS[s[i]]) {
            return false
        }

        if (!(t[i] in mapT)) {
            mapT[t[i]] = s[i]
        } else if (s[i] !== mapT[t[i]]) {
            return false
        }
    }
    return true
    
};


// paper
// title

// baba
// babc