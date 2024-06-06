function solution(n) {
    n = String(n);
    let mapfn = (arg) => Number(arg);
    let arr = Array.from(n,mapfn);
    return Number(arr.sort((a, b) => b - a).join(''));
}