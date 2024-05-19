function solution(num, k) {
    return num.toString().split("").map((el) => Number(el)).indexOf(k) < 0 ? -1 : num.toString().split("").map((el) => Number(el)).indexOf(k) + 1;
}