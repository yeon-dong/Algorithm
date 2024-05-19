function solution(num, k) {
    num = String(num);
    const mapfn = (arg) => Number(arg);
    const newArr = num.split('').map(mapfn);
    return newArr.indexOf(k) < 0 ? -1 : newArr.indexOf(k) + 1;
}