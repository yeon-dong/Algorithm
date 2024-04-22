function solution(array) {
    var a = Math.max(...array);
    var b = array.indexOf(a);
    return [a,b];
}