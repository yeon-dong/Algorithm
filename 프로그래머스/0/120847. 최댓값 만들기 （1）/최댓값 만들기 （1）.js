function solution(numbers) {
    var a = Math.max(...numbers);
    numbers.splice(numbers.indexOf(a),1)
    var b = Math.max(...numbers);
    return a*b;
}