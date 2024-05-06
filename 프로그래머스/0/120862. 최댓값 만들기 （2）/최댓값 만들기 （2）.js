function solution(numbers) {
    let n = numbers.length - 1;
    numbers.sort((a, b) => b - a);
    let max = numbers[0] * numbers[1];
    let min = numbers[n] * numbers[n-1];
    if(max > min) {
        return max;
    }
    else {return min}
}