function solution(rsp) {
    let win = {
        2: 0,
        0: 5,
        5: 2
    };
    var answer = [...rsp].map(v => win[v]).join("");
    return answer;
}