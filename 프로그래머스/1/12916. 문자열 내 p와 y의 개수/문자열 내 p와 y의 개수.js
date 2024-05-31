function solution(s){
    s = s.toLowerCase();
    return s.match(/p/g)?.length == s.match(/y/g)?.length ? true : false;
}