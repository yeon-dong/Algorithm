function solution(a, b) {
    var answer = 0;
    if(b<a){
        let space = b;
        b = a;
        a = space;
    }
    for(; a<=b; a++){
        answer += a;
    }
    return answer;
}