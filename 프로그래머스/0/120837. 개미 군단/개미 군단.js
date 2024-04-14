function solution(hp) {
    var answer = 0;
    var a = parseInt(hp / 5)
    var b = parseInt((hp-a*5) / 3)
    return a + b + (hp-a*5-b*3);
}