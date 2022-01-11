/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let array=Array.from(Array(n).keys());
    let output=[];
    for(let i=1;i<=array.length; i++){
        if(i%3!=0 && i%5!=0){
            output.push(`${i}`)
        }
        else if(i%3==0 && i%5!=0){
            output.push('Fizz')
        }
        else if (i%5==0 && i%3!=0){
            output.push('Buzz')
        }
        else if(i%3==0 && i%5==0){
            output.push('FizzBuzz')
        }
    }
    
    return output;
};
