function solution(arr1, arr2) {
  var answer = [[]];
  
  let arr_r = arr1.length;
  let arr_c = arr1[0].length;
  
  for(let i = 0; i<arr_r; i++){
      answer[i] = [];
      for(let j = 0; j<arr_c; j++){
          answer[i].push(arr1[i][j]+arr2[i][j]);
      }
  }
  
  return answer;
}