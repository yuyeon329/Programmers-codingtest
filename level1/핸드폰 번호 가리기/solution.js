function solution(phone_number) {
  var answer = '';
  let tmp = "*".repeat(phone_number.length-4)
  let tmp2 = phone_number.slice(-4)
  return tmp+tmp2;
}