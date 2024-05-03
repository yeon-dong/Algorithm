function solution(n) {
    n = n.toString();
    var answer = 0;
    for(let i = 0; i < n.length; i++){
        answer += parseInt(n[i]);
    }
    return answer;
}