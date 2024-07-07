function solution(left, right) {
    let count = 0;
    for(left; left <= right; left++){
        let sum = 0;
        for(let i = 1; i <= left; i++){
            if(left % i == 0){sum += 1;}
        }
        sum % 2 ? count -= left : count += left;
    }
    return count;
}