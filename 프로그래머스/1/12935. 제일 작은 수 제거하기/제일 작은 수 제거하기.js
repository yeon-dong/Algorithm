function solution(arr) {
    if(arr.length===1){return [-1]}
    min = arr[0];
    for(let i = 1; i < arr.length; i++){
        if(min > arr[i]){min = arr[i]}
    }
    return arr.filter((n) => n != min);
}