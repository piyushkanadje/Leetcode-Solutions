/**
 * @return {Function}
 */
var createHelloWorld = function() {
    let string = "Hello World"
    return function(...args) {
        return string;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */