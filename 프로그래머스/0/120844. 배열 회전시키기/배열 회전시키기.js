function solution(numbers, direction) {
    if(direction == "right"){
        return [numbers[numbers.length-1]].concat(numbers.slice(0,numbers.length-1))
    }
    else{
        return numbers.slice(1,numbers.length).concat(numbers[0])
    }
}