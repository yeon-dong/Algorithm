function solution(s1, s2) {
    const answer = s1.filter((x) => s2.includes(x));
    return answer.length;
}