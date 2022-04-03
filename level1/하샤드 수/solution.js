function solution(x) {
  let tmp = String(x);
  let tmpsum = 0;
  for(let i = 0; i<tmp.length; i++) {
      tmpsum += Number(tmp[i])
  }
  return x%tmpsum ? false : true;
}