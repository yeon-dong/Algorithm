function solution(s) {
    s=s.split(' ')
    min = Number(s[0]);
    max = Number(s[0]);
    for(let i = 1; i < s.length; i++){
        if(min > Number(s[i])){
            min = Number(s[i]);
        }
        if(max < Number(s[i])){
            max = Number(s[i]);
        }
    }
    return String(min) + " " + String(max);
}