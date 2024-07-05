function solution(arr)
{
    var newArr = [arr[0]];
    var num = arr[0];
    for(let i = 1; i < arr.length; i++){
        if(num != arr[i]){
            num = arr[i];
            newArr.push(num);
        }
    }
    return newArr;
}