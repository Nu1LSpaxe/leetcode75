/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 * 
 * Approach: string
 */
var mergeAlternately = function (word1, word2) {
    result = "";
    let length = Math.max(word1.length, word2.length);

    for (let i = 0; i < length; i++) {
        /*
            if (word1[i]) result += word1[i];
            if (word2[i]) result += word2[i];
        */

        // value1 ?? value2: `??` return value2 only when value1 null or undefined
        // value1 || value2: `||` turns value1 into boolean to check
        result += (word1[i] ?? "") + (word2[i] ?? "");
    }

    return result;
};

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 * 
 * Approach: array
 */
var mergeAlternately = function (word1, word2) {
    result = [];
    let length = Math.max(word1.length, word2.length);

    for (let i = 0; i < length; i++) {
        if (word1[i]) result.push(word1[i]);
        if (word2[i]) result.push(word2[i]);
    }

    return result.join('');
};

