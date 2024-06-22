function solution(numbers) {
    let sum = 0;
    [0,1,2,3,4,5,6,7,8,9].filter((n) => !numbers.includes(n))
        .forEach(num => {sum += num;});
    return sum;
}