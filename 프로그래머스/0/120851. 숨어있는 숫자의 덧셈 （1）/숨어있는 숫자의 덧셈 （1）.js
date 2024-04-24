function solution(my_string) {
    var num = my_string.replace(/[^0-9]/g,'')
    var answer = 0
    for(let i = 0; i < num.length; i++){
        answer += parseInt(num[i])
    }
    return answer;
}