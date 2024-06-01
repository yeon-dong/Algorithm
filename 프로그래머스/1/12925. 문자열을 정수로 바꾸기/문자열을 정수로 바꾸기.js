function solution(s) {
    var answer = 0;
    return s[0] == "-" ? -parseInt(s.substr(1)) : parseInt(s);
}