/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let totalWealth = []
    for(let i=0; i<accounts.length; i++) {
        totalWealth.push(accounts[i].reduce((a, b) => a+b, 0))
    }
    return Math.max(...totalWealth)
};