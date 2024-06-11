function solution(x) {
    let arr = x.toString().split('');
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum = sum + Number(arr[i]);
    }
    return x % sum ? false : true;
}