function getRandomSeconds(max) {
    return Math.floor(Math.random() * Math.floor(max)) * 1000;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

exports.handler = async (event, context) => {
    if(getRandomSeconds(4) === 0) {
        throw new Error("Something went wrong!");
    }

    let wait_time = getRandomSeconds(5);
    await sleep(wait_time);
    return { 'response': true }
};