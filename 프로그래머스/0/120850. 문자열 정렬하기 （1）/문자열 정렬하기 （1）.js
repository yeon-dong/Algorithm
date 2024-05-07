function solution(my_string) {
    return my_string
        .split("")
        .filter((e) => !isNaN(e))
        .map((e) => e*1) //이걸로 모두 int로 바꿈
        .sort((a,b) => a-b)
}