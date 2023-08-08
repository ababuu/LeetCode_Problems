/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    
    const select=(array,index)=>{
        let selected=index;
        for(let i=index+1;i<array.length;i++){
          if(array[i].slice(-1)<array[selected].slice(-1)){
                selected=i;
          }
        }
        return selected;
    }
    var arr=s.split(' ');
    for(let i=0;i<arr.length;i++){
        const selected=select(arr,i);
        [arr[selected],arr[i]]=[arr[i],arr[selected].slice(0,-1)];
    }
    console.log(arr.join(' '));
    return arr.join(' ');
};

sortSentence("is2 sentence4 This1 a3");
