console.log("Hullo Harry");

// Write a function that takes a list and returns a new list with only the odd numbers.
var allOdd = function(someList) {
    oddList = [];
    for (i = 0; i < someList.length; i++) {
        if (someList[i] % 2 !== 0) {
            oddList.push(someList[i]);
        }
    }
    return oddList;
};

console.log(allOdd([23, 42, 45, 64, 78, 65, 97]));


// Write a function that takes a list and returns a new list with only the even numbers.
var allEven = function(someList) {
    evenList = [];
    for (i = 0; i < someList.length; i++) {
        if (someList[i] % 2 === 0) {
            evenList.push(someList[i]);
        }
    }
    return evenList;
};

console.log(allEven([23, 42, 45, 64, 78, 65, 97]));

// Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
var longWords = function(wordList) {
    longList = [];
    for (i = 0; i < wordList.length; i++) {
        if (wordList[i].length >= 4) {
            longList.push(wordList[i]);
        }
    }
    return longList;
};

console.log(longWords(["mermaid", "ape", "cat", "cactus", "ood", "rose"]));

// Write a function that finds the smallest element in a list of integers and returns it.
var smallest = function(someList) {
    anchor = someList[0];
    for (i = 0; i < someList.length; i++) {
        if (someList[i] < anchor) {
            anchor = someList[i];
        }
    }
    return anchor;
};

console.log(smallest([23, 42, 45, 64, 78, 65, 97]));

// Write a function that finds the largest element in a list of integers and returns it.
var largest = function(someList) {
    anchor = someList[0];
    for (i = 0; i < someList.length; i++) {
        if (someList[i] > anchor) {
            anchor = someList[i];
        }
    }
    return anchor;
};

console.log(largest([23, 42, 45, 64, 78, 65, 97]));

// Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
var halvesies = function(someList) {
    halvesList = [];
    for (i = 0; i < someList.length; i++) {
        halvesList.push(someList[i]/2);
    }
    return halvesList;
};

console.log(halvesies([23, 42, 45, 64, 78, 65, 97]));

// Write a function that takes a list of words and returns a list of all the lengths of those words.
var wordLenths = function(wordList) {
    lengthsList = [];
    for (i = 0; i < wordList.length; i++) {
        lengthsList.push(wordList[i].length);
    }
    return lengthsList;
};

console.log(wordLenths(["mermaid", "ape", "cat", "cactus", "ood", "rose"]));

// Write a function (using iteration) that sums all the numbers in a list.
var sumNumbers = function(numbers) {
    anchor = 0;
    for (i = 0; i < numbers.length; i++) {
        anchor += numbers[i];
    }
    return anchor;
};

console.log(sumNumbers([1, 2, 3, 4, 5, 6, 7]));

// Write a function that multiplies all the numbers in a list together.
var multNumbers = function(numbers) {
    anchor = 1;
    for (i = 0; i < numbers.length; i++) {
        anchor *= numbers[i];
    }
    return anchor;
};

console.log(multNumbers([1, 2, 3, 4]));

// Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
var joinStrings = function(stringList) {
    newString = "";
    for (i = 0; i < stringList.length; i++) {
        newString += stringList[i];
    }
    return newString;
};

console.log(joinStrings(["mermaid", "ape", "cat", "cactus", "ood", "rose"]));


// Write a function that takes a list of integers and returns the average (without using the avg method)
var average = function(numbers) {
    return sumNumbers(numbers)/numbers.length;
};

console.log(average([1, 2, 3, 4, 5, 6, 7, 8]));
