function solution(age) {
    return age
    .toString()
    .split("")
    .map((v) => "abcdefghij"[v])
    .join("");
    // 52 -> "52" -> ["5","2"]. -> ["abcdefghij"[5], "abcdefghij"[2] ] -> "fc"
}