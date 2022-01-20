/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let words=s.split(' ');
    let temp;
    let chars=[];
    for(let i=0;i< words.length;i++){
        for(let j=0;j<words.length-1;j++){
            if(Number(words[j].slice(-1))>Number(words[j+1].slice(-1))){
                temp=words[j+1];
                words[j+1]=words[j];
                words[j]=temp;
            }
        }
    }
    
    for(let i=0;i<words.length;i++){
        chars.push(words[i].slice(0,-1));
    }
    return chars.join(' ');
};
