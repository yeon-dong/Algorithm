function solution(s) {
    s = s.split('').sort((a, b) => a > b ? -1 : 1);
    return s.reduce((a,c) => a+c,'');
}