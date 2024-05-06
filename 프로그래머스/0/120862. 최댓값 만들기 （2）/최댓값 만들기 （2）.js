function solution(numbers) {
    let n = numbers.length - 1;
    numbers.sort((a, b) => b - a);
    return Math.max(
        numbers[n] * numbers[n-1],
        numbers[0] * numbers[1]
    )
}