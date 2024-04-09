function solution(money) {
    var coffee = parseInt(money / 5500);
    var leftMoney = money - coffee * 5500;
    return [coffee, leftMoney];
}