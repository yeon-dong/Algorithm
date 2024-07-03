function solution(num) {
    var count = 0;
    while(num != 1){
        if(num % 2){ num = num*3 + 1 }
        else{ num = num/2 }
        if(count > 500){return -1}
        count++;
    }
    return count;
}